from rdl import Bits

class Field(object):
    """Field is a named subset of bits."""

    def __init__(self,
                 name: str,
                 msb: int,
                 lsb: int|None = None,
                 value: int|None = None,
                 fn=lambda x: x,
                 unit: str = '',
                 description: str = '',
                 fmt: str|None = None):
        """
        """

        self.name = name
        self.msb = msb
        self.lsb = lsb
        self._init_value = value
        self._disp_fn = fn
        self._parrent : Bits|None = None
        self.unit = unit
        self.description = description

        if self.lsb is None:
            self.lsb = self.msb
            self.size = 1
        else:
            self.size = self.msb - self.lsb + 1

        if not fmt and self.size == 1:
            self.fmt = 'b'
        else:
            self.fmt = fmt

    def get_value(self):
        if self._parrent:
            return self._parrent.get_bits(self.msb, self.lsb)
        # TODO: else

    def set_value(self, value):
        if self._parrent:
            self._parrent.set_bits(self.msb, self.lsb, value)
        # TODO: else

    value = property(get_value, set_value)
