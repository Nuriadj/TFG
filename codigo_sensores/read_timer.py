import lgpio
import numpy as np
import csv
import time
import sys


#Hasta que no se pulse Ctr-C seguirá leyendo

LDR= 4

if (len(sys.argv) != 2):
    error=""
    error=error+"Error: wrong number of arguments, execute as: \npython "+sys.argv[0]+" csv_name"
    sys.exit(error)

csv_name= sys.argv[1]+".csv"

h= lgpio.gpiochip_open(0)
lgpio.gpio_claim_input(h, LDR)

muestras= [] #array que contiene los valores del sensor
muestras.append(["TIME", "LIGHT"])

try:
    while True:

        state= lgpio.gpio_read(h, LDR)
        state= 1 - state
        muestras.append([time.time(), state])
        print("STATE", state)
        time.sleep(0.1)
except KeyboardInterrupt:
   pass   

    
datos= np.array(muestras)
np.savetxt(csv_name,datos,delimiter=",",fmt='%s')
