#TODO Testing of libelf
#@author Jean-Baptiste Boric
#@category Test
#@keybinding 
#@menupath 
#@toolbar 

import io, sys, unittest
sys.path.insert(1, "lib")

from libelf import *

def generateTestEmptyMips32ElRel():
    return ElfFile(ELFCLASS32, ELFDATA2LSB, ELF_ET_REL, ELF_EM_MIPS, e_flags=0x1000)

def generateTestMemcpyMips32ElRel():
    elf = ElfFile(ELFCLASS32, ELFDATA2LSB, ELF_ET_REL, ELF_EM_MIPS, e_flags=0x1000)
    text_section = ElfSection(".text", SHT_PROGBITS, SHF_ALLOC|SHF_EXECINSTR, data=b"\x06\x00\xc0\x18\x21\x30\x86\x00\x01\x00\xa5\x24\x01\x00\x84\x24\xff\xff\xa2\x80\xfc\xff\xc4\x14\xff\xff\x82\xa0\x08\x00\xe0\x03\x00\x00\x00\x00")
    reginfo_section = ElfSection(".reginfo", SHT_MIPS_REGINFO, sh_link=".text", data=b"\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1C")

    elf.append(text_section)
    elf.append(reginfo_section)

    symbols = list((
        ElfSymbol("my_memcpy", 0, 48, STT_FUNC|STB_GLOBAL, 0, ".text"),
    ))
    elf.synthesize_symbols(symbols)

    return elf

def generateTestHelloWorldMips32ElRel():
    elf = ElfFile(ELFCLASS32, ELFDATA2LSB, ELF_ET_REL, ELF_EM_MIPS, e_flags=0x1000)
    text_section = ElfSection(".text", SHT_PROGBITS, SHF_ALLOC|SHF_EXECINSTR, data=b"\xd8\xff\xbd\x27\x00\x00\x05\x3c\x10\x00\xa4\x27\x0f\x00\x06\x24\x24\x00\xbf\xaf\x00\x00\x00\x0c\x00\x00\xa5\x24\xa4\x0f\x02\x24\x01\x00\x04\x24\x10\x00\xa5\x27\x0e\x00\x06\x24\x0c\x00\x00\x00\xa1\x0f\x02\x24\x25\x20\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00")
    rodata_section = ElfSection(".rodata", SHT_PROGBITS, SHF_ALLOC, data=b"Hello, world!\n\0")
    reginfo_section = ElfSection(".reginfo", SHT_MIPS_REGINFO, sh_link=".text", data=b"\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1C")

    elf.append(text_section)
    elf.append(rodata_section)
    elf.append(reginfo_section)

    symbols = list((
        ElfSymbol("__start", 0, 96, STT_FUNC|STB_GLOBAL, 0, ".text"),
        ElfSymbol("$LC0", 0, 16, STT_NOTYPE|STB_GLOBAL, 0, ".rodata"),
        ElfSymbol("my_memcpy", 0, 0, STT_FUNC|STB_GLOBAL, 0, ""),
    ))
    elf.synthesize_symbols(symbols)

    relocations = list((
        ElfRel(0x4, "$LC0", R_MIPS_HI16),
        ElfRel(0x14, "my_memcpy", R_MIPS_26),
        ElfRel(0x18, "$LC0", R_MIPS_LO16),
    ))
    elf.synthesize_relocations(relocations)

    return elf

class TestElfFile(unittest.TestCase):
    def _compare(self, elf, reference):
        with open("tests/output/libelf/" + reference, "wb") as fp:
            elf.write(fp)
        with io.BytesIO() as mp:
            elf.write(mp)
            with open("tests/reference/libelf/" + reference, "rb") as fp:
                self.assertEquals(mp.getvalue(), fp.read())

    def testEmptyMips32ElRel(self):
        elf = generateTestEmptyMips32ElRel()
        self._compare(elf, "mips32el/testEmpty.o")

    def testMemcpyMips32ElRel(self):
        elf = generateTestMemcpyMips32ElRel()
        self._compare(elf, "mips32el/testMemcpy.o")

    def testHelloWorldMips32ElRel(self):
        elf = generateTestHelloWorldMips32ElRel()
        self._compare(elf, "mips32el/testHelloWorld.o")

    def testLoadSave(self):
        with open("tests/reference/libelf/mips32el/testLoadSave.o", "rb") as fp:
            elf = loadElfFromFile(fp)

        self._compare(elf, "mips32el/testLoadSave.o")

    def testLoadSaveNobitsMips32ElRel(self):
        with open("tests/reference/libelf/mips32el/testLoadSaveNoBits.o", "rb") as fp:
            elf = loadElfFromFile(fp)

        self._compare(elf, "mips32el/testLoadSaveNoBits.o")

if __name__ == '__main__':
    unittest.main()
