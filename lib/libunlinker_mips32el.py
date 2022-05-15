from libelf import *
from libelf_mips32el import *
from libunlinker_common import *

def lui_addiu(lui, addiu):
    return ((lui.immediate_i() << 16) & 0xffff0000) + addiu.immediate_i()

def from_jtype(j, reference):
    return (reference.getFromAddress().getOffset() & 0xf0000000) + (j.immediate_j() << 2)

class Mips32Instruction:
    def __init__(self, value):
        self.value = value

    def opcode(self):
        return (self.value >> MIPS32_OPCODE_OFFSET) & MIPS32_OPCODE_MASK

    def sreg(self):
        return (self.value >> MIPS32_SREG_OFFSET) & MIPS32_SREG_MASK

    def treg(self):
        return (self.value >> MIPS32_TREG_OFFSET) & MIPS32_TREG_MASK

    def dreg(self):
        return (self.value >> MIPS32_DREG_OFFSET) & MIPS32_DREG_MASK

    def func(self):
        return self.value & MIPS32_FUNC_MASK

    def immediate_i(self):
        return twos_complement(self.value & MIPS32_ITYPE_IMM_MASK, 16)

    def immediate_j(self):
        return self.value & ~(MIPS32_OPCODE_MASK << MIPS32_OPCODE_OFFSET)

    def zeroed_immediate_i(self):
        return self.value & ~MIPS32_ITYPE_IMM_MASK

    def zeroed_immediate_j(self):
        return self.value & (MIPS32_OPCODE_MASK << MIPS32_OPCODE_OFFSET)

    def __repr__(self):
        return "0x{:8x}".format(self.value)

class InstructionPattern:
    def __init__(self, opcode=None, sreg=None, treg=None, dreg=None, func=None):
        self.opcode = opcode
        self.sreg = sreg
        self.treg = treg
        self.dreg = dreg
        self.func = func

    def match(self, instructions):
        instruction = instructions[-1]
        if test_condition(self.opcode, instruction.opcode(), instructions) and \
                test_condition(self.sreg, instruction.sreg(), instructions) and \
                test_condition(self.treg, instruction.treg(), instructions) and \
                test_condition(self.dreg, instruction.dreg(), instructions) and \
                test_condition(self.func, instruction.func(), instructions):
            return True
        return False

class ReferencePattern:
    def __init__(self, fixup, patterns, operand_index, reftype=None, symbol=None):
        self.fixup = fixup
        self.operand_index = operand_index
        self.patterns = patterns
        self.reftype = reftype
        self.symbol = symbol

    def _build_chains(self, section, offset, min_offset, depth=0, chain=()):
        current_chain = chain + (offset,)
        instructions = tuple(Mips32Instruction(section.read_u32(link)) for link in current_chain)

        if self.patterns[depth].match(instructions):
            if len(current_chain) == len(self.patterns):
                return (current_chain,)
            new_chains = (self._build_chains(section, i, min_offset, depth+1, current_chain) for i in range(offset - 4, min_offset - 4, -4))
            return itertools.chain.from_iterable(new_chains)
        return ()

    def match(self, elf, section, function, reference, symbol, from_offset, to_offset, context):
        if not test_condition(self.operand_index, reference.getOperandIndex(), None):
            return None
        if not test_condition(self.reftype, reference.getReferenceType().getName(), None):
            return None

        min_offset = function.getEntryPoint().subtract(section.section_range.getMinAddress())
        elf_section = elf.get_section(section.section_name)

        chains = tuple(self._build_chains(elf_section, from_offset, min_offset))

        for chain in chains:
            instructions = tuple(Mips32Instruction(elf_section.read_u32(link)) for link in chain)
            fix = self.fixup(chain, instructions, reference, symbol, to_offset, context)
            if fix != None:
                return fix
        return None

def fixup_mips_26(chain, instructions, reference, symbol, to_offset, context):
    if from_jtype(instructions[0], reference) == reference.getToAddress().getOffset():
        return (
            (
                ElfRel(chain[0], symbol, R_MIPS_26),
            ),
            (
                PatchRequest(chain[0], instructions[0].zeroed_immediate_j() + (to_offset >> 2), 4),
            ),
        )
    return None

def fixup_mips_hi16_lo16_lui_itype_offset(chain, instructions, reference, symbol, to_offset, context):
    if lui_addiu(instructions[-1], instructions[-2]) == reference.getToAddress().getOffset():
        return (
            (
                ElfRel(chain[-1], symbol, R_MIPS_HI16),
                ElfRel(chain[-2], symbol, R_MIPS_LO16),
            ),
            (
                PatchRequest(chain[-1], instructions[-1].zeroed_immediate_i(), 4),
                PatchRequest(chain[-2], instructions[-2].zeroed_immediate_i() + to_offset, 4),
            ),
        )
    return None

def fixup_mips_hi16_lo16_lui_addiu_loadstore_offset(chain, instructions, reference, symbol, to_offset, context):
    if lui_addiu(instructions[-1], instructions[-2]) == (reference.getToAddress().getOffset() - to_offset) \
            and instructions[-3].immediate_i() == to_offset:
        return (
            (
                ElfRel(chain[-1], symbol, R_MIPS_HI16),
                ElfRel(chain[-2], symbol, R_MIPS_LO16),
            ),
            (
                PatchRequest(chain[-1], instructions[-1].zeroed_immediate_i(), 4),
                PatchRequest(chain[-2], instructions[-2].zeroed_immediate_i(), 4),
            ),
        )
    return None

def fixup_mips_hi16_lo16_lui_addiu_offset_reg_loadstore(chain, instructions, reference, symbol, to_offset, context):
    if lui_addiu(instructions[-1], instructions[-2]) == (reference.getToAddress().getOffset()) \
            and instructions[-4].immediate_i() == 0:
        return (
            (
                ElfRel(chain[-1], symbol, R_MIPS_HI16),
                ElfRel(chain[-2], symbol, R_MIPS_LO16),
            ),
            (
                PatchRequest(chain[-1], instructions[-1].zeroed_immediate_i(), 4),
                PatchRequest(chain[-2], instructions[-2].zeroed_immediate_i() + to_offset, 4),
            ),
        )
    return None

def fixup_mips_got16_itype_offset(chain, instructions, reference, symbol, to_offset, context):
    if context["gp"] == None:
        return None
    if context["gp"] + instructions[-1].immediate_i() == reference.getToAddress().getOffset():
        return (
            (
                ElfRel(chain[-1], symbol, R_MIPS_GPREL16),
            ),
            (
                PatchRequest(chain[-1], instructions[-1].zeroed_immediate_i() + to_offset, 4),
            ),
        )
    return None

def fixup_mips_got16_addiu_loadstore_offset(chain, instructions, reference, symbol, to_offset, context):
    if context["gp"] == None:
        return None
    if context["gp"] + instructions[-1].immediate_i() == (reference.getToAddress().getOffset() - to_offset) \
            and instructions[-2].immediate_i() == to_offset:
        return (
            (
                ElfRel(chain[-1], symbol, R_MIPS_GPREL16),
            ),
            (
                PatchRequest(chain[-1], instructions[-1].zeroed_immediate_i(), 4),
            ),
        )
    return None

def fixup_mips_got16_addiu_offset_reg_loadstore(chain, instructions, reference, symbol, to_offset, context):
    if context["gp"] == None:
        return None
    if (context["gp"] + instructions[-1].immediate_i() == reference.getToAddress().getOffset()) \
            and instructions[-3].immediate_i() == 0:
        return (
            (
                ElfRel(chain[-1], symbol, R_MIPS_GPREL16),
            ),
            (
                PatchRequest(chain[-1], instructions[-1].zeroed_immediate_i() + to_offset, 4),
            ),
        )
    return None

REFERENCE_PATTERNS=(
# Call/jump
    ReferencePattern(
        reftype=(UNCONDITIONAL_CALL, UNCONDITIONAL_JUMP),
        operand_index=0,
        patterns=tuple(reversed((
            InstructionPattern(opcode=(MIPS32_OPCODE_J, MIPS32_OPCODE_JAL)),
        ))),
        fixup=fixup_mips_26,
    ),
    ReferencePattern(
        reftype=COMPUTED_CALL,
        operand_index=0,
        patterns=tuple(reversed((
            InstructionPattern(opcode=MIPS32_OPCODE_LUI, treg=lambda reg, instructions : reg == instructions[1].sreg()),
            InstructionPattern(opcode=MIPS32_OPCODE_ADDIU, treg=lambda reg, instructions : reg == instructions[0].sreg()),
            InstructionPattern(opcode=MIPS32_OPCODE_REG, func=(MIPS32_OPCODE_JR, MIPS32_OPCODE_JALR), sreg=MIPS32_REGS_NOT_GP),
        ))),
        fixup=fixup_mips_hi16_lo16_lui_itype_offset,
    ),
# Not GP-relative
    ReferencePattern(
        reftype=(DATA, PARAM),
        operand_index=0,
        patterns=tuple(reversed((
            InstructionPattern(opcode=MIPS32_OPCODE_LUI, treg=lambda reg, instructions : reg == instructions[0].sreg()),
            InstructionPattern(opcode=MIPS32_OPCODE_ADDIU, sreg=MIPS32_REGS_NOT_GP),
        ))),
        fixup=fixup_mips_hi16_lo16_lui_itype_offset,
    ),
    ReferencePattern(
        reftype=(DATA, PARAM),
        operand_index=(0, 1),
        patterns=tuple(reversed((
            InstructionPattern(opcode=MIPS32_OPCODE_LUI, treg=lambda reg, instructions : reg == instructions[1].sreg()),
            InstructionPattern(opcode=MIPS32_OPCODE_ADDIU, treg=lambda reg, instructions : reg in (instructions[0].sreg(), instructions[0].treg())),
            InstructionPattern(opcode=MIPS32_OPCODE_REG, func=MIPS32_FUNC_ADDU),
        ))),
        fixup=fixup_mips_hi16_lo16_lui_itype_offset,
    ),
    ReferencePattern(
        reftype=(READ, WRITE),
        operand_index=1,
        patterns=tuple(reversed((
            InstructionPattern(opcode=MIPS32_OPCODE_LUI, treg=lambda reg, instructions : reg == instructions[0].sreg()),
            InstructionPattern(opcode=MIPS32_OPCODES_LOADSTORE, sreg=MIPS32_REGS_NOT_GP),
        ))),
        fixup=fixup_mips_hi16_lo16_lui_itype_offset,
    ),
    ReferencePattern(
        reftype=(READ, WRITE),
        operand_index=1,
        patterns=tuple(reversed((
            InstructionPattern(opcode=MIPS32_OPCODE_LUI, treg=lambda reg, instructions : reg == instructions[1].sreg()),
            InstructionPattern(opcode=MIPS32_OPCODE_ADDIU, treg=lambda reg, instructions : reg == instructions[0].sreg()),
            InstructionPattern(opcode=MIPS32_OPCODES_LOADSTORE, sreg=MIPS32_REGS_NOT_GP),
        ))),
        fixup=fixup_mips_hi16_lo16_lui_addiu_loadstore_offset,
    ),
    ReferencePattern(
        reftype=(READ, WRITE),
        operand_index=(0, 1),
        patterns=tuple(reversed((
            InstructionPattern(opcode=MIPS32_OPCODE_LUI, treg=lambda reg, instructions : reg == instructions[2].sreg()),
            InstructionPattern(opcode=MIPS32_OPCODE_ADDIU, treg=lambda reg, instructions : reg in (instructions[1].sreg(), instructions[1].treg())),
            InstructionPattern(opcode=MIPS32_OPCODE_REG, func=MIPS32_FUNC_ADDU, dreg=lambda reg, instructions : reg == instructions[0].sreg()),
            InstructionPattern(opcode=MIPS32_OPCODES_LOADSTORE, sreg=MIPS32_REGS_NOT_GP),
        ))),
        fixup=fixup_mips_hi16_lo16_lui_addiu_offset_reg_loadstore,
    ),
# GP-relative
    ReferencePattern(
        reftype=(DATA, PARAM),
        operand_index=0,
        patterns=tuple(reversed((
            InstructionPattern(opcode=MIPS32_OPCODE_ADDIU, sreg=MIPS32_REG_GP),
        ))),
        fixup=fixup_mips_got16_itype_offset,
    ),
    ReferencePattern(
        reftype=(DATA, PARAM),
        operand_index=(0, 1),
        patterns=tuple(reversed((
            InstructionPattern(opcode=MIPS32_OPCODE_ADDIU, treg=lambda reg, instructions : reg in (instructions[0].sreg(), instructions[0].treg()), sreg=MIPS32_REG_GP),
            InstructionPattern(opcode=MIPS32_OPCODE_REG, func=MIPS32_FUNC_ADDU),
        ))),
        fixup=fixup_mips_got16_itype_offset,
    ),
    ReferencePattern(
        reftype=(READ, WRITE),
        operand_index=1,
        patterns=tuple(reversed((
            InstructionPattern(opcode=MIPS32_OPCODES_LOADSTORE, sreg=MIPS32_REG_GP),
        ))),
        fixup=fixup_mips_got16_itype_offset,
    ),
    ReferencePattern(
        reftype=(READ, WRITE),
        operand_index=1,
        patterns=tuple(reversed((
            InstructionPattern(opcode=MIPS32_OPCODE_ADDIU, treg=lambda reg, instructions : reg == instructions[0].sreg(), sreg=MIPS32_REG_GP),
            InstructionPattern(opcode=MIPS32_OPCODES_LOADSTORE, sreg=MIPS32_REGS_NOT_GP),
        ))),
        fixup=fixup_mips_got16_addiu_loadstore_offset,
    ),
    ReferencePattern(
        reftype=(READ, WRITE),
        operand_index=(0, 1),
        patterns=tuple(reversed((
            InstructionPattern(opcode=MIPS32_OPCODE_ADDIU, treg=lambda reg, instructions : reg in (instructions[1].sreg(), instructions[1].treg()), sreg=MIPS32_REG_GP),
            InstructionPattern(opcode=MIPS32_OPCODE_REG, func=MIPS32_FUNC_ADDU, dreg=lambda reg, instructions : reg == instructions[0].sreg()),
            InstructionPattern(opcode=MIPS32_OPCODES_LOADSTORE, sreg=MIPS32_REGS_NOT_GP),
        ))),
        fixup=fixup_mips_got16_addiu_offset_reg_loadstore,
    ),
)

class ElfRelocatableObjectMips32l(ElfFile):
    def __init__(self):
        ElfFile.__init__(self, ELFCLASS32, ELFDATA2LSB, ELF_ET_REL, ELF_EM_MIPS, e_flags=0x1000)
        self.relocations = dict()

    def delocate_text(self, section, function, reference, symbol, from_offset, to_offset, context):
        instruction = Mips32Instruction(self.get_section(section.section_name).read_u32(from_offset))
        reftype = reference.getReferenceType()

        if instruction.opcode() in MIPS32_OPCODES_RELATIVE_JUMPS and section.section_range.contains(reference.getToAddress()):
            # Relative branches within section
            return ((), ())
        elif instruction.opcode() == MIPS32_OPCODE_J and function.getBody().contains(reference.getToAddress()):
            # Absolute jump within function
            to_offset = reference.getToAddress().subtract(section.section_range.getMinAddress())
            symbol = section.section_name

        for pattern in REFERENCE_PATTERNS:
            result = pattern.match(self, section, function, reference, symbol, from_offset, to_offset, context)
            if result != None:
                return result
        return None

    def delocate_data(self, section, reference, symbol, from_offset, to_offset, context):
        return (
            (
                ElfRel(from_offset, symbol, R_MIPS_32),
            ),
            (
                PatchRequest(from_offset, to_offset, 4),
            ),
        )

    def finalize(self):
        if self.has_section(".text"):
            self.append(ElfSection(".reginfo", SHT_MIPS_REGINFO, sh_link=".text", data=bytearray("\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1C")))
