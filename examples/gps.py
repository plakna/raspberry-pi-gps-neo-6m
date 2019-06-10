import serial
import pynmea2

def parse_gps(line):
    msg = pynmea2.parse(line)
    print((msg.timestamp, msg.latitude, msg.longitude))


serialPort = serial.Serial("/dev/ttyAMA0", 9600, timeout=5)
while True:
    line = serialPort.readline()

    if line.find('GGA') > 0:
        parse_gps(line)
        