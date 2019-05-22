import serial


reader = serial.Serial(
	port='/dev/ttyS0',
	baudrate=9600,
	timeout=1
)

while True:
	data = reader.readline()

	if data.startswith("$GPGLL"):
		print(data)
