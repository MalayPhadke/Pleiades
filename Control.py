class DesiredAngle(object):
    def get(self, angle):
        return angle
    
    def set(self, angle, value):
        pass

class DesiredPosition(object):
    def get(self, AXIS):
        pass

    def set(self, AXIS, position):
        pass

    def setRelative(self, AXIS, position):
        pass

class DesiredVelocity(object):
    def get(self, AXIS):
        pass

    def set(self, AXIS, velocity):
        pass

class PIDProfile(object):
    def get(self, PROFILE, *profile):
        pass

    def set(self, PROFILE, *profile):
        pass

    def setDefault(self):
        pass

class Failsafe(object):
    def enable(self, Failsafe):
        pass

    def disable(self, Failsafe):
        pass