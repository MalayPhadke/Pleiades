#include <PlutoPilot.h>
#include <Utils.h>
#include <Peripheral.h>
void plutoInit() {
GPIO.init(Pin10, OUTPUT);
}

void onLoopStart() {
}

int16_t returnFn() {
return 4;
}

void plutoLoop() {
int16_t ir = GPIO.read(Pin10);
Monitor.println("IR: ", ir);
}

void onLoopFinish() {
}

