
from rdl import Bits


class Device(object):

    def __init__(self, name):
        self.name = name
        self.bits = dict()

    def add(self, bits:Bits):
        self.bits[bits.name] = bits
        setattr(self, bits.name, bits)

    def add_all(self, lst:list[Bits]):
        for b in lst:
            self.add(b)

    def get_all(self, cls=Bits) -> list[Bits]:
        return [b for b in self.bits.values() if isinstance(b, cls)]





