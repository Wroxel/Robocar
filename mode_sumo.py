import motors
import sensors
import time


def sumo_mode():
    while True:
        reflective_surface = sensors.qr113() / 100
        distance = sensors.gy53()
        time.sleep(0.01)
        
        # Tjekker om den kører udfor banden
        if reflective_surface > 300:
            motors.stopDrive()
            time.sleep(0.1)
            motors.sumo_drive_Backward(0.30, 0.30)
            time.sleep(0.1)
            motors.sumo_drive_Right(0.35, 0.30)

        # else:
        #     if distance < 50:
        #         motors.straight_Drive(0.35, 0.35)
        #         time.sleep(0.01)
        #     else:
        #         motors.stopDrive()
        #         motors.sumo_drive_Right(0.35, 0.30)
        #         time.sleep(0.01)
        
        else:
            if distance < 50:
                while True:
                    if distance < 50:
                        motors.sumo_drive_Left(0.30, 0.35)
                    elif distance > 80:
                        motors.sumo_drive_Right(0.35, 0.30)
                    else:
                        break
                    distance = sensors.gy53()
            else:
                motors.straight_Drive(0.35, 0.35)
                time.sleep(0.01)
