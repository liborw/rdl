
from .base import Bits, Field
from .register import Register
from .device import Device


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

