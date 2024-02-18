import motors
import sensors
import time


def sumo_mode():
    
    time.sleep(5)
    
    while True:
        reflective_surface = sensors.qr113() / 100
        distance = sensors.gy53()
        time.sleep(0.01)
        
        # Standard, scanner alt.
        while distance > 150:
            motors.scan_All(0.35, 0.30)
            reflective_surface = sensors.qr113() / 100
            distance = sensors.gy53()
        
        
        # SCANNER CENTRUM AF KASSEN, FØRST VENSTRE SÅ HØJRE
        if distance < 150:
            drive_right = False

            left_steps = 0
            right_steps = 0

            while distance < 150:
                if drive_right:
                    right_steps += motors.scan_Right(0.35, 0.30)
                else:
                    left_steps += motors.scan_Left(0.35, 0.30)
                
                reflective_surface = sensors.qr113() / 100
                distance = sensors.gy53()
                
                if distance > 150:
                    drive_right = True
                    # Måske vi her skal gøre at den kører lidt til venstre, så den kommer ind under de 150CM igen?
                    # Måske brug for en "else: pass" her?
                
                # Kunne godt ske et problem her, med at den ikke ved hvornår den skal breake drive_right?
        
        
            scan_Average = (left_steps + right_steps) / 2
            
            
            # Kører mod centrum
            while True:
                steps = motors.scan_Left(0.35, 0.30)
                
                if steps >= scan_Average:
                    break
            
            # for _ in range(int(scan_Average)):
            #     motors.scan_Left(0.35, 0.30)
            
            
            
            while reflective_surface <= 300:
                motors.sumo_Drive_Forward(0.35, 0.35)
                time.sleep(0.2)
                reflective_surface = sensors.qr113() / 100

            
            time.sleep(0.5)
            
            if reflective_surface > 300:
                motors.stopDrive()
                time.sleep(0.1)
                motors.sumo_drive_Backward(0.35, 0.35)
                time.sleep(0.1)
                motors.sumo_drive_Right(0.35, 0.30)
                break