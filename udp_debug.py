from machine import Pin, ADC
import motors
import time
import network
import socket
import mode_sumo


def udp_debug():
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

        if message == b"sumo_mode_debug":
            answer = b"sumo_mode_debug"
            avg = mode_sumo.avg_distance_udp()
            print(avg)

        clientAddress = bytesAddressPair[1]
        print(clientAddress)
        print("Ready")
        sent = UDPServerConnect.sendto(answer, clientAddress)
