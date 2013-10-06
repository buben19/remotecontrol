import unittest
from remotecontrol.event import Event
from remotecontrol import defines
from ctypes import sizeof

class TestEvent(unittest.TestCase):
    def setUp(self):
        self.event = Event(1, 2, 3)

    def tearDown(self):
        self.event = None

    def test_type(self):
        self.assertEquals(self.event.type, 1)

    def test_code(self):
        self.assertEquals(self.event.code, 2)

    def test_value(self):
        self.assertEquals(self.event.value, 3)

    def test_size(self):
        self.assertEquals(self.event.size(), sizeof(defines.Event))

    def test_toBytes(self):
        self.assertEquals(self.event.toBytes(), '\x01\x02\x00\x03')
