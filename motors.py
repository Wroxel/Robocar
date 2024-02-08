from machine import Pin, PWM
import time

IN1 = Pin(2, Pin.OUT)
IN2 = Pin(3, Pin.OUT)

IN3 = Pin(4, Pin.OUT)
IN4 = Pin(5, Pin.OUT)


def drive():

    IN1.off()
    IN3.off()
    IN2.off()
    IN4.off()
    print("Stopping")

    while True:
        IN1.on()
        IN3.on()
        time.sleep(2)
        IN1.off()
        IN3.off()
        time.sleep(2)
        IN1.on()
        IN3.on()
        time.sleep(2)
        IN1.off()
        IN3.off()
        time.sleep(2)
        IN2.on()
        IN4.on()
        time.sleep(2)
        IN2.off()
        IN4.off()
        time.sleep(2)
        break


def stopDrive():
    IN1.off()
    IN3.off()
    IN2.off()
    IN4.off()


def drivePWM():
    pwm1 = PWM(Pin(6))
    pwm2 = PWM(Pin(7))

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
        time.sleep(5)
        IN3.on()
        IN2.on()
        pwm1.duty_u16(int(65536 * dutycycle1))
        pwm2.duty_u16(int(65536 * dutycycle2))
        time.sleep(5)
        IN3.off()
        IN2.off()
        time.sleep(0.5)
        IN4.on()
        IN1.on()
        # pwm1.duty_u16(int(65536 * dutycycle1))
        # pwm2.duty_u16(int(65536 * dutycycle2))
        time.sleep(5)
        IN4.off()
        IN1.off()
        time.sleep(0.5)
        IN1.on()
        IN3.on()
        # pwm1.duty_u16(int(65536 * dutycycle1))
        # pwm2.duty_u16(int(65536 * dutycycle2))
        time.sleep(5)
        IN1.off()
        IN3.off()
        break
    stopDrive()

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

    # a = 0
    # for i in range(20):
    #     IN2.on()
    #     pwm1.freq(2000)
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
    #     print(a)
    #     a += 1

    # IN2.off()

    # for i in range(20):
    #     IN3.on()
    #     pwm2.freq(20)
    #     pwm2.duty_u16(int(65536 * dutycycle))
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

    # IN3.off()

    # a = 0
    # for i in range(40):
    #     IN4.on()
    #     pwm2.freq(2000)
    #     pwm2.duty_u16(int(65536 * dutycycle))
    #     time.sleep(0.2)
    #     if upwards:
    #         dutycycle = dutycycle + 0.03
    #         if dutycycle >= 0.9:
    #             upwards = False
    #     else:
    #         dutycycle = dutycycle - 0.03
    #         if dutycycle <= 0.2:
    #             upwards = True
    #     print(a)
    #     a += 1

    # IN4.off()
