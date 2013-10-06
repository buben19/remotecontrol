from twisted.internet.protocol import Protocol
from zope.interface import implements
from interfaces import IRCTransceiver
from twisted.internet import reactor
from twisted.internet.serialport import SerialPort

class RCSerialTransceiver(object):
    """
    transceive events throught serial line
    """

    implements(IRCTransceiver);

    serial = None
    serialDevice = None

    def __init__(self, serialFile, serialConfig):
        self.serial = Protocol()
        self.serialDevice = SerialPort(
            self.serial,
            serialFile,
            reactor,
            serialConfig.baudrate)

    def sendEvent(self, event):
        self.serial.transport.write(event.toBytes())

class SerialConfig(object):
    """
    configuration for serial console
    """

    baudrate = None

    def __init__(self, baudrate):
        self.baudrate = baudrate
