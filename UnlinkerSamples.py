# Unlinker script invocations for bundled samples
#@author Jean-Baptiste Boric
#@category Unlinker
#@keybinding 
#@menupath 
#@toolbar 

import logging, os
from lib.libunlinker import *

# tests/reference/libunlinker/mips32el/linux/helloWorld.elf
if currentProgram.executableSHA256 == u'2b972ed9f9071d1c511f13bc841119202f354d5ffc08fe398bc441d5ba25fa7f':
    sym_address_start = currentProgram.getAddressFactory().getAddress("004000d0")
    sym_address_end = currentProgram.getAddressFactory().getAddress("0040010f")
    object_files = (
        ("helloWorld", (
            ("004000d0", "004000ff", ".text", SHT_PROGBITS, SHF_ALLOC|SHF_EXECINSTR),
            ("00400100", "0040010f", ".rodata", SHT_PROGBITS, SHF_ALLOC),
        )),
    )
# tests/reference/libunlinker/mips32el/linux/asciiTable.elf
elif currentProgram.executableSHA256 == u'e4ceb90bd6433a9d9059f9e00be730fd93fb78ebc4506c484069a385d4e98d00':
    sym_address_start = currentProgram.getAddressFactory().getAddress("004000d0")
    sym_address_end = currentProgram.getAddressFactory().getAddress("004005ff")
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
else:
    raise Exception("Unknown SHA256 hash {} of program {}".format(currentProgram.executableSHA256, currentProgram.getName()))

output_dir = askDirectory("Export relocatable objects to", "Save").getPath()

sym_address_set = currentProgram.getAddressFactory().getAddressSet(sym_address_start, sym_address_end)
unlink_program(currentProgram, output_dir, object_files, sym_address_set)
