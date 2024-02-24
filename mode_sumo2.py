import motors
import sensors
import time



# Beregner glidende gennemsnit af data
# data/distance_buffer = En liste af datapunkter
# window_size = Størrelsen af vinduet til beregning af glidende gennemsnit.

# Pointen er at den tager 5 (Fordi window_size er 5) målinger fra GY-53 sensoren og
# dividere det med målingerne for at få mere KONSISTENTE målinger.  (100 + 110 + 120 + 130 + 140) / 5 = 120. f.eks.
def gennemsnitlig_måling(data, window_size):
    if len(data) < window_size:
        return sum(data) / len(data)
    return sum(data[-window_size:]) / window_size


def sumo_mode2():
    window_size = 5
    distance_buffer = []

    while True:
        distance = sensors.gy53()
        distance_buffer.append(distance)
    
        avg_distance = gennemsnitlig_måling(distance_buffer, window_size)

        reflective_surface = sensors.qr113() / 100

        # SCAN ALL > 100 CM
        if avg_distance >= 150:
            motors.scan_All(0.35, 0.35)
            reflective_surface = sensors.qr113() / 100

        # KØRE LIGEUD < UNDER 100 CM
        else:
            motors.drive_Forward(0.40, 0.40)
            reflective_surface = sensors.qr113() / 100

            # KØRE TILBAGE -> UDOVER STREG
            if reflective_surface >= 300:
                motors.stopDrive()
                time.sleep(0.1)
                motors.sumo_drive_Backward(0.35, 0.35)
                time.sleep(0.1)
                motors.sumo_drive_Right(0.35, 0.35)
