#TODO Script library for unlinking a section
#@author Jean-Baptiste Boric
#@category ScriptLibrary
#@keybinding
#@menupath
#@toolbar

import itertools, jarray, logging, re
from collections import defaultdict

from libelf import *
from libunlinker_mips32el import *

class SectionAnalyzer:
    RE_SUBSCRIPT = re.compile("^([^.[]+)(\[\d+\]|\.).*$")
    RE_LABEL = re.compile("^LAB_.*$")

    def __init__(self, program, section_name, section_range, section_type, section_flags, sym_address_set):
        self.program = program
        self.section_name = section_name
        self.section_range = section_range
        self.section_type = section_type
        self.section_flags = section_flags
        self.sym_address_set = sym_address_set

        self.internal_symbols = set()
        self.external_symbols = set()

        self.internal_to_internal = dict()
        self.internal_to_external = dict()
        self.external_to_internal = dict()

        self._isolate_section()

    def _interesting_symbol(self, symbol_name):
        if self.RE_LABEL.match(symbol_name) != None:
            return False

        match = self.RE_SUBSCRIPT.match(symbol_name)
        if match:
            next_symbol = next(self.program.getSymbolTable().getSymbols(match.group(1)))
            if next_symbol != None:
                return False

        return True

    def _normalize_symbol(self, symbol):
        match = self.RE_SUBSCRIPT.match(symbol.getName())
        if match:
            next_symbol = next(self.program.getSymbolTable().getSymbols(match.group(1)))
            if next_symbol == None:
                logging.getLogger("unlinker.sym").warning("Cannot normalize subscript symbol {}".format(symbol))
            else:
                return next_symbol

        return symbol

    def _isolate_section(self):
        for symbol in self.program.getSymbolTable().getAllSymbols(True):
            symbol_address = symbol.getAddress()
            symbol_name = symbol.getName()

            if self.section_range.contains(symbol_address):
                if self._interesting_symbol(symbol_name):
                    self.internal_symbols.add(symbol)
                for reference in symbol.getReferences():
                    if reference.isPrimary() == False:
                        continue
                    from_address = reference.getFromAddress()
                    if self.section_range.contains(from_address):
                        offset = reference.getToAddress().subtract(symbol.getAddress())
                        self.internal_to_internal[reference] = (symbol, offset)
                    elif self.sym_address_set.contains(from_address):
                        self.external_to_internal[reference] = symbol
            elif self.sym_address_set.contains(symbol_address):
                for reference in symbol.getReferences():
                    if reference.isPrimary() == False:
                        continue
                    from_address = reference.getFromAddress()
                    if self.section_range.contains(from_address):
                        normalized_symbol = self._normalize_symbol(symbol)
                        offset = reference.getToAddress().subtract(normalized_symbol.getAddress())
#                        if symbol.getName()[:4] == "DAT_":
#                            logging.getLogger("unlinker.sym").warning("Symbol {} of reference {} hasn't been given a name".format(symbol, reference))
#                            pass
                        self.internal_to_external[reference] = (normalized_symbol, offset)

        for reference, (symbol, offset) in self.internal_to_external.iteritems():
            self.external_symbols.add(symbol)

        #FIXME: 1st arg can't be coerced to ghidra.program.model.address.Address, ghidra.program.model.address.AddressSetView
        #self.functions = list(self.program.getFunctionManager().getFunctions(self.section_range, True))
        self.functions = list(self.program.getFunctionManager().getFunctions(self.program.getAddressFactory().getAddressSet(self.section_range.getMinAddress(), self.section_range.getMaxAddress()), True))

class ElfRelocatableObjectExporter:
    def __init__(self, program, relocatable_object, analyzed_sections, context):
        self.elf = relocatable_object
        self.program = program
        self.context = context

        self.symbols = list()
        self.internal_symbols = set()
        self.external_symbols = set()
        for analyzed_section in analyzed_sections:
            self.internal_symbols |= analyzed_section.internal_symbols
            self.external_symbols |= analyzed_section.external_symbols
        self.external_symbols -= analyzed_section.internal_symbols

        for analyzed_section in analyzed_sections:
            self.symbols.append(ElfSymbol(analyzed_section.section_name, 0, 0, STB_LOCAL|STT_SECTION, 0, analyzed_section.section_name))

        for analyzed_section in analyzed_sections:
            self._add_section(analyzed_section)
            self._build_internal_symbol_table(program, analyzed_section.section_name, analyzed_section.section_range, analyzed_section.internal_symbols)

        self._build_external_symbol_table(program, self.external_symbols)
        self.elf.synthesize_symbols(sorted(self.symbols))

        for analyzed_section in analyzed_sections:
            if (analyzed_section.section_flags & (SHF_ALLOC | SHF_EXECINSTR)) == SHF_ALLOC | SHF_EXECINSTR:
                self._build_relocations_text(program, analyzed_section)
            elif (analyzed_section.section_flags & SHF_ALLOC) == SHF_ALLOC:
                self._build_relocations_data(program, analyzed_section)
            else:
                logging.getLogger("unlinker.rel").error("Section {} is neither text or data".format(analyzed_section.section_name))

        self.elf.finalize()

    def _add_section(self, section):
        section_data = jarray.zeros(section.section_range.getLength(), "b")
        if section.section_type != SHT_NOBITS:
            self.program.getMemory().getBytes(section.section_range.getMinAddress(), section_data)
        section = ElfSection(section.section_name, section.section_type, sh_flags=section.section_flags, sh_addralign=1, data=bytearray(section_data))
        self.elf.append(section)

    def _build_internal_symbol_table(self, program, section_name, section_range, internal_symbols):
        for symbol in internal_symbols:
            address = symbol.getAddress()
            section_address = address.subtract(section_range.getMinAddress())
            function = program.getFunctionManager().getFunctionAt(address)
            data = program.getListing().getDataAt(address)

            if symbol.isGlobal():
                st_info = STB_GLOBAL
            else:
                st_info = STB_LOCAL

            if function != None and function.getEntryPoint() == address:
                st_length = function.getBody().getNumAddresses()
                st_info |= STT_FUNC
            elif data != None:
                st_length = data.getLength()
                st_info |= STT_OBJECT
            else:
                st_length = 0
                st_info |= STT_NOTYPE

            self.symbols.append(ElfSymbol(symbol.getName(), section_address, st_length, st_info, 0, section_name))

    def _build_external_symbol_table(self, program, external_symbols):
        for symbol in external_symbols:
            address = symbol.getAddress()

            elf_symbol = ElfSymbol(symbol.getName(), 0, 0, STB_GLOBAL, 0, "")
            self.symbols.append(elf_symbol)

    def _build_relocations_text(self, program, section):
        relocations = defaultdict(set)
        patches = defaultdict(set)

        for reference, (symbol, to_offset) in itertools.chain(section.internal_to_external.iteritems(), section.internal_to_internal.iteritems()):
            from_address = reference.getFromAddress()
            from_offset = from_address.subtract(section.section_range.getMinAddress())
            function = program.getFunctionManager().getFunctionContaining(from_address)
            rels = None

            if function != None:
                rels = self.elf.delocate_text(section, function, reference, symbol.getName(), from_offset, to_offset, self.context)
            if rels != None:
                for processed_relocation in rels[0]:
                    relocations[processed_relocation.r_address].add(processed_relocation)
                for processed_patch in rels[1]:
                    patches[processed_patch.offset].add(processed_patch)
            else:
                logging.getLogger("unlinker.rel").error("Unsupported text delocation reference {} from_offset {} to_offset {} symbol {}".format(reference, from_offset, to_offset, symbol))

        self._synthesize_relocations(section, relocations, patches)

    def _build_relocations_data(self, program, section):
        relocations = defaultdict(set)
        patches = defaultdict(set)

        for reference, (symbol, to_offset) in itertools.chain(section.internal_to_external.iteritems(), section.internal_to_internal.iteritems()):
            from_address = reference.getFromAddress()
            from_offset = from_address.subtract(section.section_range.getMinAddress())

            rels = self.elf.delocate_data(section, reference, symbol.getName(), from_offset, to_offset, self.context)
            if rels != None:
                for processed_relocation in rels[0]:
                    relocations[processed_relocation.r_address].add(processed_relocation)
                for processed_patch in rels[1]:
                    patches[processed_patch.offset].add(processed_patch)
            else:
                logging.getLogger("unlinker.rel").error("Unsupported data delocation reference {} from_offset {} to_offset {} symbol {}".format(reference, from_offset, to_offset, symbol))

        self._synthesize_relocations(section, relocations, patches)

    def _synthesize_relocations(self, section, relocations_dict, patches_dict):
        if len(relocations_dict) == 0:
            return

        relocations_list = list()
        elf_section = self.elf.get_section(section.section_name)

        for offset in sorted(relocations_dict.keys()):
            relocations = relocations_dict[offset]
            if len(relocations) > 1:
                logging.getLogger("unlinker.rel").error("Multiple conflicting relocations @ 0x{:x}: {}".format(offset, relocations))
            relocations_list.extend(relocations)

        for offset in sorted(patches_dict.keys()):
            patches = patches_dict[offset]
            if len(patches) > 1:
                logging.getLogger("unlinker.rel").error("Multiple conflicting patches @ 0x{:x}: {}".format(offset, patches))
            for patch in patches:
                if patch.length == 4:
                    elf_section.write_u32(patch.offset, patch.value)
                else:
                    raise Exception("Don't know how to patch with length " + str(patch.length))

        self.elf.synthesize_relocations(relocations_list, info_section=section.section_name)

def unlink_program(currentProgram, output_dir, object_files, sym_address_set):
    for object_file in object_files:
        output_path = output_dir + '/' + object_file[0] + '.o'
        log_path = output_path + ".log"
        sections = list()
        print(" --- Processing object file {}".format(output_path))

        try:
            os.remove(log_path)
        except:
            pass
        log_file = logging.FileHandler(log_path)
        logging.getLogger("unlinker").addHandler(log_file)

        for object_section in object_file[1]:
            start_address = currentProgram.getAddressFactory().getAddress(object_section[0])
            end_address = currentProgram.getAddressFactory().getAddress(object_section[1])
            section_name = object_section[2]
            section_type = object_section[3]
            section_flags = object_section[4]
            section_range = currentProgram.getAddressFactory().getAddressSet(start_address, end_address).getFirstRange()

            gp = next(currentProgram.getSymbolTable().getSymbols("_gp"))
            if gp != None:
                gp = gp.getAddress().getOffset()
            context = {
                "gp": gp,
            }

            print("      * Processing section {} {}".format(section_name, section_range))
            section = SectionAnalyzer(currentProgram, section_name, section_range, section_type, section_flags, sym_address_set)
            sections.append(section)

        with open(output_path, "wb") as fp:
            elf = ElfRelocatableObjectMips32l()
            exporter = ElfRelocatableObjectExporter(currentProgram, elf, sections, context)
            elf.write(fp)

        logging.getLogger("unlinker").removeHandler(log_file)
        log_file.close()
