try:
    import usocket as socket
except:
    import socket

import network
import time
import motors


def start_web_server():
    ssid = "ITEK 2nd"
    password = "2nd_Semester_F24v"

    station = network.WLAN(network.STA_IF)

    station.active(True)
    station.connect(ssid, password)

    while not station.isconnected():
        pass

    print("Connection successful")
    print(station.ifconfig())

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
                <a href=\"drive\"><button>Drive</button></a>
                <a></a>
            </p>
            <p>
                <a href=\"stop\"><button>Stop</button></a>
                <a></a>
            </p>

        </body>
        </html>"""
        return html

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 81))
    s.listen(5)
    conn = 0

    while True:
        try:
            conn, addr = s.accept()
            conn.settimeout(3.0)
            request = conn.recv(1024)
            conn.settimeout(None)
            request = str(request)
            drive = request.find("/drive")
            stop = request.find("/stop")

            if drive == 6:
                motors.drive()
                print("Driving")
            if stop == 6:
                motors.stopDrive()
                print("Stopping")

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
