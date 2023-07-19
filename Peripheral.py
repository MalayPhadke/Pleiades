class GPIO(object):
    def init(pin_number, mode):
        pass

    def read(pin_number):
        return pin_number

    def write(pin_number, state):
        pass

class ADC(object):
    def init(pin_number):
        pass

    def read(pin_number):
        pass

class PWM(object):
    def init(pin_number, pwmRate):
        pass

    def write(pin_number, pwmRate):
        pass

class UART(object):
    def init(port, baudrate):
        pass

    def read8(port):
        pass

    def read16(port):
        pass
    def read32(port):
        pass
    
    def write(port, data):
        pass
    
    def write(port, data, length):
        pass

    def rxBytesWaiting(port):
        pass
    
    def rxBytesFree(port):
        pass

class I2C(object):
    def read(device_add, req, length):
        pass

    def write(device_add, reg, length, data):
        pass 


