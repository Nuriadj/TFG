import RPi.GPIO as GPIO

Sensor= 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(Sensor, GPIO.IN)# Lee del pin 4prueba
while True:
    h= GPIO.input(Sensor)
    if h:
        print('Esta seco')
    else:
        print('Esta humedo')
    #print(GPIO.input(Sensor))