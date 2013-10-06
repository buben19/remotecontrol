from zope.interface import Interface


class IRCTransceiver(Interface):

    def sendEvent(event):
        """
        send event to the controlled device
        """
