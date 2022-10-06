
class Bits(object):
    """
    A base class for a list of bits with fixed length. It might contain one or
    more fields. Value of a field can be accessed as property of this class.
    """

    def __init__(self, value: int, size_b: int, fields: list = [], **kvargs):
        """
        :param value: Initial value
        :param size_b: numbe of bits is the list
        :param fields: list of fields
        """
        self.value = value
        self.fields = dict()
        self.size_b = size_b
        self.size_B = size_b // 8 + (1 if size_b % 8 > 0 else 0)

        for field in fields:
            self._add_field(field)

    def _add_field(self, field):
        field._parrent = self
        self.fields[field.label] = field

    def get_bits(self, msb, lsb):
        """
        Get value of subset of bits given by most and least significant bit index.

            :param msb: most significant bit index
            :param lsb: least significant bit index
            :return:
        """
        reg = self.value >> lsb
        val = 0
        for i in range(msb-lsb + 1):
            val += (reg % 2) * 2**i
            reg = reg // 2
        return val

    def set_bits(self, msb, lsb, value):
        """
        Set new value to subset of bits given by most and least significant
        bit index.

            :param msb: most significant bit index
            :param lsb: least significant bit index
            :param value: new value
        """
        val = value << lsb
        tmp = self.value
        reg = 0
        i = 0
        while val > 0 or tmp > 0:
            if i >= lsb and i <= msb:
                reg += (val % 2) * 2**i
            else:
                reg += (tmp % 2) * 2**i

            val = val // 2
            tmp = tmp // 2
            i += 1
        self.value = reg

    def __repr__(self):
        return '<Bits: 0x{0:0{1}x} >'.format(self.value, self.size_B*2)

    def __getattr__(self, name):
        if 'fields' in self.__dict__ and name in self.__dict__['fields']:
            return self.__dict__['fields'][name].value
        else:
            return super(Bits, self).__getattribute__(name)

    def __setattr__(self, name, value):
        if 'fields' in self.__dict__ and name in self.__dict__['fields']:
            self.__dict__['fields'][name].value = value
        else:
            super(Bits, self).__setattr__(name, value)

    def get_sorted_fields(self, reserved=False):
        """Get list of fields sorted by the position in the bits list"""

        if reserved:
            fields = []

            last_start = 0
            reserved_cnt = 0

            for field in sorted(self.fields.values(), key=lambda x: x.lsb):

                space = field.lsb - last_start
                if space > 0:
                    fields.append(Field(f"reserved_{reserved_cnt}", lsb = last_start, msb = field.lsb-1))
                    reserved_cnt += 1
                fields.append(field)
                last_start = field.msb + 1
            return fields
        else:
            return sorted(self.fields.values(), key=lambda x: x.lsb)


class Field(object):
    """Field is a named subset of bits."""

    def __init__(self,
                 label: str,
                 msb: int,
                 lsb: int|None = None,
                 value: int|None = None,
                 fn=lambda x: x,
                 unit: str = '',
                 description: str = '',
                 fmt: str|None = None):

        self.label = label
        self.msb = msb
        self.lsb = lsb
        self._init_value = value
        self._disp_fn = fn
        self._parrent = None
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
        self.name = name
        self.asize_b = asize_b
        super(Register, self).__init__(value, dsize_b, fields=fields)


class Command(Bits):
    """
    Representation of a command, just value, but can have fields.
    """

    def __init__(self, base, name, csize_b, options: list = [], **kvargs):
        self.name = name
        super(Command, self).__init__(base, csize_b, options, **kvargs)

    def get_value(self, **kvargs):
        for key in self.fields.keys():
            if key in kvargs:
                self.fields[key] = kvargs[key]
        return self.value

