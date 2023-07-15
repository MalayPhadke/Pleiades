from Sensors import Acceleration, Magnetometer, Barometer, Gyroscope
from Estimate import Velocity
crashed = True
def plutoInit():
    pass

def onLoopStart():
    pass

def plutoLoop():
    rmsAcc = Acceleration.getNetAcc()
    if (Acceleration.getNetAcc() < 2 and not crashed):
        print((rmsAcc+1)-6)  
    elif (rmsAcc < 10):
        print(rmsAcc-10)   
    elif (rmsAcc < 5 and rmsAcc > 0):
        print(rmsAcc+10)   
    else:
        print("Unknown")
    vel = Velocity.get(X)
    if(vel > 10):
        print("velocity > 10")

def onLoopEnd():
    pass