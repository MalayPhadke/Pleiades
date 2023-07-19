from Peripheral import GPIO, ADC, UART
Pin10 = 5
OUTPUT = True
def plutoInit():
    GPIO.init(Pin10, OUTPUT)
def onLoopStart():
    pass

def returnFn() -> int:
    return GPIO

def plutoLoop():
    ir = GPIO.read(Pin10)
    if (ir == 1):
        print("No object detected")
    else:
        print("Object detected!")

def onLoopFinish():
    pass