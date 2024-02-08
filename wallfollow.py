import sensors
import motors


def wall_follow():
    while True:
        distance = sensors.gy53()
        if distance > 80:
            motors.drive()
            print("Driving")
        else:
            motors.stopDrive()
            print("Not Driving")
