import PySimpleGUI as sg

layout = [
    [sg.Button("←", key="left")],
    [sg.Button("→", key="right")],
    [sg.Button("↑", key="up")],
    [sg.Button("↓", key="down")],
]

window = sg.Window("test", layout)

while True:
    event, data = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    elif event in ("left", "right", "up", "down"):
        print("Directional button clicked:", event)

window.close()
