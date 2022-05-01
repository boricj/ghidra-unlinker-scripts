class MockAddress:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return hex(self.value)

    def __eq__(self, address):
        return self.value == address.value

    def __ne__(self, other):
        return not (self == other)

    def __hash__(self):
        return hash(self.value)

    def add(self, displacement):
        return MockAddress(self.value + displacement)

    def subtract(self, address):
        return self.value - address.value

    def getOffset(self):
        return self.value

    def getNewAddress(self, offset):
        return MockAddress(offset)

class MockAddressRange:
    def __init__(self, addr, length):
        self.addr = addr
        self.length = length

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "[{} {}]".format(self.getMinAddress(), self.getMaxAddress())

    def contains(self, addr):
        return addr.subtract(self.addr) >= 0 and addr.subtract(self.addr) < self.length

    def getLength(self):
        return self.length

    def getMinAddress(self):
        return self.addr

    def getMaxAddress(self):
        return self.addr.add(self.length - 1)

class MockAddressSet:
    def __init__(self, min_addr, max_addr):
        self.ranges = (MockAddressRange(min_addr, max_addr.subtract(min_addr) + 1),)

    def contains(self, addr):
        for address_range in self.ranges:
            if address_range.contains(addr):
                return True
        return False

    def getFirstRange(self):
        return self.ranges[0]

    def getMinAddress(self):
        min_addr = self.ranges[0].getMinAddress()
        for address_range in self.ranges:
            if min_addr.getOffset() > address_range.getMinAddress().getOffset():
                min_addr = address_range.getMinAddress()
        return min_addr

    def getMaxAddress(self):
        max_addr = self.ranges[0].getMaxAddress()
        for address_range in self.ranges:
            if max_addr.getOffset() < address_range.getMaxAddress().getOffset():
                max_addr = address_range.getMaxAddress()
        return max_addr

    def getNumAddresses(self):
        return self.getFirstRange().getLength()

class MockAddressFactory:
    def getAddress(self, value):
        return MockAddress(int(value, 16))

    def getAddressSet(self, min_addr, max_addr):
        return MockAddressSet(min_addr, max_addr)

class MockData():
    def __init__(self, min_addr, max_addr):
        self.min_addr = min_addr
        self.max_addr = max_addr

    def getMinAddress(self):
        return self.min_addr

    def getMaxAddress(self):
        return self.max_addr

    def getLength(self):
        return self.max_addr.subtract(self.min_addr) + 1

class MockListing():
    def __init__(self, data):
        self.data = data
        self.data_at = dict()
        for datum in data:
            self.data_at[datum.getMinAddress()] = datum

    def getDataAt(self, address):
        return self.data_at.get(address, None)

class MockFunction:
    def __init__(self, name, body):
        self.name = name
        self.body = body

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.name

    def getBody(self):
        return self.body

    def getEntryPoint(self):
        return self.body.getMinAddress()

    def getName(self):
        return self.name

class MockFunctionManager:
    def __init__(self, functions):
        self.functions = functions

    def getFunctions(self, asv, forward):
        if forward == False:
            raise Exception("forward != True")
        return (f for f in self.functions if asv.contains(f.getEntryPoint()))

    def getFunctionAt(self, address):
        for function in self.functions:
            if function.getBody().getMinAddress() == address:
                return function
        return None

    def getFunctionContaining(self, address):
        for function in self.functions:
            if function.getBody().contains(address):
                return function
        return None

class MockMemory:
    def __init__(self, memory_blocks):
        self.memory_blocks = memory_blocks

    def getBytes(self, address, buffer):
        for memory_block in self.memory_blocks:
            if memory_block.contains(address):
                memory_block.getBytes(address, buffer)
                return

class MockMemoryBlock:
    def __init__(self, name, address_range, data):
        self.name = name
        self.address_range = address_range
        self.data = data

    def contains(self, address):
        return self.address_range.contains(address)

    def getName(self):
        self.name = name

    def getStart(self):
        return self.address_range.getMinAddress()

    def getEnd(self):
        return self.address_range.getMaxAddress()

    def getBytes(self, address, buffer):
        memory_offset = address.subtract(self.getStart())
        for i in range(0, len(buffer)):
            buffer[i] = self.data[memory_offset + i]

class MockReference:
    def __init__(self, from_address, to_address, reftype, operand_index, isPrimary):
        self.from_address = from_address
        self.to_address = to_address
        self.reftype = reftype
        self.operand_index = operand_index
        self._isPrimary = isPrimary

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "From: {} To: {}".format(self.from_address, self.to_address)

    def getFromAddress(self):
        return self.from_address

    def getToAddress(self):
        return self.to_address

    def getOperandIndex(self):
        return self.operand_index

    def getReferenceType(self):
        return self.reftype

    def isPrimary(self):
        return self._isPrimary

class MockRefType:
    def __init__(self, name, isCall, isComputed, isConditional, isData, isFallthrough, isFlow, isIndirect, isJump, isOverride, isRead, isTerminal, isUnConditional, isWrite):
        self.name = name
        self._isCall = isCall
        self._isComputed = isComputed
        self._isConditional = isConditional
        self._isData = isData
        self._isFallthrough = isFallthrough
        self._isFlow = isFlow
        self._isIndirect = isIndirect
        self._isJump = isJump
        self._isOverride = isOverride
        self._isRead = isRead
        self._isTerminal = isTerminal
        self._isUnConditional = isUnConditional
        self._isWrite = isWrite

    def getName(self):
        return self.name

    def isCall(self):
        return self._isCall

    def isComputed(self):
        return self._isComputed

    def isConditional(self):
        return self._isConditional

    def isData(self):
        return self._isData

    def isFallthrough(self):
        return self._isFallthrough

    def isFlow(self):
        return self._isFlow

    def isIndirect(self):
        return self._isIndirect

    def isJump(self):
        return self._isJump

    def isOverride(self):
        return self._isOverride

    def isRead(self):
        return self._isRead

    def isTerminal(self):
        return self._isTerminal

    def isUnConditional(self):
        return self._isUnConditional

    def isWrite(self):
        return self._isWrite

class MockSymbol:
    def __init__(self, name, address, isGlobal, references):
        self.name = name
        self.address = address
        self.references = references
        self._isGlobal = isGlobal

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.name

    def getAddress(self):
        return self.address

    def getName(self):
        return self.name

    def getReferences(self):
        return self.references

    def isGlobal(self):
        return self._isGlobal

class MockSymbolTable:
    def __init__(self, symbols):
        self.symbols = symbols

    def getAllSymbols(self, includeDynamicSymbols):
        if includeDynamicSymbols == False:
            raise Exception("includeDynamicSymbols != True")
        return self.symbols

    def getSymbols(self, name):
        return [symbol for symbol in self.symbols if symbol.getName() == name].__iter__()

class MockProgram:
    def __init__(self, data, functions, memory_blocks, symbols):
        self.address_factory = MockAddressFactory()
        self.function_manager = MockFunctionManager(functions)
        self.listing = MockListing(data)
        self.memory = MockMemory(memory_blocks)
        self.symbol_table = MockSymbolTable(symbols)

    def getAddressFactory(self):
        return self.address_factory

    def getFunctionManager(self):
        return self.function_manager

    def getListing(self):
        return self.listing

    def getMemory(self):
        return self.memory

    def getSymbolTable(self):
        return self.symbol_table