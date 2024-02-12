import sensors
import motors
import time


def wall_follow():
    time.sleep(3)
    while True:
        distance = sensors.gy53()
        time.sleep(0.1)
        
        if distance > 80:
            print(f"Drive right distance is {distance}")
            motors.right_Drive(0.35, 0.25)

        elif 30 < distance <= 80:
            print(f"Drive forward distance is {distance}")
            motors.straight_Drive(0.25, 0.25)

        elif 0 < distance <= 30:
            print(f"Drive left distance is {distance}")
            motors.left_Drive(0.25, 0.35)
        else:
            print("Error")
        
        time.sleep(0.1)