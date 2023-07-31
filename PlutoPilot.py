from Peripheral import GPIO, ADC, UART

def plutoInit():
    GPIO.init(Pin10, OUTPUT)
def onLoopStart():
    pass



def plutoLoop():
    ir = GPIO.read(Pin10)
    if (ir == 1):
        print("No object detected")
    else:
        print("Object detected!")

def onLoopFinish():
    pass