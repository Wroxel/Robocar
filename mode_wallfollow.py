import sensors
import motors
import time


def wall_follow2():

    time.sleep(5)

    while True:
        distance = sensors.gy53()

        # 15 cm fra væggen
        if distance <= 15:
            motors.drive_Backward(0.36, 0.41)
            time.sleep(0.1)
            motors.wall_look_left(0.38, 0.38)

        # Mellem 15 cm og 55 cm
        elif 15 < distance < 55:
            motors.wall_left_Drive(0.38, 0.56)

        # Mellem 55 cm og 90 cm -> Idealt
        elif 55 <= distance <= 90:
            motors.wall_straight_Drive(0.91, 0.91)

        # Over 90 cm
        elif distance > 90:
            motors.wall_drive_Right(0.51, 0.37)

        else:
            print("Error")
