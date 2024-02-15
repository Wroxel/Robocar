import socket
import PySimpleGUI as sg
import time


def send_udp_packet(command):
    target_ip = "10.120.0.87"
    target_port = 5005

    message = f"{command}"

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        sock.sendto(message.encode(), (target_ip, target_port))
    except Exception as e:
        sg.popup("Error", e)
    finally:
        sock.close()


layout = [
    [
        sg.Button("Q", size=(10, 2), key="backspace"),
        sg.Button("↑", size=(10, 2), key="up"),
    ],
    [
        sg.Button("←", size=(10, 2), key="left"),
        sg.Button("↓", size=(10, 2), key="down"),
        sg.Button("→", size=(10, 2), key="right"),
        # sg.Slider(default_value=45, range=(0,100))
    ],
]

window = sg.Window("WASD Keys", layout, use_default_focus=False, finalize=True)

window.bind("q", "backspace")
window.bind("w", "up")
window.bind("a", "left")
window.bind("s", "down")
window.bind("d", "right")
# window.bind("<KeyRelease-w>", "stop")


while True:
    event, values = window.read()
    print(event, values)
    
    if event == sg.WINDOW_CLOSED:
        break

    elif event == "up":
        print("Forward button clicked")
        send_udp_packet("forward")
        time.sleep(0.2)

    elif event == "right":
        print("Right button clicked")
        send_udp_packet("right")
        time.sleep(0.2)

    elif event == "left":
        print("Left button clicked")
        send_udp_packet("left")
        time.sleep(0.2)

    elif event == "down":
        print("Backward button clicked")
        send_udp_packet("backward")
        time.sleep(0.2)

    elif event == "stop":
        print("Backspace button clicked")
        send_udp_packet("stop")
        time.sleep(0.2)
    # time.sleep(0.01)

window.close()
