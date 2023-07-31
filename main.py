from Sensor import Acceleration, Magnetometer, Barometer, Gyroscope
from Estimate import Angle
from Control import DesiredAngle
from User import App
from Utils import LED
from Constants import *
Error = 0
PlutoXHeading = 0
def plutoInit():
    pass


def onLoopStart():
    LED.flightStatus(DEACTIVATE)
    Error = App.getAppHeading() - Angle.get(AG_YAW)
    print("Error is: ", Error)

def plutoLoop():
    print("PhoneHeading: ", App.getAppHeading())
    PlutoXHeading = App.getAppHeading() - Error
    if (PlutoXHeading < 0):
        PlutoXHeading+=360
    print("Pluto X should turn to ", PlutoXHeading)
    DesiredAngle.set(AG_YAW, PlutoXHeading)
    print("Pluto X is at: ", Angle.get(AG_YAW))
    LED.set(RED, ON)
    LED.set(GREEN, ON)

def onLoopFinish():
    LED.flightStatus(ACTIVATE)