# Export the current program as a test case for the unlinker
#@author Jean-Baptiste Boric
#@category Unlinker
#@keybinding 
#@menupath 
#@toolbar 

import jarray

output_file = askFile("Export unlinker test case", "Save").getPath()

program_name = currentProgram.getName()
data = currentProgram.getListing().getDefinedData(True)
functions = currentProgram.getFunctionManager().getFunctions(True)
memory_blocks = currentProgram.getMemory().getBlocks()
symbols = currentProgram.getSymbolTable().getAllSymbols(True)

def toaddr(addr):
    return hex(int(addr.getOffset()))

with open(output_file, "w") as fp:
    fp.write("# Generated from {}\n".format(program_name))
    fp.write("from MockProgram import *\n")

    fp.write("# Data\ndata = (\n")
    for datum in data:
        fp.write("  MockData(min_addr=MockAddress({}), max_addr=MockAddress({})),\n".format(toaddr(datum.getMinAddress()), toaddr(datum.getMaxAddress())))
    fp.write(")\n")

    fp.write("# Functions\nfunctions = (\n")
    for function in functions:
        fp.write("  MockFunction(name='{}', body=MockAddressSet(MockAddress({}), MockAddress({}))),\n".format(function.getName(), toaddr(function.getBody().getMinAddress()), toaddr(function.getBody().getMaxAddress())))
    fp.write(")\n")

    fp.write("# Memory blocks\nmemory_blocks = (\n")
    for memory_block in memory_blocks:
        if memory_block.isLoaded():
            if memory_block.isInitialized():
                fp.write("  MockMemoryBlock(name='{}', address_range=MockAddressSet(MockAddress({}), MockAddress({})).getFirstRange(), data=(".format(memory_block.getName(), toaddr(memory_block.getStart()), toaddr(memory_block.getEnd())))
                data = jarray.zeros(memory_block.getSize(), "b")
                memory_block.getBytes(memory_block.getStart(), data)
                fp.write(','.join((str(i) for i in data)))
                fp.write(")),\n")
            else:
                fp.write("  MockMemoryBlock(name='{}', address_range=MockAddressSet(MockAddress({}), MockAddress({})).getFirstRange(), data=None),\n".format(memory_block.getName(), toaddr(memory_block.getStart()), toaddr(memory_block.getEnd())))
    fp.write(")\n")

    fp.write("# Symbols\nsymbols = (\n")
    for symbol in symbols:
        fp.write("  MockSymbol(name='{}', address=MockAddress({}), isGlobal={}, references=(\n".format(symbol.getName(), toaddr(symbol.getAddress()), str(symbol.isGlobal())))
        for reference in symbol.getReferences():
            fp.write("    MockReference(from_address=MockAddress({}), to_address=MockAddress({}), isPrimary={}, operand_index={},\n".format(toaddr(reference.getFromAddress()), toaddr(reference.getToAddress()), str(reference.isPrimary()), reference.getOperandIndex()))
            reftype = reference.getReferenceType()
            fp.write("      reftype=MockRefType('{}', isCall={}, isComputed={}, isConditional={}, isData={}, isFallthrough={}, isFlow={}, isIndirect={}, isJump={}, isOverride={}, isRead={}, isTerminal={}, isUnConditional={}, isWrite={})),\n".format(
                reftype.getName(),
                str(reftype.isCall()),
                str(reftype.isComputed()),
                str(reftype.isConditional()),
                str(reftype.isData()),
                str(reftype.isFallthrough()),
                str(reftype.isFlow()),
                str(reftype.isIndirect()),
                str(reftype.isJump()),
                str(reftype.isOverride()),
                str(reftype.isRead()),
                str(reftype.isTerminal()),
                str(reftype.isUnConditional()),
                str(reftype.isWrite())
            ))
        fp.write("  )),\n")
    fp.write(")\n")

    fp.write("currentProgram = MockProgram(data=data, functions=functions, memory_blocks=memory_blocks, symbols=symbols)\n")
