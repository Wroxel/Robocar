# Indeholder både GY-53 og IR-Sensor
from machine import Pin, ADC
import time


# GY53
def gy53():
    gy53 = Pin(17, Pin.IN)
    while True:

        # Echo signal starter
        while gy53.value() == True:
            pass
        while gy53.value() == False:
            pass
        startTime = time.ticks_us()

        # Echo signal slutter
        while gy53.value() == True:
            pass
        endtime = time.ticks_us()

        diffInMicroS = endtime - startTime
        diffInCM = diffInMicroS / 100
        return diffInCM



# QR113
def qr113():
    refl_sens = ADC(Pin(28))
    return refl_sens.read_u16()
