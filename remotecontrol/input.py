"""
drivers for input devices
"""

from twistedinput.protocol import EventProtocol
from twistedinput.mapping import GamepadEventMapping
from twistedinput.factory import InputEventFactory

_MIDDLE_AXIS_X = 0x80
_MIDDLE_AXIS_Y = 0x80

class GamepadProtocol(EventProtocol):

    radioControl = None

    def __init__(self, radioControl):
        EventProtocol.__init__(
            self, InputEventFactory(),
            GamepadEventMapping())
        self.radioControl = radioControl

    def joystickLeftY(self, event):
        """
        move forward or backward
        """
        if event.value == _MIDDLE_AXIS_Y:
            self.radioControl.stopMoving()
        elif event.value > _MIDDLE_AXIS_Y:

            # move backward
            self.radioControl.moveBackward(event.value - _MIDDLE_AXIS_Y + 1)

        else:
            # move forward
            self.radioControl.moveForward(_MIDDLE_AXIS_Y - event.value)

    def joystickLeftX(self, event):
        """
        turn left or right
        """
        if event.value == _MIDDLE_AXIS_X:
            self.radioControl.goStraight()
        elif event.value < _MIDDLE_AXIS_X:

            # turn left
            self.radioControl.turnLeft(_MIDDLE_AXIS_X - event.value)
        else:

            # turn right
            self.radioControl.turnRight(event.value - _MIDDLE_AXIS_X + 1)
