import sensors
import motors
import time


def wall_follow():
    time.sleep(5)
    while True:
        distance = sensors.gy53()
        # time.sleep(0.1)

        if distance > 100:
            print(f"Drive right distance is {distance}")
            motors.left_Drive_Long(0.43, 0.30)
            time.sleep(0.1)
            motors.left_Drive(0.25, 0.42)

        if distance > 50:
            print(f"Drive right distance is {distance}")
            motors.left_Drive(0.45, 0.25)
            time.sleep(0.1)
            motors.left_Drive(0.25, 0.42)

        elif 20 < distance <= 50:
            print(f"Drive forward distance is {distance}")
            motors.straight_Drive(0.30, 0.30)

        elif 0 <= distance <= 20:
            print(f"Drive left distance is {distance}")
            motors.left_Drive(0.25, 0.45)
            time.sleep(0.1)
            motors.left_Drive(0.41, 0.28)
        else:
            print("Error")
        # time.sleep(1)

        # time.sleep(0.1)
