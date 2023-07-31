#include <PlutoPilot.h>
#include <Utils.h>
#include <Sensor.h>
#include <Estimate.h>
#include <Control.h>
#include <User.h>
int16_t Error = 0;
int16_t PlutoXHeading = 0;
void plutoInit() {
}

void onLoopStart() {
LED.flightStatus(DEACTIVATE);
Error = (App.getAppHeading() - Angle.get(AG_YAW));
Monitor.println("Error is: ", Error);
}

void plutoLoop() {
Monitor.println("PhoneHeading: ", App.getAppHeading());
PlutoXHeading = (App.getAppHeading() - Error);
if (PlutoXHeading < 0) {
PlutoXHeading += 360;
}
Monitor.println("Pluto X should turn to ", PlutoXHeading);
DesiredAngle.set(AG_YAW, PlutoXHeading);
Monitor.println("Pluto X is at: ", Angle.get(AG_YAW));
LED.set(RED, ON);
LED.set(GREEN, ON);
}

void onLoopFinish() {
LED.flightStatus(ACTIVATE);
}

