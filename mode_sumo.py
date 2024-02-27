import motors
import sensors
import time
import mode_debug

# NUMMER 1 LØSNING (KØRER LIGEUD NÅR MÅLER NOGET)

def gennemsnitlig_måling(data, window_size):
    if len(data) < window_size:
        pass
    return int(sum(data[-window_size:]) / window_size)


def getAverage(antalMålinger):
    total = 0

    for x in range(antalMålinger):
        total += sensors.gy53()

    return total / antalMålinger


def sumo_mode2():
    window_size = 5
    distance_buffer = [sensors.gy53()] * window_size
    buffer_index = 0

    while True:
        distance_buffer[buffer_index] = sensors.gy53()

        buffer_index = (buffer_index + 1) % window_size

        avg_distance = sum(distance_buffer) / window_size



        reflective_surface = sensors.qr113() / 100

        # SCAN ALL > 125 CM
        if avg_distance >= 150:
            motors.scan_All(0.45, 0.45)
            reflective_surface = sensors.qr113() / 100

        # KØRE LIGEUD < UNDER 125 CM
        else:
            motors.sumo_Drive_Forward(0.50, 0.58)
            reflective_surface = sensors.qr113() / 100

            # KØRE TILBAGE -> UDOVER STREG
            if reflective_surface >= 300:
                motors.sumo_drive_Backward(0.35, 0.60)




# NUMMER 2 LØSNING (WHILE STATEMENT)

def drive_forward():
    while True:
        motors.sumo_Drive_Forward(0.50, 0.58)
        reflective_surface = sensors.qr113() / 100
        if reflective_surface >= 300:
            motors.sumo_drive_Backward(0.35, 0.60)
            break


def sumo_mode2():
    window_size = 5
    distance_buffer = [sensors.gy53()] * window_size
    buffer_index = 0

    while True:
        distance_buffer[buffer_index] = sensors.gy53()

        buffer_index = (buffer_index + 1) % window_size

        avg_distance = sum(distance_buffer) / window_size
        print(avg_distance)
        reflective_surface = sensors.qr113() / 100

        # SCAN ALL > 125 CM
        if avg_distance >= 150:
            motors.scan_All(0.45, 0.45)
            reflective_surface = sensors.qr113() / 100

        else:
            drive_forward()

            # Backward if reflective surface detected
            if reflective_surface >= 300:
                motors.sumo_drive_Backward(0.35, 0.60)
            # KØRE TILBAGE -> UDOVER STREG
