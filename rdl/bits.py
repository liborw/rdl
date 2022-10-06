
from .field import Field


class Bits(object):
    """
    A base class for a list of bits with fixed length. It might contain one or
    more fields. Value of a field can be accessed as property of this class.
    """

    def __init__(self, name: str, size_b: int, value: int = 0, fields: list = [], **kvargs):
        """
        :param size_b: numbe of bits is the list
        :param name: Name
        :param value: Initial value
        :param fields: list of fields
        """
        self.name = name
        self.value = value
        self.fields = dict()
        self.size_b = size_b
        self.size_B = size_b // 8 + (1 if size_b % 8 > 0 else 0)

        for field in fields:
            self._add_field(field)

    def _add_field(self, field:Field):
        field._parrent = self
        self.fields[field.name] = field

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

