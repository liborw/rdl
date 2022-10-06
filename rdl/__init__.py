
from .bits import Bits
from .field import Field

class Register(Bits):
    """
    Representation of a register, it has an address and a value.
    """

    def __init__(self,
                 address: int,
                 value: int,
                 name: str,
                 dsize_b: int = 8,
                 asize_b: int = 8,
                 fields: list = []):
        self.address = address
        self.asize_b = asize_b
        super(Register, self).__init__(name, value, dsize_b, fields=fields)


class Command(Bits):
    """
    Representation of a command, just value, but can have fields.
    """

    def __init__(self, base, name, csize_b, options: list = [], **kvargs):
        super(Command, self).__init__(name, base, csize_b, options, **kvargs)

    def get_value(self, **kvargs):
        for key in self.fields.keys():
            if key in kvargs:
                self.fields[key] = kvargs[key]
        return self.value

