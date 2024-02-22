import motors
import sensors
import time


def sumo_mode2():
    while True:
        distance = sensors.gy53()
        reflective_surface = sensors.qr113() / 100

        while distance >= 100:
            distance = sensors.gy53()

            motors.scan_All(0.35, 0.35)

        while distance < 100:
            distance = sensors.gy53()
            reflective_surface = sensors.qr113() / 100

            motors.drive_Forward(0.45, 0.45)

            if reflective_surface >= 300:
                motors.stopDrive()
                time.sleep(0.1)
                motors.drive_Backward(0.35, 0.35)
                time.sleep(0.1)
                motors.drive_Right(0.35, 0.35)
