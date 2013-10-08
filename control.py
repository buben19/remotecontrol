#!/usr/bin/env python
from __future__ import unicode_literals
from remotecontrol.input import GamepadProtocol
from remotecontrol.protocol import RCInputProtocol
from twistedinput.device import EventDevice
from twisted.internet import reactor
from remotecontrol.transceiver import RCSerialTransceiver, SerialConfig
import sys

def printUsage():
    print "usage: %s <input device> <transceiver device>" % (sys.argv[0],)

def main():

    if len(sys.argv) < 3:
        printUsage()
        exit(1)

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
