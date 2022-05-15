# Generated from testFlow.elf
from MockProgram import *
# Data
data = (
  MockData(min_addr=MockAddress(0x400000), max_addr=MockAddress(0x400033)),
  MockData(min_addr=MockAddress(0x400034), max_addr=MockAddress(0x400093)),
  MockData(min_addr=MockAddress(0x4000b0), max_addr=MockAddress(0x4000c7)),
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
  MockData(min_addr=MockAddress(0x20), max_addr=MockAddress(0x23)),
  MockData(min_addr=MockAddress(0x24), max_addr=MockAddress(0x27)),
  MockData(min_addr=MockAddress(0x28), max_addr=MockAddress(0x28)),
  MockData(min_addr=MockAddress(0x29), max_addr=MockAddress(0x29)),
  MockData(min_addr=MockAddress(0x2a), max_addr=MockAddress(0x2a)),
  MockData(min_addr=MockAddress(0x2b), max_addr=MockAddress(0x2b)),
  MockData(min_addr=MockAddress(0x2c), max_addr=MockAddress(0x2c)),
  MockData(min_addr=MockAddress(0x2d), max_addr=MockAddress(0x2f)),
  MockData(min_addr=MockAddress(0x30), max_addr=MockAddress(0x33)),
  MockData(min_addr=MockAddress(0x34), max_addr=MockAddress(0x37)),
  MockData(min_addr=MockAddress(0x38), max_addr=MockAddress(0x3b)),
  MockData(min_addr=MockAddress(0x3c), max_addr=MockAddress(0x3f)),
  MockData(min_addr=MockAddress(0x40), max_addr=MockAddress(0x43)),
  MockData(min_addr=MockAddress(0x44), max_addr=MockAddress(0x47)),
  MockData(min_addr=MockAddress(0x48), max_addr=MockAddress(0x4b)),
  MockData(min_addr=MockAddress(0x4c), max_addr=MockAddress(0x4f)),
  MockData(min_addr=MockAddress(0x50), max_addr=MockAddress(0x53)),
  MockData(min_addr=MockAddress(0x54), max_addr=MockAddress(0x57)),
  MockData(min_addr=MockAddress(0x58), max_addr=MockAddress(0x5b)),
  MockData(min_addr=MockAddress(0x5c), max_addr=MockAddress(0x5f)),
  MockData(min_addr=MockAddress(0x60), max_addr=MockAddress(0x63)),
  MockData(min_addr=MockAddress(0x64), max_addr=MockAddress(0x67)),
  MockData(min_addr=MockAddress(0x68), max_addr=MockAddress(0x6b)),
  MockData(min_addr=MockAddress(0x6c), max_addr=MockAddress(0x6f)),
  MockData(min_addr=MockAddress(0x70), max_addr=MockAddress(0x73)),
  MockData(min_addr=MockAddress(0x74), max_addr=MockAddress(0x77)),
  MockData(min_addr=MockAddress(0x78), max_addr=MockAddress(0x7b)),
  MockData(min_addr=MockAddress(0x7c), max_addr=MockAddress(0x7f)),
  MockData(min_addr=MockAddress(0x80), max_addr=MockAddress(0x83)),
  MockData(min_addr=MockAddress(0x84), max_addr=MockAddress(0x87)),
  MockData(min_addr=MockAddress(0x88), max_addr=MockAddress(0x8b)),
  MockData(min_addr=MockAddress(0x8c), max_addr=MockAddress(0x8f)),
  MockData(min_addr=MockAddress(0x0), max_addr=MockAddress(0x7d)),
  MockData(min_addr=MockAddress(0x1), max_addr=MockAddress(0x8)),
  MockData(min_addr=MockAddress(0x9), max_addr=MockAddress(0x10)),
  MockData(min_addr=MockAddress(0x11), max_addr=MockAddress(0x1a)),
  MockData(min_addr=MockAddress(0x1b), max_addr=MockAddress(0x29)),
  MockData(min_addr=MockAddress(0x2a), max_addr=MockAddress(0x32)),
  MockData(min_addr=MockAddress(0x33), max_addr=MockAddress(0x38)),
  MockData(min_addr=MockAddress(0x39), max_addr=MockAddress(0x41)),
  MockData(min_addr=MockAddress(0x42), max_addr=MockAddress(0x46)),
  MockData(min_addr=MockAddress(0x47), max_addr=MockAddress(0x55)),
  MockData(min_addr=MockAddress(0x56), max_addr=MockAddress(0x61)),
  MockData(min_addr=MockAddress(0x62), max_addr=MockAddress(0x6f)),
  MockData(min_addr=MockAddress(0x70), max_addr=MockAddress(0x7b)),
  MockData(min_addr=MockAddress(0x7c), max_addr=MockAddress(0x88)),
  MockData(min_addr=MockAddress(0x89), max_addr=MockAddress(0x93)),
  MockData(min_addr=MockAddress(0x94), max_addr=MockAddress(0xa3)),
  MockData(min_addr=MockAddress(0xa4), max_addr=MockAddress(0xb1)),
  MockData(min_addr=MockAddress(0x1), max_addr=MockAddress(0x14)),
  MockData(min_addr=MockAddress(0x15), max_addr=MockAddress(0x29)),
  MockData(min_addr=MockAddress(0x2a), max_addr=MockAddress(0x2d)),
  MockData(min_addr=MockAddress(0x2e), max_addr=MockAddress(0x34)),
  MockData(min_addr=MockAddress(0x35), max_addr=MockAddress(0x49)),
  MockData(min_addr=MockAddress(0x4a), max_addr=MockAddress(0x5c)),
  MockData(min_addr=MockAddress(0x5d), max_addr=MockAddress(0x64)),
  MockData(min_addr=MockAddress(0x65), max_addr=MockAddress(0x6b)),
  MockData(min_addr=MockAddress(0x6c), max_addr=MockAddress(0x87)),
  MockData(min_addr=MockAddress(0x88), max_addr=MockAddress(0x93)),
  MockData(min_addr=MockAddress(0x94), max_addr=MockAddress(0xa6)),
  MockData(min_addr=MockAddress(0xa7), max_addr=MockAddress(0xad)),
  MockData(min_addr=MockAddress(0xae), max_addr=MockAddress(0xb2)),
  MockData(min_addr=MockAddress(0xb3), max_addr=MockAddress(0xce)),
  MockData(min_addr=MockAddress(0xcf), max_addr=MockAddress(0xe7)),
  MockData(min_addr=MockAddress(0xe8), max_addr=MockAddress(0xed)),
  MockData(min_addr=MockAddress(0x0), max_addr=MockAddress(0x1ef)),
  MockData(min_addr=MockAddress(0x0), max_addr=MockAddress(0x2a7)),
)
# Functions
functions = (
  MockFunction(name='__start', body=MockAddressSet(MockAddress(0x4000d0), MockAddress(0x4000d7))),
  MockFunction(name='testcase_flow_target', body=MockAddressSet(MockAddress(0x4000e0), MockAddress(0x4000e7))),
  MockFunction(name='testcase_flow_call', body=MockAddressSet(MockAddress(0x4000e8), MockAddress(0x4000f7))),
  MockFunction(name='testcase_flow_call_indirect', body=MockAddressSet(MockAddress(0x4000f8), MockAddress(0x40010f))),
  MockFunction(name='testcase_flow_jump', body=MockAddressSet(MockAddress(0x400110), MockAddress(0x400117))),
  MockFunction(name='testcase_flow_jump_local', body=MockAddressSet(MockAddress(0x400118), MockAddress(0x400133))),
  MockFunction(name='testcase_flow_jump_indirect', body=MockAddressSet(MockAddress(0x400134), MockAddress(0x400143))),
)
# Memory blocks
memory_blocks = (
  MockMemoryBlock(name='segment_2.1', address_range=MockAddressSet(MockAddress(0x400000), MockAddress(0x400097)).getFirstRange(), data=(127,69,76,70,1,1,1,0,0,0,0,0,0,0,0,0,2,0,8,0,1,0,0,0,-48,0,64,0,52,0,0,0,76,11,0,0,1,16,0,0,52,0,32,0,3,0,40,0,17,0,16,0,3,0,0,112,-104,0,0,0,-104,0,64,0,-104,0,64,0,24,0,0,0,24,0,0,0,4,0,0,0,8,0,0,0,0,0,0,112,-80,0,0,0,-80,0,64,0,-80,0,64,0,24,0,0,0,24,0,0,0,4,0,0,0,4,0,0,0,1,0,0,0,0,0,0,0,0,0,64,0,0,0,64,0,80,1,0,0,80,1,0,0,5,0,0,0,0,0,1,0,0,0,0,0)),
  MockMemoryBlock(name='.MIPS.abiflags', address_range=MockAddressSet(MockAddress(0x400098), MockAddress(0x4000af)).getFirstRange(), data=(0,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)),
  MockMemoryBlock(name='.reginfo', address_range=MockAddressSet(MockAddress(0x4000b0), MockAddress(0x4000c7)).getFirstRange(), data=(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,64,-127,65,0)),
  MockMemoryBlock(name='.text', address_range=MockAddressSet(MockAddress(0x4000d0), MockAddress(0x40014f)).getFirstRange(), data=(-1,-1,0,16,0,0,0,0,0,0,0,0,0,0,0,0,8,0,-32,3,0,0,0,0,56,0,16,12,0,0,0,0,8,0,-32,3,0,0,0,0,64,0,2,60,-32,0,66,36,9,-8,64,0,0,0,0,0,8,0,-32,3,0,0,0,0,56,0,16,8,0,0,0,0,3,0,-124,16,0,0,0,0,75,0,16,8,33,32,-124,0,33,48,-58,0,8,0,-32,3,33,40,-91,0,64,0,2,60,-32,0,66,36,8,0,64,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)),
)
# Symbols
symbols = (
  MockSymbol(name='Elf32_Phdr_ARRAY_00400034', address=MockAddress(0x400034), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0x40001c), to_address=MockAddress(0x400034), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='DAT_00400098', address=MockAddress(0x400098), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0x40003c), to_address=MockAddress(0x400098), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
    MockReference(from_address=MockAddress(0x34), to_address=MockAddress(0x400098), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='Elf32_RegInfo_MIPS_004000b0', address=MockAddress(0x4000b0), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0x40005c), to_address=MockAddress(0x4000b0), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
    MockReference(from_address=MockAddress(0x5c), to_address=MockAddress(0x4000b0), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='__start', address=MockAddress(0x4000d0), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0x84), to_address=MockAddress(0x4000d0), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
    MockReference(from_address=MockAddress(0x0), to_address=MockAddress(0x4000d0), isPrimary=False, operand_index=-1,
      reftype=MockRefType('EXTERNAL', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
    MockReference(from_address=MockAddress(0x400018), to_address=MockAddress(0x4000d0), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
    MockReference(from_address=MockAddress(0x18), to_address=MockAddress(0x4000d0), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
    MockReference(from_address=MockAddress(0x4000d0), to_address=MockAddress(0x4000d0), isPrimary=True, operand_index=0,
      reftype=MockRefType('UNCONDITIONAL_JUMP', isCall=False, isComputed=False, isConditional=False, isData=False, isFallthrough=False, isFlow=True, isIndirect=False, isJump=True, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='testcase_flow_target', address=MockAddress(0x4000e0), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0x400110), to_address=MockAddress(0x4000e0), isPrimary=False, operand_index=-2,
      reftype=MockRefType('THUNK', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
    MockReference(from_address=MockAddress(0x400134), to_address=MockAddress(0x4000e0), isPrimary=False, operand_index=-2,
      reftype=MockRefType('THUNK', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
    MockReference(from_address=MockAddress(0x0), to_address=MockAddress(0x4000e0), isPrimary=False, operand_index=-1,
      reftype=MockRefType('EXTERNAL', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
    MockReference(from_address=MockAddress(0x38), to_address=MockAddress(0x4000e0), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
    MockReference(from_address=MockAddress(0x4000e8), to_address=MockAddress(0x4000e0), isPrimary=True, operand_index=0,
      reftype=MockRefType('UNCONDITIONAL_CALL', isCall=True, isComputed=False, isConditional=False, isData=False, isFallthrough=False, isFlow=True, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
    MockReference(from_address=MockAddress(0x400110), to_address=MockAddress(0x4000e0), isPrimary=True, operand_index=0,
      reftype=MockRefType('UNCONDITIONAL_JUMP', isCall=False, isComputed=False, isConditional=False, isData=False, isFallthrough=False, isFlow=True, isIndirect=False, isJump=True, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
    MockReference(from_address=MockAddress(0x40013c), to_address=MockAddress(0x4000e0), isPrimary=True, operand_index=0,
      reftype=MockRefType('COMPUTED_CALL', isCall=True, isComputed=True, isConditional=False, isData=False, isFallthrough=False, isFlow=True, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
    MockReference(from_address=MockAddress(0x400100), to_address=MockAddress(0x4000e0), isPrimary=True, operand_index=0,
      reftype=MockRefType('COMPUTED_CALL', isCall=True, isComputed=True, isConditional=False, isData=False, isFallthrough=False, isFlow=True, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='testcase_flow_call', address=MockAddress(0x4000e8), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0x0), to_address=MockAddress(0x4000e8), isPrimary=False, operand_index=-1,
      reftype=MockRefType('EXTERNAL', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
    MockReference(from_address=MockAddress(0x48), to_address=MockAddress(0x4000e8), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='testcase_flow_call_indirect', address=MockAddress(0x4000f8), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0x0), to_address=MockAddress(0x4000f8), isPrimary=False, operand_index=-1,
      reftype=MockRefType('EXTERNAL', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
    MockReference(from_address=MockAddress(0x58), to_address=MockAddress(0x4000f8), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='testcase_flow_jump', address=MockAddress(0x400110), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0x0), to_address=MockAddress(0x400110), isPrimary=False, operand_index=-1,
      reftype=MockRefType('EXTERNAL', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
    MockReference(from_address=MockAddress(0x68), to_address=MockAddress(0x400110), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='testcase_flow_jump_local', address=MockAddress(0x400118), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0x0), to_address=MockAddress(0x400118), isPrimary=False, operand_index=-1,
      reftype=MockRefType('EXTERNAL', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
    MockReference(from_address=MockAddress(0x78), to_address=MockAddress(0x400118), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='LAB_00400128', address=MockAddress(0x400128), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0x400118), to_address=MockAddress(0x400128), isPrimary=True, operand_index=2,
      reftype=MockRefType('CONDITIONAL_JUMP', isCall=False, isComputed=False, isConditional=True, isData=False, isFallthrough=False, isFlow=True, isIndirect=False, isJump=True, isOverride=False, isRead=False, isTerminal=False, isUnConditional=False, isWrite=False)),
  )),
  MockSymbol(name='LAB_0040012c', address=MockAddress(0x40012c), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0x400120), to_address=MockAddress(0x40012c), isPrimary=True, operand_index=0,
      reftype=MockRefType('UNCONDITIONAL_JUMP', isCall=False, isComputed=False, isConditional=False, isData=False, isFallthrough=False, isFlow=True, isIndirect=False, isJump=True, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='testcase_flow_jump_indirect', address=MockAddress(0x400134), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0x0), to_address=MockAddress(0x400134), isPrimary=False, operand_index=-1,
      reftype=MockRefType('EXTERNAL', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
    MockReference(from_address=MockAddress(0x88), to_address=MockAddress(0x400134), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='_fdata', address=MockAddress(0x410150), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0x0), to_address=MockAddress(0x410150), isPrimary=True, operand_index=-1,
      reftype=MockRefType('EXTERNAL', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='__bss_start', address=MockAddress(0x410150), isGlobal=True, references=(
  )),
  MockSymbol(name='_edata', address=MockAddress(0x410150), isGlobal=True, references=(
  )),
  MockSymbol(name='_end', address=MockAddress(0x410150), isGlobal=True, references=(
  )),
  MockSymbol(name='_fbss', address=MockAddress(0x410150), isGlobal=True, references=(
  )),
  MockSymbol(name='_gp', address=MockAddress(0x418140), isGlobal=True, references=(
  )),
  MockSymbol(name='_mips_gp0_value', address=MockAddress(0x418140), isGlobal=True, references=(
  )),
  MockSymbol(name='s_GCC:_(crosstool-NG_1.24.0)_8.3.0_.comment__00000000', address=MockAddress(0x0), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0xac), to_address=MockAddress(0x0), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='DAT_.debug_abbrev__00000000', address=MockAddress(0x0), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0x14c), to_address=MockAddress(0x0), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='DAT_.debug_aranges__00000000', address=MockAddress(0x0), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0xfc), to_address=MockAddress(0x0), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='cie_.debug_frame::00000000', address=MockAddress(0x0), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0x19c), to_address=MockAddress(0x0), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
    MockReference(from_address=MockAddress(0x14), to_address=MockAddress(0x0), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='fde_.debug_frame::00000010', address=MockAddress(0x10), isGlobal=True, references=(
  )),
  MockSymbol(name='cie_.debug_frame::00000020', address=MockAddress(0x20), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0x34), to_address=MockAddress(0x20), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
    MockReference(from_address=MockAddress(0x44), to_address=MockAddress(0x20), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
    MockReference(from_address=MockAddress(0x54), to_address=MockAddress(0x20), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
    MockReference(from_address=MockAddress(0x64), to_address=MockAddress(0x20), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
    MockReference(from_address=MockAddress(0x74), to_address=MockAddress(0x20), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
    MockReference(from_address=MockAddress(0x84), to_address=MockAddress(0x20), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='fde_.debug_frame::00000030', address=MockAddress(0x30), isGlobal=True, references=(
  )),
  MockSymbol(name='fde_.debug_frame::00000040', address=MockAddress(0x40), isGlobal=True, references=(
  )),
  MockSymbol(name='fde_.debug_frame::00000050', address=MockAddress(0x50), isGlobal=True, references=(
  )),
  MockSymbol(name='fde_.debug_frame::00000060', address=MockAddress(0x60), isGlobal=True, references=(
  )),
  MockSymbol(name='fde_.debug_frame::00000070', address=MockAddress(0x70), isGlobal=True, references=(
  )),
  MockSymbol(name='fde_.debug_frame::00000080', address=MockAddress(0x80), isGlobal=True, references=(
  )),
  MockSymbol(name='DAT_.debug_info__00000000', address=MockAddress(0x0), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0x124), to_address=MockAddress(0x0), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='DAT_.debug_line__00000000', address=MockAddress(0x0), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0x174), to_address=MockAddress(0x0), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='s_GNU_C17_8.3.0_-mel_-mno-abicalls_.debug_str__00000000', address=MockAddress(0x0), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0x1c4), to_address=MockAddress(0x0), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='DAT_.gnu.attributes__00000000', address=MockAddress(0x0), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0x1ec), to_address=MockAddress(0x0), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='DAT_.pdr__00000000', address=MockAddress(0x0), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0xd4), to_address=MockAddress(0x0), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='DAT_.shstrtab__00000000', address=MockAddress(0x0), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0x28c), to_address=MockAddress(0x0), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='DAT_.strtab__00000000', address=MockAddress(0x0), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0x264), to_address=MockAddress(0x0), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='Elf32_Sym_ARRAY_.symtab__00000000', address=MockAddress(0x0), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0x23c), to_address=MockAddress(0x0), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
  MockSymbol(name='Elf32_Shdr_ARRAY__elfSectionHeaders__00000000', address=MockAddress(0x0), isGlobal=True, references=(
    MockReference(from_address=MockAddress(0x400020), to_address=MockAddress(0x0), isPrimary=True, operand_index=0,
      reftype=MockRefType('DATA', isCall=False, isComputed=False, isConditional=False, isData=True, isFallthrough=False, isFlow=False, isIndirect=False, isJump=False, isOverride=False, isRead=False, isTerminal=False, isUnConditional=True, isWrite=False)),
  )),
)
currentProgram = MockProgram(data=data, functions=functions, memory_blocks=memory_blocks, symbols=symbols)