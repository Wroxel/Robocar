from machine import Pin, ADC
import motors
import time
import network
import socket


def remote_control():
    motors.IN1 = Pin(2, Pin.OUT)
    adc = ADC(Pin(26))
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect("ITEK 2nd", "2nd_Semester_F24v")

    while not wlan.isconnected():  # and wlan.status() >= 0:
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
        answer = b"default answer"

        # Tilføj forskellige messages & funktioner her 😎 ->

        if message == b"ana":
            answer = str(adc.read_u16())

        if message == b"forward":
            answer = b"forward"
            motors.drive_Forward(0.80, 0.80)

        if message == b"left":
            answer = b"left"
            motors.drive_Left(0.50, 0.40)

        if message == b"right":
            answer = b"right"
            motors.drive_Right(0.40, 0.50)

        if message == b"backward":
            answer = b"backward"
            motors.drive_Backward(0.50, 0.50)

        clientAddress = bytesAddressPair[1]
        print(clientAddress)
        print("Ready")
        sent = UDPServerConnect.sendto(answer, clientAddress)
