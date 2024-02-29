import sensors
import motors
import time


def wall_follow2():

    time.sleep(5)

    while True:
        distance = sensors.gy53()

        # 20 cm fra væggen
        if distance <= 20:
            motors.drive_Backward(0.36, 0.41)
            time.sleep(0.1)
            motors.wall_look_left(0.40, 0.40)

        # Mellem 20 cm og 50 cm
        elif 20 < distance < 40:
            # 0.34, 0.56
            motors.wall_left_Drive(0.39, 0.63)

        # Mellem 50 cm og 90 cm -> Idealt
        elif 40 <= distance <= 120:
            motors.wall_straight_Drive(0.97, 1)

        # Over 90 cm
        elif distance > 120:
            motors.wall_drive_Right(0.54, 0.40)

        else:
            print("Error")
