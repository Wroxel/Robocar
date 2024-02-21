import sensors
import motors
import time


def wall_follow():
    time.sleep(5)
    while True:
        distance = sensors.gy53()

        # Kode som reagere på front mod væg og hjørner — Start

        # I mod væg
        if distance < 4:
            motors.drive_Backward(0.30, 0.30)

        # Hjørne
        if distance > 150:
            print(0)
            # Få motoren til at kører 90 grader til højre og køre ligeud i antal sekunder???

        # Kode som reagere på front mod væg og hjørner — Slut

        # Kode som holder afstanden til væggen — Start

        if 100 < distance <= 150:
            motors.left_Drive(0.25, 0.48)
            time.sleep(0.1)
            motors.stopDrive()

        elif distance > 50:
            motors.left_Drive(0.45, 0.25)
            time.sleep(0.1)
            motors.left_Drive(0.25, 0.42)
            time.sleep(0.1)
            motors.stopDrive()

        elif 20 < distance <= 50:
            motors.straight_Drive(0.35, 0.35)
            time.sleep(0.1)
            motors.stopDrive()

        elif 4 <= distance <= 20:
            motors.left_Drive(0.25, 0.45)
            time.sleep(0.1)
            motors.left_Drive(0.42, 0.28)
            time.sleep(0.1)
            motors.stopDrive()
        else:
            print("Error")

        # Kode som holder afstanden til væggen — Start

        time.sleep(0.1)
