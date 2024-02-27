from machine import Pin, PWM
import time

# Venstre motor
IN1 = Pin(2, Pin.OUT)  # venstre hjul bagud
IN2 = Pin(3, Pin.OUT)  # venstre hjul fremad

# Højre motor
IN3 = Pin(4, Pin.OUT)  # Højre hjul bagud
IN4 = Pin(5, Pin.OUT)  # højre hjul fremad


# PWM pins
pwm1 = PWM(Pin(6))
pwm2 = PWM(Pin(7))
pwm1.freq(700)
pwm2.freq(700)

LEFT = 0
RIGHT = 1


# Sætter PWM speed
def setSpeed(motor, speed):
    if motor == 0:
        pwm1.duty_u16(int(65536 * speed))
    else:
        pwm2.duty_u16(int(65536 * speed))


# Stopper med at køre
def stopDrive():
    IN1.off()
    IN3.off()
    IN2.off()
    IN4.off()


# Motor for Wall Follow Mode — START


def wall_straight_Drive(left_speed, right_speed):
    stopDrive()

    setSpeed(LEFT, left_speed)
    setSpeed(RIGHT, right_speed)

    IN2.on()
    IN4.on()
    time.sleep(0.028)
    IN2.off()
    IN4.off()


def wall_gone_cont(left_speed, right_speed):
    stopDrive()

    setSpeed(LEFT, left_speed)
    setSpeed(RIGHT, right_speed)

    IN2.on()
    IN4.on()
    time.sleep(0.1)
    IN2.off()
    IN4.off()


def wall_left_Drive(left_speed, right_speed):
    stopDrive()

    setSpeed(LEFT, left_speed)
    setSpeed(RIGHT, right_speed)

    IN2.on()
    IN4.on()
    time.sleep(0.1)
    IN2.off()
    IN4.off()


def wall_drive_Right(left_speed, right_speed):
    stopDrive()

    setSpeed(LEFT, left_speed)
    setSpeed(RIGHT, right_speed)

    IN2.on()
    IN4.on()
    time.sleep(0.2)
    IN2.off()
    IN4.off()


def wall_look_right(left_speed, right_speed):
    stopDrive()

    setSpeed(LEFT, left_speed)
    setSpeed(RIGHT, right_speed)

    IN2.on()
    IN3.on()

    time.sleep(0.4)

    IN2.off()
    IN3.off()


def wall_look_left(left_speed, right_speed):
    stopDrive()

    setSpeed(LEFT, left_speed)
    setSpeed(RIGHT, right_speed)

    IN1.on()
    IN4.on()

    time.sleep(0.4)

    IN1.off()
    IN4.off()


# Motor for Wall Follow Mode — SLUT


# Motor for Remote Control Mode — START


def drive_Forward(left_speed, right_speed):
    stopDrive()

    setSpeed(LEFT, left_speed)
    setSpeed(RIGHT, right_speed)

    IN2.on()
    IN4.on()
    time.sleep(0.2)
    IN2.off()
    IN4.off()


def drive_Left(left_speed, right_speed):
    stopDrive()

    setSpeed(LEFT, left_speed)
    setSpeed(RIGHT, right_speed)

    IN1.on()
    IN4.on()
    time.sleep(0.2)
    IN1.off()
    IN4.off()


def drive_Right(left_speed, right_speed):
    stopDrive()

    setSpeed(LEFT, left_speed)
    setSpeed(RIGHT, right_speed)

    IN2.on()
    IN3.on()
    time.sleep(0.2)
    IN2.off()
    IN3.off()


def drive_Backward(left_speed, right_speed):
    stopDrive()

    setSpeed(LEFT, left_speed)
    setSpeed(RIGHT, right_speed)

    IN1.on()
    IN3.on()
    time.sleep(0.2)
    IN1.off()
    IN3.off()


# Motor for Remote Control Mode — SLUT


# Motor for Sumo Mode — START


def sumo_Drive_Forward(left_speed, right_speed):
    stopDrive()

    setSpeed(LEFT, left_speed)
    setSpeed(RIGHT, right_speed)

    IN2.on()
    IN4.on()
    time.sleep(0.065)
    IN2.off()
    IN4.off()


def sumo_drive_Backward(left_speed, right_speed):
    stopDrive()

    setSpeed(LEFT, left_speed)
    setSpeed(RIGHT, right_speed)

    IN1.on()
    IN3.on()

    time.sleep(1)

    IN1.off()
    IN3.off()


def sumo_drive_Right(left_speed, right_speed):
    stopDrive()

    setSpeed(LEFT, left_speed)
    setSpeed(RIGHT, right_speed)

    IN2.on()
    IN3.on()
    time.sleep(0.5)
    IN2.off()
    IN3.off()


# Sumo Mode Scanning — Start


def scan_All(left_speed, right_speed):
    stopDrive()

    setSpeed(LEFT, left_speed)
    setSpeed(RIGHT, right_speed)

    IN2.on()
    IN3.on()

    time.sleep(0.045)

    IN2.off()
    IN3.off()


def scan_Right(left_speed, right_speed):
    stopDrive()

    setSpeed(LEFT, left_speed)
    setSpeed(RIGHT, right_speed)

    IN2.on()
    IN3.on()

    time.sleep(0.1)

    IN2.off()
    IN3.off()


def scan_Left(left_speed, right_speed):
    stopDrive()

    setSpeed(LEFT, left_speed)
    setSpeed(RIGHT, right_speed)

    IN1.on()
    IN4.on()

    time.sleep(0.1)

    IN1.off()
    IN4.off()


# Sumo Mode Scanning — Slut
