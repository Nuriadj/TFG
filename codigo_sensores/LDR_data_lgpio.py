import lgpio
import numpy as np
import csv
import time
import sys


LDR= 4

if (len(sys.argv) != 2):
    error=""
    error=error+"Error: wrong number of arguments, execute as: \npython "+sys.argv[0]+" csv_name"
    sys.exit(error)

csv_name= sys.argv[1]+".csv"

h= lgpio.gpiochip_open(0)
lgpio.gpio_claim_input(h, LDR)

total_v= 100 #numero de muestras en total que se quieren recoger
muestras= [] #array que contiene los valores del sensor

while len(muestras) < total_v:

    state= lgpio.gpio_read(h, LDR)
    muestras.append(state)
    print("STATE", state)
    time.sleep(0.1)
    
datos= np.array(muestras)
np.savetxt(csv_name,datos,delimiter=",",fmt='%s')
