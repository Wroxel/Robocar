import sensors
import motors
import time


def wall_follow2():
    time.sleep(5)
    while True:
        distance = sensors.gy53()

        # Kode som reagere på front mod væg og hjørner — Start

        # left_Wheel = 0
        # right_Wheel = 0

        if distance < 20:
            motors.drive_Backward(0.35, 0.35)
            time.sleep(0.1)
            motors.wall_look_left(0.35, 0.35)

        # Væg forsvundet
        elif distance > 69:
            motors.wall_gone_cont(1, 1)
            time.sleep(0.1)
            motors.wall_look_right(0.35, 0.35)
            # Få motoren til at kører 90 grader til højre og køre ligeud i antal sekunder???

        # Væg just right :)
        elif 20 <= distance <= 69:
            motors.wall_straight_Drive(1, 1)

        else:
            print("Error")

        # Kode som reagere på front mod væg og hjørner — Slut

        # Kode som holder afstanden til væggen — Start

        # if 100 < distance <= 150:
        #     motors.wall_left_Drive(0.25, 0.48)
        #     time.sleep(0.1)
        #     motors.stopDrive()

        # elif distance > 50:
        #     motors.wall_left_Drive(0.45, 0.25)
        #     time.sleep(0.1)
        #     motors.wall_left_Drive(0.25, 0.42)
        #     time.sleep(0.1)
        #     motors.stopDrive()

        # elif 20 < distance <= 50:
        #     motors.wall_straight_Drive(0.35, 0.35)
        #     time.sleep(0.1)
        #     motors.stopDrive()

        # elif 4 <= distance <= 20:
        #     motors.wall_left_Drive(0.25, 0.45)
        #     time.sleep(0.1)
        #     motors.wall_left_Drive(0.42, 0.28)
        #     time.sleep(0.1)
        #     motors.stopDrive()
        # else:
        #     print("Error")

        # # Kode som holder afstanden til væggen — Slut

        # time.sleep(0.1)
