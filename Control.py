class DesiredAngle(object):
    def get(angle):
        return angle
    
    def set(angle, value):
        pass

class DesiredRate(object):
    def get(angle):
        return angle

    def set(angle, rate):
        pass
    
class DesiredPosition(object):
    def get(AXIS):
        return AXIS

    def set(AXIS, position):
        pass

    def setRelative(AXIS, position):
        pass

class DesiredVelocity(object):
    def get(AXIS):
        return AXIS

    def set(AXIS, velocity):
        pass

class PIDProfile(object):
    def get(PROFILE, *profile):
        return PROFILE

    def set(PROFILE, *profile):
        pass

    def setDefault():
        pass

class Failsafe(object):
    def enable(Failsafe):
        pass

    def disable(Failsafe):
        pass