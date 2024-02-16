import sensors
import motors
from time import sleep


def wall_follow():
    sleep(5)
    while True:
        distance = sensors.gy53()

        if distance > 100:
            print(f"Drive right distance is {distance}")
            motors.left_Drive_Long(0.46, 0.25)
            sleep(0.1)
            motors.left_Drive(0.25, 0.48)
            sleep(0.1)
            motors.stopDrive()

        if distance > 50:
            print(f"Drive right distance is {distance}")
            motors.left_Drive(0.45, 0.25)
            sleep(0.1)
            motors.left_Drive(0.25, 0.42)
            sleep(0.1)
            motors.stopDrive()

        elif 20 < distance <= 50:
            print(f"Drive forward distance is {distance}")
            motors.straight_Drive(0.35, 0.35)
            sleep(0.1)
            motors.stopDrive()

        elif 0 <= distance <= 20:
            print(f"Drive left distance is {distance}")
            motors.left_Drive(0.25, 0.45)
            sleep(0.1)
            motors.left_Drive(0.42, 0.28)
            sleep(0.1)
            motors.stopDrive()
        else:
            print("Error")
        sleep(0.1)
