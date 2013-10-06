import defines
from ctypes import sizeof, BigEndianStructure

class _BigEndianEvent(BigEndianStructure):
    _fields_ = defines.Event._fields_

class Event(object):

    __event = None

    def __init__(self, type, code, value):
        self.__event = defines.Event(type, code, value)

    @property
    def type(self):
        return self.__event.type

    @property
    def code(self):
        return self.__event.code

    @property
    def value(self):
        return self.__event.value

    def size(self):
        """
        get size of event in bytes
        """
        return sizeof(defines.Event)

    def toBytes(self):
        """
        convert event into big-endian byte stream
        """
        s = _BigEndianEvent()
        for field, t in defines.Event._fields_:
            setattr(s, field, getattr(self.__event, field))
        return str(buffer(s))
