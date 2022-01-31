import RPi.GPIO as GPIO

#no va?

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)# Lee del pin 4
while True:
    tmp= GPIO.input(4)
    print(tmp)
    if(tmp == GPIO.HIGH):
        print("Frio")
    else:
        print("Calor")
