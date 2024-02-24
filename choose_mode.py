try:
    import usocket as socket
except:
    import socket

import network
import time
import motors
import mode_remote
import mode_wallfollow2
import motors
import mode_sumo2
from machine import Pin


# Link til hjemmesiden -> http://10.120.0.87:84/


def choose_gamemode():
    ssid = "ITEK 2nd"
    password = "2nd_Semester_F24v"

    station = network.WLAN(network.STA_IF)

    station.active(True)
    station.connect(ssid, password)

    while not station.isconnected():
        pass

    print("Connection successful")
    print(station.ifconfig())

    # Gamemode LED
    pin_LedGREEN = Pin(11, mode=Pin.OUT)
    pin_LedYELLOW = Pin(12, mode=Pin.OUT)
    pin_LedRED = Pin(13, mode=Pin.OUT)

    def web_page():
        html = """<html>

        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css"
            integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
            <link href="https://fonts.googleapis.com/css2?family=Ubuntu+Mono:wght@700&display=swap" rel="stylesheet">
            <style>
            html {
                font-family: 'Ubuntu Mono', monospace;
                display: inline-block;
                margin: 0px auto;
                text-align: center;
            }


            body {
                font-family: 'Ubuntu Mono', monospace;
                position: relative;
            }
            </style>
        </head>
        <body>
            <h2>Robocar</h2>
            <p>
                <a href=\"remote\"><button>Remote Control Mode</button></a>
                <a></a>
            </p>
            <p>
                <a href=\"sumo\"><button>Sumo Mode</button></a>
                <a></a>
            </p>
            <p>
                <a href=\"wallfollow\"><button>Wall Follow Mode</button></a>
                <a></a>
            </p>

        </body>
        </html>"""
        return html

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 84))
    s.listen(5)
    conn = 0

    while True:
        try:
            conn, addr = s.accept()
            conn.settimeout(3.0)
            request = conn.recv(1024)
            conn.settimeout(None)
            request = str(request)
            remote = request.find("/remote")
            sumo = request.find("/sumo")
            wallfollow = request.find("/wallfollow")

            if remote == 6:
                pin_LedGREEN.on()
                pin_LedRED.off()
                pin_LedYELLOW.off()

                mode_remote.remote_control()
                print("Remote Control Mode")
            if sumo == 6:
                pin_LedGREEN.off()
                pin_LedRED.on()
                pin_LedYELLOW.off()

                mode_sumo2.sumo_mode2()
                print("Sumo Mode")
            if wallfollow == 6:
                pin_LedGREEN.off()
                pin_LedRED.off()
                pin_LedYELLOW.on()

                mode_wallfollow2.wall_follow2()
                print("Wallfollow Mode")

            response = web_page()
            conn.send("HTTP/1.1 200 OK\n")
            conn.send("Content-Type: text/html\n")
            conn.send("Connection: close\n  \n")
            conn.sendall(response)
            conn.close()
        except OSError as e:
            if conn:
                conn.close()
            print("Connection closed")
