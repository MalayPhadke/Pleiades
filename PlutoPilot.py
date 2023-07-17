from Sensor import Acceleration, Magnetometer, Barometer, Gyroscope
from Estimate import Velocity
crashed = True
def plutoInit():
    pass
def onLoopStart():
    pass

def plutoLoop():
   rc_Roll_Stick = 0
   rc = []
   rc = RcData.get()
   rc_Roll_Stick = rc[0]
   rc_Throttle_stick = rc[1]
def onLoopFinish():
    pass