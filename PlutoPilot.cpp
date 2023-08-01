#include <PlutoPilot.h>
#include <Utils.h>
#include <Sensor.h>
#include <Estimate.h>
#include <Control.h>
#include <User.h>
void plutoInit() {
}

void onLoopStart() {
LED.flightStatus(DEACTIVATE);
int16_t Error = (App.getAppHeading() - Angle.get(AG_YAW));
int16_t* arr;
bool test = (Error > 10) ? true : false;
int16_t new = arr[3];
Monitor.println("Error is: ", Error);
}

void plutoLoop() {
Monitor.println("PhoneHeading: ", App.getAppHeading());
Monitor.println("Pluto X is at: ", Angle.get(AG_YAW));
LED.set(RED, ON);
LED.set(GREEN, ON);
Command.arm();
Graph.red(Velocity.get(Z), 1);
}

void onLoopFinish() {
LED.flightStatus(ACTIVATE);
}

