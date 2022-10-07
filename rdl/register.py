
from rdl import Bits, Field

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
                 fields: list[Field] = []):


        self.address = address
        self.asize_b = asize_b
        super(Register, self).__init__(name, dsize_b, value, fields=fields)

    def __repr__(self):
        return '<Register:{0} 0x{1:0{2}x} >'.format(self.name,
                                                    self.value,
                                                    self.size_B*2)
