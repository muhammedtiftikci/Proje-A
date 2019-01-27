import RPi.GPIO as GPIO
from time import sleep

pinBuzzer = 40

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinBuzzer, GPIO.OUT)

while True:
	GPIO.output(pinBuzzer, GPIO.HIGH)
	sleep(1)

	GPIO.output(pinBuzzer, GPIO.LOW)
	sleep(1)

