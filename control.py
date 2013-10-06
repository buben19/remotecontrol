#!/usr/bin/env python
from remotecontrol.input import GamepadProtocol
from remotecontrol.protocol import RCInputProtocol
from twistedinput.device import EventDevice
from twisted.internet import reactor
from remotecontrol.transceiver import RCSerialTransceiver, SerialConfig
import sys

class MyTransceiver(object):
    def sendEvent(self, event):
        print repr(event.toBytes())

def main():

    serialConfig = SerialConfig(19200)

    EventDevice(
        GamepadProtocol(
            RCInputProtocol(
                RCSerialTransceiver(
                    sys.argv[2],
                    serialConfig))),
        sys.argv[1]).startReading()
    reactor.run()

if __name__ == '__main__':
    main()
