from Sensors import Acceleration, Magnetometer, Barometer, Gyroscope
def plutoInit():
    pass

def onLoopStart():
    pass

def plutoLoop():
    rmsAcc = Acceleration.getNetAcc()
    if (rmsAcc > 10 and rmsAcc < 20):
        print(rmsAcc)  
    elif (rmsAcc  < 10 and rmsAcc > 5):
        print(rmsAcc-10)   
    elif (rmsAcc < 5 and rmsAcc > 0):
        print(rmsAcc+10)   
    else:
        print("Unknown")

def onLoopEnd():
    pass