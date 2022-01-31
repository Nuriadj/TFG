import RPi.GPIO as GPIO

LDR= 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(LDR, GPIO.IN)# Lee del pin 4
while True:
    print(GPIO.input(LDR))