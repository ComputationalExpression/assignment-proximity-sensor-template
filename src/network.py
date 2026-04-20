STA_IF = None

class WLAN:

    def __init__(self, state):
        pass

    def active(self, state):
        self.state = state

    def connect(self, ssid, password):
        pass

    def isconnected(self) -> bool:
        return True