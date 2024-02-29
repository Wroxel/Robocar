import socket
import PySimpleGUI as sg
import time
import threading


def send_udp_packet(command):
    target_ip = "10.120.0.5"
    target_port = 5005

    message = f"{command}"

    def send_command():
        nonlocal target_ip, target_port, message
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            sock.sendto(message.encode(), (target_ip, target_port))
            if command == "ana":
                response, _ = sock.recvfrom(1024)
                print("Response from IP address:", response.decode())
                window["-RESPONSE_TEXT-"].update(response.decode())
                ana_number = int(response.decode())
                window["-PROGRESS_BAR-"].update(ana_number)
        except Exception as e:
            sg.popup("Error", e)
        finally:
            sock.close()

    threading.Thread(target=send_command).start()


layout = [
    [
        sg.Button("Q", size=(10, 2), key="backspace"),
        sg.Button("↑", size=(10, 2), key="up"),
    ],
    [
        sg.Button("←", size=(10, 2), key="left"),
        sg.Button("↓", size=(10, 2), key="down"),
        sg.Button("→", size=(10, 2), key="right"),
        sg.Text("Response: "),
        sg.Text("", key="-RESPONSE_TEXT-"),
    ],
    [sg.ProgressBar(65356, orientation="h", size=(20, 20), key="-PROGRESS_BAR-")],
]

window = sg.Window("WASD Keys", layout, use_default_focus=False, finalize=True)

window.bind("q", "backspace")
window.bind("w", "up")
window.bind("a", "left")
window.bind("s", "down")
window.bind("d", "right")


while True:
    event, values = window.read()
    print(event, values)

    if event == sg.WINDOW_CLOSED:
        break

    elif event == "up":
        print("Forward button clicked")
        send_udp_packet("forward")
        time.sleep(0.17)

    elif event == "right":
        print("Right button clicked")
        send_udp_packet("right")
        time.sleep(0.17)

    elif event == "left":
        print("Left button clicked")
        send_udp_packet("left")
        time.sleep(0.17)

    elif event == "down":
        print("Backward button clicked")
        send_udp_packet("backward")
        time.sleep(0.17)

    elif event == "stop":
        print("Backspace button clicked")
        send_udp_packet("stop")
        time.sleep(0.2)

    elif event == "backspace":
        print("Backspace button clicked")
        send_udp_packet("ana")
        time.sleep(0.2)

window.close()
