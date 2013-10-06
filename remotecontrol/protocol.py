from event import Event
import defines



class RCInputProtocol(object):

    transceiver = None

    def __init__(self, transceiver):
        self.transceiver = transceiver

    def moveForward(self, value):
        self.transceiver.sendEvent(
            Event(
                defines.EV_MOVE,
                defines.MOVE_FORWARD,
                value))

    def moveBackward(self, value):
        self.transceiver.sendEvent(
            Event(
                defines.EV_MOVE,
                defines.MOVE_BACKWARD,
                value))

    def stopMoving(self):
        self.transceiver.sendEvent(
            Event(
                defines.EV_MOVE,
                defines.MOVE_STOP,
                0))

    def turnLeft(self, value):
        self.transceiver.sendEvent(
            Event(
                defines.EV_MOVE,
                defines.MOVE_LEFT,
                value))

    def turnRight(self, value):
        self.transceiver.sendEvent(
            Event(
                defines.EV_MOVE,
                defines.MOVE_RIGHT,
                value))

    def goStraight(self):
        self.transceiver.sendEvent(
            Event(
                defines.EV_MOVE,
                defines.MOVE_STRAIGHT,
                0))
