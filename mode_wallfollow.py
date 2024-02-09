import sensors
import motors
import time


def wall_follow():
    while True:
        distance = sensors.gy53()
        time.sleep(0.2)
        if distance > 80:
            print(f"Drive right distance is {distance}")
            # Få den til at køre til højre i x sekunder

        elif distance > 30 and distance <= 80:
            print(f"Drive forward distance is {distance}")
            # Få den til at køre ligeud i x sekunder

        elif distance <= 30 and distance > 0:
            print(f"Drive left distance is {distance}")
            # Få den til at køre til venstre x sekunder

        else:
            print("Else")
