import sys
import Adafruit_DHT
import RPi.GPIO as GPIO

BuzzerPin = 3
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BuzzerPin, GPIO.OUT, initial=GPIO.LOW)

while True:
  humidity, temperature = Adafruit_DHT.read_retry(11,4)
  print("Temp={0:0.1f}*C Humidity={1:0.1f}%".format(temperature, humidity))
  if(temperature>17): GPIO.output(3, GPIO.HIGH)
  else: GPIO.output(3, GPIO.LOW)
