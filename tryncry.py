import serial
import time

# Establish serial connection with Arduino
ser = serial.Serial('/dev/tty.usbmodem1101', 9600, timeout=1)

# Wait for serial connection to establish
time.sleep(2)

try:
    # Send "hello" to Arduino
    ser.write(b'180')

    # Read the echoed message from Arduino
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode().strip()
            print("Arduino says:", data)
            break

finally:
    ser.close()
