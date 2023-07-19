#include <PlutoPilot.h>
#include <Utils.h>
#include <Peripheral.h>
int16_t Pin10 = 5;
bool OUTPUT = true;
void plutoInit() {
GPIO.init(OUTPUT);
ADC.init();
UART.init();
}

void onLoopStart() {
}

int16_t returnFn() {
return 4;
}

void plutoLoop() {
int16_t ir = GPIO.read(Pin10);
UART.write(Pin10, 20);
Monitor.println("IR: ", ir);
for (int i = 0; i < 5; i++) {
Monitor.println("Value:", i);
Monitor.println("Value:", ir);
UART.write(Pin10, 10);
}
char* text = "Hello, World!";
Monitor.println("Value:", char);
if (char == "
") {
break;
}
}
int16_t* b = {1, 3, 4};
int16_t c = 3;
int16_t d = 4;
d = 99;
for (int a = c; a < d; a++) {
if (a > 5) {
break;
}
else {
continue;
}
}
for (int a = 0; a < 3; a++) {
int16_t xyz = b[a];
Monitor.println('Value:' b[a]);
Monitor.println("Value:", a);
}
}

void onLoopFinish() {
}

