import serial

def RSSI(port):
        with serial.Serial(port, baudrate=115200, timeout=5) as ser:
            line = ser.readline()
            rssi = line.decode().strip()
        return rssi



if __name__ == '__main__':
    port = "/dev/ttyACM0"
    RSSI(port)



