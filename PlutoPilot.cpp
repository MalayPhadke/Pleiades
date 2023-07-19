#include <PlutoPilot.h>
#include <Utils.h>
#include <Peripheral.h>
int16_t Pin10 = 5;
bool OUTPUT = true;
void plutoInit() {
GPIO.init(Pin10, OUTPUT);
}

void onLoopStart() {
}

char* returnFn() {
return GPIO;
}

void plutoLoop() {
int16_t ir = GPIO.read(Pin10);
if (ir == 1) {
Monitor.println("No object detected");
}
else {
Monitor.println("Object detected!");
}
}

void onLoopFinish() {
}

