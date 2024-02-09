from machine import Pin, PWM
import time

# Højre motor
IN1 = Pin(2, Pin.OUT)
IN2 = Pin(3, Pin.OUT)

# Venstre motor
IN3 = Pin(4, Pin.OUT)
IN4 = Pin(5, Pin.OUT)


def stopDrive():
    IN1.off()
    IN3.off()
    IN2.off()
    IN4.off()


def drivePWM():
    pwm1 = PWM(Pin(6))
    pwm2 = PWM(Pin(7))

    # Kode der gøre at motorene køre men en bestemt hastighed hele tiden.

    pwm1.freq(500)
    pwm2.freq(500)

    dutycycle1 = 0.35
    dutycycle2 = 0.35
    upwards = True

    while True:
        time.sleep(3)
        IN3.off()
        IN2.off()
        IN4.off()
        IN1.off()
        time.sleep(3)
        IN3.on()
        IN2.on()
        pwm1.duty_u16(int(65536 * dutycycle1))
        pwm2.duty_u16(int(65536 * dutycycle2))
        time.sleep(3)
        IN3.off()
        IN2.off()
        time.sleep(0.5)
        IN4.on()
        IN1.on()
        time.sleep(3)
        IN4.off()
        IN1.off()
        time.sleep(0.5)
        IN1.on()
        IN3.on()
        time.sleep(3)
        IN1.off()
        IN3.off()
        break
    stopDrive()

    # Kode der gøre motoren køre hurtigere og hurtigere.

    # i = 0

    # for i in range(40):
    #     IN1.on()
    #     pwm1.freq(20)
    #     pwm1.duty_u16(int(65536 * dutycycle))
    #     time.sleep(0.2)
    #     if upwards:
    #         dutycycle = dutycycle + 0.03
    #         if dutycycle >= 0.9:
    #             upwards = False
    #     else:
    #         dutycycle = dutycycle - 0.03
    #         if dutycycle <= 0.2:
    #             upwards = True
    #     print(i)
    #     i += 1

    # IN1.off()
