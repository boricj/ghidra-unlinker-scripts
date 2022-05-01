#TODO Script library for writing ELF files
#@author Jean-Baptiste Boric
#@category ScriptLibrary
#@keybinding
#@menupath
#@toolbar

#TODO Make it 64-bit ELF compatible

import itertools, jarray, struct

ELFCLASSNONE = 0
ELFCLASS32 = 1
ELFCLASS64 = 2

ELFDATANONE = 0
ELFDATA2LSB = 1
ELFDATA2MSB = 2

EV_NONE = 0
EV_CURRENT = 1

ELFOSABI_SYSV = 0
ELFOSABI_HPUX = 1
ELFOSABI_NETBSD = 2
ELFOSABI_LINUX = 3
ELFOSABI_HURD = 4
ELFOSABI_86OPEN = 5
ELFOSABI_SOLARIS = 6
ELFOSABI_MONTEREY = 7
ELFOSABI_IRIX = 8
ELFOSABI_FREEBSD = 9
ELFOSABI_TRU64 = 10
ELFOSABI_MODESTO = 11
ELFOSABI_OPENBSD = 12
ELFOSABI_ARM = 97
ELFOSABI_STANDALONE = 255

ELF_ET_NONE = 0
ELF_ET_REL = 1
ELF_ET_EXEC = 2
ELF_ET_DYN = 3
ELF_ET_CORE = 4

ELF_EM_MIPS = 8

ELF_EV_NONE = 0
ELF_EV_CURRENT = 1

elf32_hdr = "<4c12BHHIIIIIHHHHHH"
elf32_hdr_size = struct.calcsize(elf32_hdr)
elf32_sym = "<IIIBBH"
elf32_sym_size = struct.calcsize(elf32_sym)

SHT_NULL = 0
SHT_PROGBITS = 1
SHT_SYMTAB = 2
SHT_STRTAB = 3
SHT_RELA = 4
SHT_HASH = 5
SHT_DYNAMIC = 6
SHT_NOTE = 7
SHT_NOBITS = 8
SHT_REL = 9
SHT_SHLIB = 10
SHT_DYNSYM = 11
SHT_MIPS_LIBLIST = 0x70000000
SHT_MIPS_CONFLICT = 0x70000002
SHT_MIPS_GPTAB = 0x70000003
SHT_MIPS_UCODE = 0x70000004
SHT_MIPS_DEBUG = 0x70000005
SHT_MIPS_REGINFO = 0x70000006

SHF_WRITE = 0x1
SHF_ALLOC = 0x2
SHF_EXECINSTR = 0x4
SHF_MIPS_GPREL = 0x10000000

elf32_shdr = "<IIIIIIIIII"
elf32_shdr_size = struct.calcsize(elf32_shdr)

STB_LOCAL = 0 << 4
STB_GLOBAL = 1 << 4
STB_WEAK = 2 << 4

STT_NOTYPE = 0
STT_OBJECT = 1
STT_FUNC = 2
STT_SECTION = 3
STT_FILE = 4
STT_COMMON = 5
STT_TLS = 6
STT_NUM = 7

elf32_sym = "<IIIBBH"
elf32_sym_size = struct.calcsize(elf32_sym)

R_MIPS_NONE = 0
R_MIPS_16 = 1
R_MIPS_32 = 2
R_MIPS_REL32 = 3
R_MIPS_26 = 4
R_MIPS_HI16 = 5
R_MIPS_LO16 = 6
R_MIPS_GPREL16 = 7
R_MIPS_LITERAL = 8
R_MIPS_GOT16 = 9
R_MIPS_PC16 = 10
R_MIPS_CALL16 = 11
R_MIPS_GPREL32 = 12

elf32_rel = "<II"
elf32_rel_size = struct.calcsize(elf32_rel)

elf32_rela = "<III"
elf32_rela_size = struct.calcsize(elf32_rel)

def loadElfFromFile(fp):
    hdr = struct.unpack(elf32_hdr, fp.read(elf32_hdr_size))

    sh_off = hdr[21]
    sh_num = hdr[27]
    sh_stridx = hdr[28]
    raw_section_hdrs = list()
    raw_section_datas = list()

    for section_idx in range(0, sh_num):
        fp.seek(sh_off + section_idx * elf32_shdr_size, 0)
        raw_section_hdr = struct.unpack(elf32_shdr, fp.read(elf32_shdr_size))
        raw_section_hdrs.append(raw_section_hdr)
        if raw_section_hdr[1] == SHT_NOBITS:
            raw_section_datas.append("\0" * raw_section_hdr[5])
        else:
            fp.seek(raw_section_hdr[4], 0)
            raw_section_datas.append(fp.read(raw_section_hdr[5]))

    sections = list()
    raw_shstr = raw_section_datas[sh_stridx]
    for raw_section_hdr, raw_section_data in zip(raw_section_hdrs, raw_section_datas):
        section_name = raw_shstr[raw_section_hdr[0]:raw_shstr.find("\0", raw_section_hdr[0])]
        section = ElfSection(section_name, raw_section_hdr[1], sh_flags=raw_section_hdr[2], sh_link="", sh_info="", sh_addralign=raw_section_hdr[8], sh_entsize=raw_section_hdr[9], data=raw_section_data)
        sections.append(section)

    for raw_section_hdr, section in zip(raw_section_hdrs, sections):
        section.sh_link = sections[raw_section_hdr[6]].sh_name
        section.sh_info = sections[raw_section_hdr[7]].sh_name

    return ElfFile(hdr[4], hdr[5], hdr[16], hdr[17], sections=sections)

def twos_complement(value, length):
    return value if value < (1 << (length - 1)) else value - (1 << length)

class ElfFile:
    def __init__(self, e_class, e_data, e_type, e_machine, e_flags=0, sections=None):
        self.e_class = e_class
        self.e_data = e_data
        self.e_type = e_type
        self.e_machine = e_machine
        self.e_flags = e_flags

        if sections != None:
            self.sections = sections
        else:
            self.sections = list()
            self.sections.append(ElfSection("", SHT_NULL))
            self.sections.append(ElfSection(".shstrtab", SHT_STRTAB))
            self.sections[1].data = "\0.shstrtab\0"

    def shname2idx(self, name):
        for idx, section in enumerate(self.sections):
            if section.sh_name == name:
                return idx
        raise Exception("section " + name + " not found")

    def get_section(self, name):
        return self.sections[self.shname2idx(name)]

    def has_section(self, name):
        for idx, section in enumerate(self.sections):
            if section.sh_name == name:
                return True
        return False

    def find_symbol_idx(self, name, section=".symtab"):
        sym_section = self.sections[self.shname2idx(section)]
        str_section = self.sections[self.shname2idx(sym_section.sh_link)]

        try:
            offset = str_section.data.index(("\0" + name + "\0").encode("ascii")) + 1
            symtab_data = sym_section.data

            for i in range(0, len(symtab_data), elf32_sym_size):
                symbol = struct.unpack_from(elf32_sym, symtab_data, i)
                if symbol[0] == offset:
                    return i / elf32_sym_size
        except ValueError:
            pass

        raise Exception("symbol " + name + " not found")

    def write(self, fp):
        hdr = struct.pack(elf32_hdr,
            '\x7f', 'E', 'L', 'F', self.e_class, self.e_data, EV_CURRENT, ELFOSABI_SYSV, 0, 0, 0, 0, 0, 0, 0, 0,
            self.e_type, self.e_machine, ELF_EV_CURRENT, 0, 0, elf32_hdr_size, self.e_flags, elf32_hdr_size, 0, 0, elf32_shdr_size, len(self.sections), self.shname2idx(".shstrtab")
        )
        fp.write(hdr)

        offset = elf32_hdr_size + len(self.sections) * elf32_shdr_size
        for section in self.sections:
            sh_name_offset = self.sections[self.shname2idx(".shstrtab")].data.find((section.sh_name + "\0").encode("ascii"))
            shdr = struct.pack(elf32_shdr,
                sh_name_offset, section.sh_type, section.sh_flags, 0, offset, len(section.data), self.shname2idx(section.sh_link), self.shname2idx(section.sh_info), section.sh_addralign, section.sh_entsize
            )
            fp.write(shdr)
            if section.sh_type != SHT_NOBITS:
                offset += len(section.data)
        for section in self.sections:
            if section.sh_type != SHT_NOBITS:
                fp.write(section.data)

    def append(self, section):
        self.sections[self.shname2idx(".shstrtab")].data += (section.sh_name + "\0").encode("ascii")
        self.sections.append(section)

    def synthesize_symbols(self, symbols, section=".symtab", str_section=".strtab"):
        symtab_data = bytearray()
        strtab_data = bytearray()

        # Null symbol name and data
        strtab_data += "\0".encode("ascii")
        symtab_data += struct.pack(elf32_sym,
            0, 0, 0, 0, 0, 0
        )

        for symbol in symbols:
            name_offset = len(strtab_data)
            strtab_data += (symbol.st_name + "\0").encode("ascii")
            symtab_data += struct.pack(elf32_sym,
                name_offset, symbol.st_value, symbol.st_size, symbol.st_info, symbol.st_others, self.shname2idx(symbol.st_section)
            )

        self.append(ElfSection(section, SHT_SYMTAB, sh_link=str_section, sh_entsize=elf32_sym_size, data=symtab_data))
        self.append(ElfSection(str_section, SHT_STRTAB, data=strtab_data))

    def read_symbols(self, section=".symtab"):
        section_symtab = self.get_section(section)
        if section_symtab.sh_type != SHT_SYMTAB:
            raise Exception("section type of " + section_symtab.sh_name + " is not SYMTAB")

        section_strtab = self.get_section(section_symtab.sh_link)
        if section_strtab.sh_type != SHT_STRTAB:
            raise Exception("section type of " + section_strtab.sh_name + " is not STRTAB")
        strtab_data = section_strtab.data

        symbols = list()
        for raw_symbol in itertools.izip_longest(*[iter(section_symtab.data)] * struct.calcsize(elf32_sym)):
            symbol_data = struct.unpack(elf32_sym, bytearray(raw_symbol))
            # FIXME: Handle special section indexes
            if symbol_data[5] >= 0xff00:
                symbol_data=(0, 0, 0, 0, 0, 0)
            symbol_name = strtab_data[symbol_data[0]:strtab_data.find("\0", symbol_data[0])]
            symbols.append(ElfSymbol(symbol_name, symbol_data[1], symbol_data[2], symbol_data[3], symbol_data[4], self.sections[symbol_data[5]].sh_name))
        return symbols

    def synthesize_relocations(self, relocations, info_section=".text", link_section=".symtab"):
        rel_data = bytearray()

        for relocation in relocations:
            symbol_idx = self.find_symbol_idx(relocation.r_symbol, link_section)
            rel_data += struct.pack(elf32_rel,
                relocation.r_address, symbol_idx << 8 | relocation.r_type
            )

        self.append(ElfSection(".rel" + info_section, SHT_REL, sh_link=link_section, sh_info=info_section, sh_entsize=elf32_rel_size, data=rel_data))

    def read_rel(self, section):
        section_rel = self.get_section(section)
        if section_rel.sh_type != SHT_REL:
            raise Exception("section type of " + section_rel.sh_name + " is not REL")

        symbols = self.read_symbols(section_rel.sh_link)

        rels = list()
        for raw_rel in itertools.izip_longest(*[iter(section_rel.data)] * struct.calcsize(elf32_rel)):
            rel_data = struct.unpack(elf32_rel, bytearray(raw_rel))
            rels.append(ElfRel(rel_data[0], symbols[rel_data[1] >> 8].st_name, rel_data[1] & 0xff))
        return rels

class ElfSection:
    def __init__(self, sh_name, sh_type, sh_flags=0, sh_link="", sh_info="", sh_addralign=0, sh_entsize=0, data=""):
        self.sh_name = sh_name
        self.sh_type = sh_type
        self.sh_flags = sh_flags
        self.sh_link = sh_link
        self.sh_info = sh_info
        self.sh_addralign = sh_addralign
        self.sh_entsize = sh_entsize

        self.data = data

    def read_u32(self, offset):
        return struct.unpack_from("<I", self.data, offset)[0]

    def write_u32(self, offset, value):
        # TODO Find a less stupid way
        self.data[offset + 0] = (value) & 0xFF
        self.data[offset + 1] = (value >> 8) & 0xFF
        self.data[offset + 2] = (value >> 16) & 0xFF
        self.data[offset + 3] = (value >> 24) & 0xFF

class ElfSymbol:
    def __init__(self, name, value, size, info, others, section):
        self.st_name = name
        self.st_value = value
        self.st_size = size
        self.st_info = info
        self.st_others = others
        self.st_section = section

    def __repr__(self):
        return "S 0x{:x} {} {}".format(self.st_value, self.st_section if self.st_section != "" else "UND", self.st_name)

    def __eq__(self, other):
        return self.st_name == other.st_name and self.st_value == other.st_value and self.st_size == other.st_size and self.st_info == other.st_info and self.st_others == other.st_others and self.st_section == other.st_section

    def __lt__(self, other):
        if self.st_section == other.st_section:
            if self.st_value == other.st_value:
                return self.st_name < other.st_name
            return self.st_value < other.st_value
        return self.st_section < other.st_section

    def __hash__(self):
        return hash((self.st_name, self.st_value, self.st_size, self.st_info, self.st_others, self.st_section))

class ElfRel:
    def __init__(self, r_address, r_symbol, r_type):
        self.r_address = r_address
        self.r_symbol = r_symbol
        self.r_type = r_type

    def __repr__(self):
        return "R 0x{:x} {} {}".format(self.r_address, self.r_symbol, self.r_type)

    def __eq__(self, other):
        return self.r_address == other.r_address and self.r_symbol == other.r_symbol and self.r_type == other.r_type

    def __ne__(self, other):
        return not (self == other)

    def __hash__(self):
        return hash((self.r_address, self.r_symbol, self.r_type))
