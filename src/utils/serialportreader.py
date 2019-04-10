import RPi.GPIO as GPIO
from time import sleep
import serial
from direction import Coordinate

from clientsocket import ClientSocket


client_socket = ClientSocket("192.168.1.8", 37037, 1024)


serial_port_reader = serial.Serial(
	port='/dev/ttyS0',
	baudrate=9600,
	timeout=1
)


def dmm2dd(dmm):
	dmm_str = str(dmm)

	d = dmm_str[0:2]
	mmmmmm = dmm_str[2:4] + dmm_str[5:10]

	m = float(mmmmmm) / 60

	# Stable mm value to 6 chars.
	return d + "." + str(m).replace(".", "").ljust(6)[0:6]


while True:
	received_text = serial_port_reader.readline()

	if received_text.startswith("$GPGLL"):
		splitted_data = received_text.split(",")

		latitude_dmm = float(splitted_data[1])
		longitude_dmm = float(splitted_data[3])

		latitude_dd = dmm2dd(latitude_dmm)
		longitude_dd = dmm2dd(longitude_dmm)

		print("Read:")
		print("Latitude: " + latitude_dd)
		print("Longitude: " + longitude_dd)

		locations = client_socket.get_locations(latitude_dd, longitude_dd)

		print("Get:")
		print(locations)

		sleep(5)
