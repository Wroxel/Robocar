from machine import Pin, PWM
import time
import sensors

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

    pwm1.freq(500)
    pwm2.freq(500)

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
    time.sleep(2)
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

    global left_steps
    left_steps = 0

    time.sleep(0.1)

    left_steps += 1
    print("Lefts steps:", left_steps)

    IN2.off()
    IN3.off()

    return left_steps


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
    global right_steps
    right_steps = 0

    time.sleep(0.1)

    right_steps += 1
    print("Right steps:", right_steps)
    IN2.off()
    IN3.off()
    return right_steps


def scan_Middle():
    scan_Sum = left_steps + right_steps
    scan_Average = scan_Sum / 2
    print("Gennemsnit af steps:", scan_Average)

    while True:
        scan_Left(0.30, 0.35)

        if scan_Left == scan_Average:
            break


# Motor for Sumo Mode — SLUT
