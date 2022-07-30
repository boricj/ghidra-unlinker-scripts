# Generated from helloWorld.elf
from MockProgram import *
# Data
data = (
  MockData(min_addr=MockAddress(0x400000), max_addr=MockAddress(0x400033)),
  MockData(min_addr=MockAddress(0x400034), max_addr=MockAddress(0x400093)),
  MockData(min_addr=MockAddress(0x4000b0), max_addr=MockAddress(0x4000c7)),
  MockData(min_addr=MockAddress(0x400100), max_addr=MockAddress(0x40010e)),
  MockData(min_addr=MockAddress(0x0), max_addr=MockAddress(0x20)),
  MockData(min_addr=MockAddress(0x0), max_addr=MockAddress(0x3)),
  MockData(min_addr=MockAddress(0x4), max_addr=MockAddress(0x7)),
  MockData(min_addr=MockAddress(0x8), max_addr=MockAddress(0x8)),
  MockData(min_addr=MockAddress(0x9), max_addr=MockAddress(0x9)),
  MockData(min_addr=MockAddress(0xa), max_addr=MockAddress(0xa)),
  MockData(min_addr=MockAddress(0xb), max_addr=MockAddress(0xb)),
  MockData(min_addr=MockAddress(0xc), max_addr=MockAddress(0xc)),
  MockData(min_addr=MockAddress(0xd), max_addr=MockAddress(0xf)),
  MockData(min_addr=MockAddress(0x10), max_addr=MockAddress(0x13)),
  MockData(min_addr=MockAddress(0x14), max_addr=MockAddress(0x17)),
  MockData(min_addr=MockAddress(0x18), max_addr=MockAddress(0x1b)),
  MockData(min_addr=MockAddress(0x1c), max_addr=MockAddress(0x1f)),
  MockData(min_addr=MockAddress(0x0), max_addr=MockAddress(0xc)),
  MockData(min_addr=MockAddress(0x1), max_addr=MockAddress(0x8)),
  MockData(min_addr=MockAddress(0x9), max_addr=MockAddress(0x10)),
  MockData(min_addr=MockAddress(0x11), max_addr=MockAddress(0x1a)),
  MockData(min_addr=MockAddress(0x1b), max_addr=MockAddress(0x29)),
  MockData(min_addr=MockAddress(0x2a), max_addr=MockAddress(0x32)),
  MockData(min_addr=MockAddress(0x33), max_addr=MockAddress(0x38)),
  MockData(min_addr=MockAddress(0x39), max_addr=MockAddress(0x40)),
  MockData(min_addr=MockAddress(0x41), max_addr=MockAddress(0x49)),
  MockData(min_addr=MockAddress(0x4a), max_addr=MockAddress(0x4e)),
  MockData(min_addr=MockAddress(0x4f), max_addr=MockAddress(0x5d)),
  MockData(min_addr=MockAddress(0x5e), max_addr=MockAddress(0x69)),
  MockData(min_addr=MockAddress(0x6a), max_addr=MockAddress(0x77)),
  MockData(min_addr=MockAddress(0x78), max_addr=MockAddress(0x83)),
  MockData(min_addr=MockAddress(0x84), max_addr=MockAddress(0x90)),
  MockData(min_addr=MockAddress(0x91), max_addr=MockAddress(0x9b)),
  MockData(min_addr=MockAddress(0x9c), max_addr=MockAddress(0xab)),
  MockData(min_addr=MockAddress(0xac), max_addr=MockAddress(0xb9)),
  MockData(min_addr=MockAddress(0x1), max_addr=MockAddress(0x13)),
  MockData(min_addr=MockAddress(0x14), max_addr=MockAddress(0x17)),
  MockData(min_addr=MockAddress(0x18), max_addr=MockAddress(0x25)),
  MockData(min_addr=MockAddress(0x26), max_addr=MockAddress(0x2c)),
  MockData(min_addr=MockAddress(0x2d), max_addr=MockAddress(0x34)),
  MockData(min_addr=MockAddress(0x35), max_addr=MockAddress(0x3b)),
  MockData(min_addr=MockAddress(0x3c), max_addr=MockAddress(0x47)),
  MockData(min_addr=MockAddress(0x48), max_addr=MockAddress(0x4e)),
  MockData(min_addr=MockAddress(0x4f), max_addr=MockAddress(0x53)),
  MockData(min_addr=MockAddress(0x54), max_addr=MockAddress(0x59)),
  MockData(min_addr=MockAddress(0x0), max_addr=MockAddress(0x19f)),
  MockData(min_addr=MockAddress(0x0), max_addr=MockAddress(0x2cf)),
)
# Functions
functions = (
  MockFunction(name='__start', body=MockAddressSet(MockAddress(0x4000d0), MockAddress(0x4000f3))),
)
# Memory blocks
memory_blocks = (
  MockMemoryBlock(name='segment_2.1', address_range=MockAddressSet(MockAddress(0x400000), MockAddress(0x400097)).getFirstRange(), data=(127,69,76,70,1,1,1,0,0,0,0,0,0,0,0,0,2,0,8,0,1,0,0,0,-48,0,64,0,52,0,0,0,-40,7,0,0,0,16,0,0,52,0,32,0,3,0,40,0,18,0,17,0,3,0,0,112,-104,0,0,0,-104,0,64,0,-104,0,64,0,24,0,0,0,24,0,0,0,4,0,0,0,8,0,0,0,0,0,0,112,-80,0,0,0,-80,0,64,0,-80,0,64,0,24,0,0,0,24,0,0,0,4,0,0,0,4,0,0,0,1,0,0,0,0,0,0,0,0,0,64,0,0,0,64,0,16,1,0,0,16,1,0,0,5,0,0,0,0,0,1,0,0,0,0,0)),
  MockMemoryBlock(name='.MIPS.abiflags', address_range=MockAddressSet(MockAddress(0x400098), MockAddress(0x4000af)).getFirstRange(), data=(0,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)),
  MockMemoryBlock(name='.reginfo', address_range=MockAddressSet(MockAddress(0x4000b0), MockAddress(0x4000c7)).getFirstRange(), data=(116,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-127,65,0)),
  MockMemoryBlock(name='.text', address_range=MockAddressSet(MockAddress(0x4000d0), MockAddress(0x4000ff)).getFirstRange(), data=(64,0,5,60,-92,15,2,36,1,0,4,36,0,1,-91,36,14,0,6,36,12,0,0,0,-95,15,2,36,37,32,0,0,12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)),
  MockMemoryBlock(name='.rodata', address_range=MockAddressSet(MockAddress(0x400100), MockAddress(0x40010f)).getFirstRange(), data=(72,101,108,108,111,44,32,119,111,114,108,100,33,10,0,0)),
)
# Symbols
symbols = (
  MockSymbol(name='Elf32_Phdr_ARRAY_00400034', fullName='Elf32_Phdr_ARRAY_00400034', address=MockAddress(0x400034), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0x40001c), to_address=MockAddress(0x400034), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='DAT_00400098', fullName='DAT_00400098', address=MockAddress(0x400098), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0x40003c), to_address=MockAddress(0x400098), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
    MockReference(from_address=MockAddress(0x34), to_address=MockAddress(0x400098), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='Elf32_RegInfo_MIPS_004000b0', fullName='Elf32_RegInfo_MIPS_004000b0', address=MockAddress(0x4000b0), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0x40005c), to_address=MockAddress(0x4000b0), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
    MockReference(from_address=MockAddress(0x5c), to_address=MockAddress(0x4000b0), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='__start', fullName='__start', address=MockAddress(0x4000d0), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0x84), to_address=MockAddress(0x4000d0), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
    MockReference(from_address=MockAddress(0x0), to_address=MockAddress(0x4000d0), isPrimary=False, operand_index=-1,
      reftype=MockRefType('EXTERNAL', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
    MockReference(from_address=MockAddress(0x400018), to_address=MockAddress(0x4000d0), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
    MockReference(from_address=MockAddress(0x18), to_address=MockAddress(0x4000d0), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='S_HELLO_WORLD', fullName='S_HELLO_WORLD', address=MockAddress(0x400100), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0xac), to_address=MockAddress(0x400100), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
    MockReference(from_address=MockAddress(0x0), to_address=MockAddress(0x400100), isPrimary=True, operand_index=-1,
      reftype=MockRefType('EXTERNAL', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
    MockReference(from_address=MockAddress(0x4000dc), to_address=MockAddress(0x400100), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='_fdata', fullName='_fdata', address=MockAddress(0x410110), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0x0), to_address=MockAddress(0x410110), isPrimary=False, operand_index=-1,
      reftype=MockRefType('EXTERNAL', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='__bss_start', fullName='__bss_start', address=MockAddress(0x410110), isGlobal=True, references=(
  )),
  MockSymbol(name='_edata', fullName='_edata', address=MockAddress(0x410110), isGlobal=True, references=(
  )),
  MockSymbol(name='_end', fullName='_end', address=MockAddress(0x410110), isGlobal=True, references=(
  )),
  MockSymbol(name='_fbss', fullName='_fbss', address=MockAddress(0x410110), isGlobal=True, references=(
  )),
  MockSymbol(name='_gp', fullName='_gp', address=MockAddress(0x418100), isGlobal=True, references=(
  )),
  MockSymbol(name='_mips_gp0_value', fullName='_mips_gp0_value', address=MockAddress(0x418100), isGlobal=True, references=(
  )),
  MockSymbol(name='s_GCC:_(crosstool-NG_1.24.0)_8.3.0_.comment__00000000', fullName='s_GCC:_(crosstool-NG_1.24.0)_8.3.0_.comment__00000000', address=MockAddress(0x0), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0xd4), to_address=MockAddress(0x0), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='DAT_.debug_abbrev__00000000', fullName='DAT_.debug_abbrev__00000000', address=MockAddress(0x0), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0x174), to_address=MockAddress(0x0), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='DAT_.debug_aranges__00000000', fullName='DAT_.debug_aranges__00000000', address=MockAddress(0x0), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0x124), to_address=MockAddress(0x0), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='cie_.debug_frame::00000000', fullName='cie_.debug_frame::00000000', address=MockAddress(0x0), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0x1c4), to_address=MockAddress(0x0), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
    MockReference(from_address=MockAddress(0x14), to_address=MockAddress(0x0), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='fde_.debug_frame::00000010', fullName='fde_.debug_frame::00000010', address=MockAddress(0x10), isGlobal=True, references=(
  )),
  MockSymbol(name='DAT_.debug_info__00000000', fullName='DAT_.debug_info__00000000', address=MockAddress(0x0), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0x14c), to_address=MockAddress(0x0), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='DAT_.debug_line__00000000', fullName='DAT_.debug_line__00000000', address=MockAddress(0x0), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0x19c), to_address=MockAddress(0x0), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='s___NR_syscall_.debug_str__00000000', fullName='s___NR_syscall_.debug_str__00000000', address=MockAddress(0x0), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0x1ec), to_address=MockAddress(0x0), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='DAT_.gnu.attributes__00000000', fullName='DAT_.gnu.attributes__00000000', address=MockAddress(0x0), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0x214), to_address=MockAddress(0x0), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='DAT_.pdr__00000000', fullName='DAT_.pdr__00000000', address=MockAddress(0x0), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0xfc), to_address=MockAddress(0x0), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='DAT_.shstrtab__00000000', fullName='DAT_.shstrtab__00000000', address=MockAddress(0x0), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0x2b4), to_address=MockAddress(0x0), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='DAT_.strtab__00000000', fullName='DAT_.strtab__00000000', address=MockAddress(0x0), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0x28c), to_address=MockAddress(0x0), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='Elf32_Sym_ARRAY_.symtab__00000000', fullName='Elf32_Sym_ARRAY_.symtab__00000000', address=MockAddress(0x0), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0x264), to_address=MockAddress(0x0), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='Elf32_Shdr_ARRAY__elfSectionHeaders__00000000', fullName='Elf32_Shdr_ARRAY__elfSectionHeaders__00000000', address=MockAddress(0x0), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0x400020), to_address=MockAddress(0x0), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
)
currentProgram = MockProgram(data=data, functions=functions, memory_blocks=memory_blocks, symbols=symbols)
