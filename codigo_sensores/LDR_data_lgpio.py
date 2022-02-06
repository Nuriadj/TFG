import lgpio
import numpy as np
import csv

LDR= 4

h= lgpio.gpiochip_open(0)
lgpio.gpio_claim_input(h, LDR)

total_v= 100 #numero de muestras en total que se quieren recoger
muestras= [] #array que contiene los valores del sensor

while len(muestras) < total_v:

    state= lgpio.gpio_read(h, LDR)
    print("STATE", state)
    
datos= np.array(muestras)
np.savetxt("Muestras_LDR.csv",data,delimiter=",",fmt='%s')
