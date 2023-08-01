from Sensor import Acceleration, Magnetometer, Barometer, Gyroscope
from Estimate import Angle, Velocity
from Control import DesiredAngle
from User import App, Command
from Utils import LED, Graph
from Constants import *

def plutoInit():
    pass


def onLoopStart():
    LED.flightStatus(DEACTIVATE)
    Error = App.getAppHeading() - Angle.get(AG_YAW)
    arr = []
    test = True if (Error > 10) else False
    new = arr[3]
    print("Error is: ", Error)
    LED.set(RED, ON)

def plutoLoop():
    print("PhoneHeading: ", App.getAppHeading())
    print("Pluto X is at: ", Angle.get(AG_YAW))
    LED.set(RED, ON)
    LED.set(GREEN, ON)
    Command.arm()
    Graph.red(Velocity.get(Z), 1)


def onLoopFinish():
    LED.flightStatus(ACTIVATE)