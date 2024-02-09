import sensors
import motors
import time


def wall_follow():

    # print(f"New {distance} cm")
    while True:
        distance = sensors.gy53()
        time.sleep(0.2)
        if distance > 80:
            print(f"Drive left distance is {distance}")
        elif distance <= 80 >= 50:
            print(f"Drive foward distance is {distance}")
        elif distance > 50 <= 1:
            print(f"Drive right distance is {distance}")
        else:
            print("None")
    # while distance > 80:
    #     print("Drive")
    #     time.sleep(0.5)
    # while distance < 80:
    #     print("STOP")
    #     time.sleep(0.5)
