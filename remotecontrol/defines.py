from ctypes import *

# define types of events
EV_MOVE             = 0x01

# move codes
MOVE_FORWARD        = 0x01
MOVE_BACKWARD       = 0x02
MOVE_STOP           = 0x03
MOVE_LEFT           = 0x04
MOVE_RIGHT          = 0x05
MOVE_STRAIGHT       = 0x06

class Event(Structure):
    _fields_ = [
        ('type',        c_ubyte),
        ('code',        c_ubyte),
        ('value',       c_short)]
