from Peripheral import GPIO, ADC, UART
Pin10 = 5
OUTPUT = True
def plutoInit():
    GPIO.init(OUTPUT)
    ADC.init()
    UART.init()
def onLoopStart():
    pass

def returnFn() -> int:
    return 4

def plutoLoop():
    ir = GPIO.read(Pin10)
    UART.write(Pin10, 20)
    print("IR: " , ir)

def onLoopFinish():
    pass
