import motors
import sensors
import time

# NUMMER 1 LØSNING (FØRSTE)


def get_smoothed_distance(window_size=5):

    distance_buffer = [sensors.gy53()] * window_size
    buffer_index = 0

    while True:
        distance_buffer[buffer_index] = sensors.gy53()
        buffer_index = (buffer_index + 1) % window_size

        avg_distance = sum(distance_buffer) / window_size
        return avg_distance


def sumo_mode2():
    while True:
        avg_distance = get_smoothed_distance()
        reflective_surface = sensors.qr113() / 100

        # SCAN ALL > 150 CM
        if avg_distance >= 150:
            while avg_distance >= 150:
                motors.scan_All(0.52, 0.52)
                avg_distance = get_smoothed_distance()

        # KØRE LIGEUD < UNDER 150 CM
        else:
            # Drive forward until reflective surface is over 300
            while reflective_surface < 300 and avg_distance < 125:
                motors.sumo_Drive_Forward(0.50, 0.54)
                reflective_surface = sensors.qr113() / 100
                if reflective_surface >= 300:
                    # Drive backward and break
                    motors.sumo_drive_Backward(0.40, 0.40)
                    time.sleep(0.1)
                    motors.sumo_drive_Right(0.35, 0.35)
                    break
