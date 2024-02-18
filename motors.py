from machine import Pin, PWM
import time

# Højre motor
IN1 = Pin(2, Pin.OUT)
IN2 = Pin(3, Pin.OUT)

# Venstre motor
IN3 = Pin(4, Pin.OUT)
IN4 = Pin(5, Pin.OUT)

# PWM pins
pwm1 = PWM(Pin(6))
pwm2 = PWM(Pin(7))


# Stopper med at køre
def stopDrive():
    IN1.off()
    IN3.off()
    IN2.off()
    IN4.off()


# Motor for Wall Follow Mode — START


def straight_Drive(left_speed, right_speed):
    pwm1.freq(800)
    pwm2.freq(800)

    pwm1.duty_u16(int(65536 * right_speed))
    pwm2.duty_u16(int(65536 * left_speed))

    IN2.on()
    IN4.on()

    return


def left_Drive(left_speed, right_speed):
    pwm1.freq(800)
    pwm2.freq(800)

    pwm1.duty_u16(int(65536 * left_speed))
    pwm2.duty_u16(int(65536 * right_speed))

    IN2.on()
    IN4.on()
    time.sleep(1)
    IN2.off()
    IN4.off()

    return


def left_Drive_Long(left_speed, right_speed):
    pwm1.freq(800)
    pwm2.freq(800)

    pwm1.duty_u16(int(65536 * left_speed))
    pwm2.duty_u16(int(65536 * right_speed))

    IN2.on()
    IN4.on()
    time.sleep(3)
    IN2.off()
    IN4.off()

    return


# Motor for Wall Follow Mode — SLUT






# Motor for Remote Control Mode — START

def drive_Forward(left_speed, right_speed):
    IN1.off()
    IN3.off()
    IN2.off()
    IN4.off()

    pwm1.freq(800)
    pwm2.freq(800)

    pwm1.duty_u16(int(65536 * left_speed))
    pwm2.duty_u16(int(65536 * right_speed))

    IN2.on()
    IN4.on()
    time.sleep(0.2)
    IN2.off()
    IN4.off()


def drive_Left(left_speed, right_speed):
    IN1.off()
    IN3.off()
    IN2.off()
    IN4.off()

    pwm1.freq(800)
    pwm2.freq(800)

    pwm1.duty_u16(int(65536 * left_speed))
    pwm2.duty_u16(int(65536 * right_speed))

    IN1.on()
    IN4.on()
    time.sleep(0.2)
    IN1.off()
    IN4.off()


def drive_Right(left_speed, right_speed):
    IN1.off()
    IN3.off()
    IN2.off()
    IN4.off()

    pwm1.freq(800)
    pwm2.freq(800)

    pwm1.duty_u16(int(65536 * left_speed))
    pwm2.duty_u16(int(65536 * right_speed))

    IN2.on()
    IN3.on()
    time.sleep(0.2)
    IN2.off()
    IN3.off()


def drive_Backward(left_speed, right_speed):
    IN1.off()
    IN3.off()
    IN2.off()
    IN4.off()

    pwm1.freq(800)
    pwm2.freq(800)

    pwm1.duty_u16(int(65536 * left_speed))
    pwm2.duty_u16(int(65536 * right_speed))

    IN1.on()
    IN3.on()
    time.sleep(0.2)
    IN1.off()
    IN3.off()


# Motor for Remote Control Mode — SLUT






# Motor for Sumo Mode — START


def sumo_drive_Backward(left_speed, right_speed):
    IN1.off()
    IN3.off()
    IN2.off()
    IN4.off()

    pwm1.freq(800)
    pwm2.freq(800)

    pwm1.duty_u16(int(65536 * left_speed))
    pwm2.duty_u16(int(65536 * right_speed))

    IN1.on()
    IN3.on()
    time.sleep(3.5)
    IN1.off()
    IN3.off()


def sumo_drive_Right(left_speed, right_speed):
    IN1.off()
    IN3.off()
    IN2.off()
    IN4.off()

    pwm1.freq(800)
    pwm2.freq(800)

    pwm1.duty_u16(int(65536 * left_speed))
    pwm2.duty_u16(int(65536 * right_speed))

    IN2.on()
    IN3.on()
    time.sleep(1)
    IN2.off()
    IN3.off()


def sumo_drive_Left(left_speed, right_speed):
    IN1.off()
    IN3.off()
    IN2.off()
    IN4.off()

    pwm1.freq(800)
    pwm2.freq(800)

    pwm1.duty_u16(int(65536 * left_speed))
    pwm2.duty_u16(int(65536 * right_speed))

    IN2.on()
    IN3.on()
    time.sleep(0.8)
    IN2.off()
    IN3.off()


# Sumo Mode Scanning — Start

def scan_All(left_speed, right_speed):
    IN1.off()
    IN3.off()
    IN2.off()
    IN4.off()

    pwm1.freq(800)
    pwm2.freq(800)

    pwm1.duty_u16(int(65536 * left_speed))
    pwm2.duty_u16(int(65536 * right_speed))

    IN2.on()
    IN3.on()
    time.sleep(0.5)
    IN2.off()
    IN3.off()


def scan_Left(left_speed, right_speed):
    IN1.off()
    IN3.off()
    IN2.off()
    IN4.off()

    pwm1.freq(800)
    pwm2.freq(800)

    pwm1.duty_u16(int(65536 * left_speed))
    pwm2.duty_u16(int(65536 * right_speed))

    IN2.on()
    IN3.on()

    time.sleep(0.2)
    
    IN2.off()
    IN3.off()


def scan_Right(left_speed, right_speed):
    IN1.off()
    IN3.off()
    IN2.off()
    IN4.off()

    pwm1.freq(800)
    pwm2.freq(800)

    pwm1.duty_u16(int(65536 * left_speed))
    pwm2.duty_u16(int(65536 * right_speed))

    IN2.on()
    IN3.on()

    time.sleep(0.2)

    IN2.off()
    IN3.off()


def sumo_Drive_Forward(left_speed, right_speed):
    IN1.off()
    IN3.off()
    IN2.off()
    IN4.off()

    pwm1.freq(800)
    pwm2.freq(800)

    pwm1.duty_u16(int(65536 * left_speed))
    pwm2.duty_u16(int(65536 * right_speed))

    IN2.on()
    IN4.on()
    time.sleep(2)
    IN1.off()
    IN3.off()


# Motor for Sumo Mode — SLUT