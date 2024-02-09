# Indeholder både GY-53 og IR-Sensor
from machine import Pin
import time


# GY53
def gy53():
    gy53 = Pin(17, Pin.IN)
    while True:

        while gy53.value() == True:
            pass
        while gy53.value() == False:
            pass
        startTime = time.ticks_us()
        while gy53.value() == True:
            pass
        endtime = time.ticks_us()
        diffInMicroS = endtime - startTime
        diffInMM = diffInMicroS / 10
        diffInCM = diffInMicroS / 100
        diffInCM = diffInCM
        # print("MM: ")
        # print(diffInMM)
        # print("CM: ")
        # print(diffInCM)
        time.sleep(1)

        return diffInCM


# QR113
def qr113():
    return 0
