mport Adafruit_DHT as AdaDHT
import RPi.GPIO as GPIO

DHTSensor = AdaDHT.DHT11
DHTPin = 4
BuzzerPin = 3

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BuzzerPin, GPIO.OUT, initial=GPIO.LOW)

while True:
	humidity, temperature = AdaDHT.read_retry(DHTSensor, DHTPin)
	if humidity is not None and temperature is not None:
		print("Temperature={0:0.1f}*C Humidity={1:0.1f}%".format(temperature,humidity))
		if(temperature>32):
			GPIO.output(BuzzerPin, GPIO.HIGH)
		else:
			GPIO.output(BuzzerPin, GPIO.LOW)
	else:
        	print("Failed to retrieve data from sensor")
