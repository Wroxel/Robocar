from machine import Pin, ADC
import motors
import time
import network
import socket


def udp_1():
    motors.IN1 = Pin(2, Pin.OUT)
    adc = ADC(Pin(26))
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect("ITEK 2nd", "2nd_Semester_F24v")

    while not wlan.isconnected() and wlan.status() >= 0:
        print("Waiting to connect")
        time.sleep(1)

    print(wlan.ifconfig())
    time.sleep(1)

    UDPServerConnect = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    UDPServerConnect.bind(("0.0.0.0", 5005))
    bufferSize = 100

    print("Listening")

    while True:
        bytesAddressPair = UDPServerConnect.recvfrom(bufferSize)
        message, clientAddress = bytesAddressPair
        print(message)
        answear = b"default answear"
        if message == b"on":
            answear = b"onnn"
            motors.drivePWM()

        if message == b"off":
            motors.IN1.off()
        if message == b"ana":
            answear = str(adc.read_u16())
        clientAddress = bytesAddressPair[1]
        print(clientAddress)
        print("Ready")
        sent = UDPServerConnect.sendto(answear, clientAddress)
