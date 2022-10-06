
from . import Bits
from . import Field


class Device(object):

    def __init__(self, name):
        self.name = name
        self.bits = dict()

    def add(self, bits:Bits):
        self.bits[bits.name] = bits
        setattr(self, bits.name, bits)

    def get_all(self, cls=(Bits,)) -> list[Bits]:
        return [b for b in self.bits if isinstance(b, cls)]





