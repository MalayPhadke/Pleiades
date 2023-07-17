class RcData(object):
    def get():
        pass

    def get(Channel):
        pass

class RcCommand(object):
    def get():
        pass

    def get(Channel):
        pass

    def set(rcValueArray):
        pass

    def set(Channel, rcValueArray):
        pass

class FlightMode(object):
    def check(mode):
        pass

    def set(status):
        pass

class Command(object):
    def takeOff(height):
        pass

    def land(landSpeed):
        pass

    def flip(direction):
        pass

    def arm():
        pass

    def disarm():
        pass

def setUserLoopFrequency(frequency):
    pass

class App(object):
    def getAppHeading():
        pass
    
    def isArmSwitchOn():
        pass
