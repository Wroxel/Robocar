import motors
import sensors
import time


def sumo_mode():
    motors.stopDrive()
    for i in range(5):
        distance = sensors.gy53()
        reflective_surface = sensors.qr113() / 100

    time.sleep(1)

    # Control flag
    finished = False

    # MAIN LOOP
    while not finished:
        print("Starting main loop")
        time.sleep(0.01)
        reflective_surface = sensors.qr113() / 100
        distance = sensors.gy53()

        # SCANNER ALT
        if distance >= 100:
            while distance >= 100:
                print("Scanner ALT")
                distance = sensors.gy53()
                motors.scan_All(0.35, 0.35)

        # SCANNER CENTRUM
        if distance < 100:
            motors.stopDrive()

            time.sleep(0.01)
            left_steps = 0

            # SCANNER HØJRE
            while distance <= 100:
                print("Scanner højre")
                distance = sensors.gy53()
                reflective_surface = sensors.qr113() / 100

                time.sleep(0.01)

                left_steps += 1
                motors.scan_Right(0.35, 0.35)

            # GÅR MOD MIDTEN
            for _ in range(int(left_steps / 2)):
                print("Kører mod venstre")
                motors.scan_Left(0.30, 0.30)

                time.sleep(0.01)

            # KØRE MOD KASSEN
            while reflective_surface <= 300:
                reflective_surface = sensors.qr113() / 100

                motors.sumo_Drive_Forward(0.50, 0.50)

                time.sleep(0.2)
                if reflective_surface > 300:
                    # KØRE VÆK
                    motors.stopDrive()
                    time.sleep(0.1)

                    motors.sumo_drive_Backward(0.35, 0.35)

                    time.sleep(0.1)
                    motors.sumo_drive_Right(0.35, 0.35)
                    finished = True  # Set the flag to True to break out of the loop
                    break

    time.sleep(0.5)
