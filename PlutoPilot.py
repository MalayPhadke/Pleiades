from Sensor import Acceleration, Magnetometer, Barometer, Gyroscope
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
    vel += 10
    stri = "Hello World"
    crashed = False
    print(stri)
    filled = [1, 2, 3, 4, 5, 6, 7, 8]
    rcRoll = filled[0:4]
    if(Velocity.get(X) > 10):
        print("velocity > 10", Velocity.get(X))
    if crashed:
        print("crashed", crashed)
def onLoopFinish():
    pass