import RPi.GPIO as GPIO
from time import sleep
import serial
from direction import Coordinate

from clientsocket import ClientSocket

PIN_BUZZER = 40

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_BUZZER, GPIO.OUT)

client_socket = ClientSocket("10.201.2.77", 37037, 1024)


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

coordinate = None

while True:
	received_text = serial_port_reader.readline()

	if received_text.startswith("$GPGLL"):
		splitted_data = received_text.split(",")

		if splitted_data[1] == "" or splitted_data[3] == "":
			continue

		latitude_dmm = float(splitted_data[1])
		longitude_dmm = float(splitted_data[3])

		latitude_dd = dmm2dd(latitude_dmm)
		longitude_dd = dmm2dd(longitude_dmm)

		c = Coordinate(float(latitude_dd), float(longitude_dd))

		print("Read:")
		print("Latitude: " + latitude_dd)
		print("Longitude: " + longitude_dd)

		locations = client_socket.get_locations(latitude_dd, longitude_dd)

		print("Get:")
		print(locations)

		if len(locations) > 0:
			print(locations)

			if coordinate != None:
				x = float(locations[0][1])
				y = float(locations[0][2])

				cc = Coordinate(x, y)

				print(coordinate.direction(c.x, c.y, x, y))

			GPIO.output(PIN_BUZZER, GPIO.HIGH)
		else:
			#pass
			GPIO.output(PIN_BUZZER, GPIO.LOW)

		sleep(2)

		coordinate = c
