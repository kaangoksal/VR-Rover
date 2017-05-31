import abc
import RPi.GPIO as GPIO


class rp_wheel(object):
    def __init__(self, A, B, PWM_Freq):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
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
            print("forward")
            # self.pwmB.ChangeDutyCycle(0)
            # self.pwmA.ChangeDutyCycle(thr)
            self.pwmB.start(0)
            self.pwmA.start(thr)
        elif thr < 0:
            print("reverse")
            thr = abs(thr)
            # self.pwmA.ChangeDutyCycle(0)
            # self.pwmB.ChangeDutyCycle(thr)
            self.pwmA.start(0)
            self.pwmB.start(thr)
        else:
            print("stop")
            self.pwmA.ChangeDutyCycle(0)
            self.pwmB.ChangeDutyCycle(0)
            # self.pwmA.stop()
            # self.pwmB.stop()
            # GPIO.output(self.pinA, GPIO.LOW)
            # GPIO.output(self.pinB, GPIO.LOW)