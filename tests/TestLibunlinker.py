#TODO Testing of libunlinker
#@author Jean-Baptiste Boric
#@category Test
#@keybinding 
#@menupath 
#@toolbar 

import sys, unittest
sys.path.insert(1, "lib")

from libunlinker import *
from MockProgram import *

class TestUnlinker(unittest.TestCase):
    def _compare(self, object_files, output_dir, reference_dir):
        for object_file in object_files:
            filename = object_file[0] + ".o"
            output = output_dir + "/" + filename
            reference = reference_dir + "/" + filename

            with open(output, "rb") as op:
                with open(reference, "rb") as rp:
                    self.assertEquals(op.read(), rp.read())

    def _weakCompare(self, object_files, output_dir, reference_dir):
        for object_file in object_files:
            filename = object_file[0] + ".o"
            output = output_dir + "/" + filename
            reference = reference_dir + "/" + filename

            with open(output, "rb") as op:
                output_elf = loadElfFromFile(op)
            with open(reference, "rb") as rp:
                reference_elf = loadElfFromFile(rp)

            symbols_output = [symbol for symbol in output_elf.read_symbols() if symbol.st_info & STB_GLOBAL]
            symbols_reference = [symbol for symbol in reference_elf.read_symbols() if symbol.st_info & STB_GLOBAL]
            self.assertEquals(set(symbols_output), set(symbols_reference) & set(symbols_output))

            for section in reference_elf.sections:
                if section.sh_type == SHT_REL and reference_elf.get_section(section.sh_info).sh_flags & SHF_ALLOC == SHF_ALLOC:
                    rels_output = output_elf.read_rel(section.sh_name)
                    rels_reference = reference_elf.read_rel(section.sh_name)
                    self.assertEquals(set(rels_output), set(rels_reference))
                if section.sh_type == SHT_PROGBITS and section.sh_flags & SHF_ALLOC == SHF_ALLOC and len(section.data) > 0:
                    self.assertEquals(len(output_elf.get_section(section.sh_name).data), len(section.data))
                    self.assertEquals(output_elf.get_section(section.sh_name).data, section.data)

    def testHelloWorldMips32ElExec(self):
        from reference.libunlinker.mips32el.linux.helloWorld import currentProgram
        sym_address_start = currentProgram.getAddressFactory().getAddress("004000d0")
        sym_address_end = currentProgram.getAddressFactory().getAddress("0040010f")
        sym_address_set = currentProgram.getAddressFactory().getAddressSet(sym_address_start, sym_address_end)
        object_files = (
            ("helloWorld", (
                ("004000d0", "004000ff", ".text", SHT_PROGBITS, SHF_ALLOC|SHF_EXECINSTR),
                ("00400100", "0040010f", ".rodata", SHT_PROGBITS, SHF_ALLOC),
            )),
        )
        unlink_program(currentProgram, "tests/output/libunlinker/mips32el", object_files, sym_address_set)
        self._weakCompare(object_files, "tests/output/libunlinker/mips32el", "tests/reference/libunlinker/mips32el/linux")

    def testAsciiTableMips32ElExec(self):
        from reference.libunlinker.mips32el.linux.asciiTable import currentProgram
        sym_address_start = currentProgram.getAddressFactory().getAddress("004000d0")
        sym_address_end = currentProgram.getAddressFactory().getAddress("004005ff")
        sym_address_set = currentProgram.getAddressFactory().getAddressSet(sym_address_start, sym_address_end)
        object_files = (
            ("asciiTable", (
                ("004000d0", "0040027f", ".text", SHT_PROGBITS, SHF_ALLOC|SHF_EXECINSTR),
                ("00400490", "004004ef", ".rodata", SHT_PROGBITS, SHF_ALLOC),
            )),
            ("ctype", (
                ("00400280", "0040048f", ".text", SHT_PROGBITS, SHF_ALLOC|SHF_EXECINSTR),
                ("004004f0", "004005ff", ".rodata", SHT_PROGBITS, SHF_ALLOC),
            )),
        )
        unlink_program(currentProgram, "tests/output/libunlinker/mips32el", object_files, sym_address_set)
        self._weakCompare(object_files, "tests/output/libunlinker/mips32el", "tests/reference/libunlinker/mips32el/linux")

if __name__ == '__main__':
    unittest.main()
