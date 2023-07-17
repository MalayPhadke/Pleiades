#include <PlutoPilot.h>
#include <Utils.h>
#include <Sensor.h>
#include <Estimate.h>
bool crashed = true;
void plutoInit() {
}

void onLoopStart() {
}

int16_t returnFn() {
return 1;
}

void plutoLoop() {
int16_t rc_Roll_Stick = 0;
int16_t* rc;
rc = RcData.get();
rc_Roll_Stick = rc[0];
int16_t rc_Throttle_stick = rc[1];
}

void onLoopFinish() {
}

