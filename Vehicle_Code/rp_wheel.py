import abc
import RPi.GPIO as GPIO
from Wheel import Wheel

class rp_wheel(Wheel):
    def __init__(self, A, B, PWM_Freq):
        self.pinA = A
        self.pinB = B
        self.PWM_Freq = PWM_Freq

        GPIO.setup(self.pinA, GPIO.OUT)
        GPIO.setup(self.pinB, GPIO.OUT)

        self.pwmA = GPIO.PWM(self.pinA, self.PWM_Freq)
        self.pwmB = GPIO.PWM(self.pinB, self.PWM_Freq)

        self.pwmA.start(0)
        self.pwmB.start(0)

    def setspeed(self, thr):
        if thr > 0:
            self.pwmB.ChangeDutyCycle(0)
            self.pwmA.ChangeDutyCycle(thr)
        elif thr < 0:
            thr = abs(thr)
            self.pwmA.ChangeDutyCycle(0)
            self.pwmB.ChangeDutyCycle(thr)
        else:
            self.pwmB.ChangeDutyCycle(100)
            self.pwmB.ChangeDutyCycle(100)