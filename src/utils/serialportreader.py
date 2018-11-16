import RPi.GPIO as GPIO
from time import sleep
import serial

serial_port_reader = serial.Serial(
	port='/dev/ttyS0',
	baudrate=9600,
	timeout=1
)

while True:
	received_text = serial_port_reader.readline()
	
	print(str(received_text))

	sleep(1)