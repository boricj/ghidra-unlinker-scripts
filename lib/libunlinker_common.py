# Ghidra reference type names
COMPUTED_CALL="COMPUTED_CALL"
DATA="DATA"
PARAM="PARAM"
READ="READ"
UNCONDITIONAL_CALL="UNCONDITIONAL_CALL"
UNCONDITIONAL_JUMP="UNCONDITIONAL_JUMP"
WRITE="WRITE"

def test_condition(expected, value, context):
    if isinstance(expected, tuple) or isinstance(expected, list) or isinstance(expected, set):
        return value in expected
    elif isinstance(expected, int) or isinstance(expected, long) or isinstance(expected, str):
        return expected == value
    elif callable(expected):
        return expected(value, context) == True
    elif expected is None:
        return True
    raise Exception("Unknown condition type " + str(type(expected)))

class PatchRequest:
    def __init__(self, offset, value, length):
        self.offset = offset
        self.value = value
        self.length = length

    def __eq__(self, other):
        return self.offset == other.offset and self.value == other.value and self.length == other.length

    def __hash__(self):
        return hash((self.offset, self.value, self.length))
