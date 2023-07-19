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
    for i in range(0, 5):
        print(i)
        print(ir)
        UART.write(Pin10, 10)
    text = "Hello, World!"
    for char in text:
        print(char)
        if char == '\n':
            break
    b=[1, 3, 4]
    c, d = 3, 4
    d = 99
    for a in range(c, d):
        if a > 5:
            break
        else:
            continue
    # c = len(b)
    for a in b:
        xyz = b[a]
        print(a)

def onLoopFinish():
    pass