import motors
import sensors
import time


def moving_average(data, window_size):
    if len(data) < window_size:
        return sum(data) / len(data)
    return sum(data[-window_size:]) / window_size


def sumo_mode2():
    window_size = 5
    distance_buffer = []

    while True:
        distance = sensors.gy53()
        distance_buffer.append(distance)

        avg_distance = moving_average(distance_buffer, window_size)

        reflective_surface = sensors.qr113() / 100

        # SCAN ALL > 100 CM
        if avg_distance >= 150:
            motors.scan_All(0.35, 0.35)
            reflective_surface = sensors.qr113() / 100

        # KØRE LIGEUD < UNDER 100 CM
        else:
            motors.drive_Forward(0.40, 0.40)
            reflective_surface = sensors.qr113() / 100

            # KØRE TILBAGE -> UDOVER STREG
            if reflective_surface >= 300:
                motors.stopDrive()
                time.sleep(0.1)
                motors.drive_Backward(0.35, 0.35)
                time.sleep(0.1)
                motors.drive_Right(0.35, 0.35)
