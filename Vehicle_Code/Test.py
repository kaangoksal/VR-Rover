import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

LeftWheel_A = 17
LeftWheel_B = 23

RightWheel_A = 27
RightWheel_B = 22

PWM_Frequency = 490

# Left wheels
GPIO.setup(LeftWheel_A, GPIO.OUT)
GPIO.setup(LeftWheel_B, GPIO.OUT)

# Right wheels
GPIO.setup(RightWheel_A, GPIO.OUT)
GPIO.setup(RightWheel_B, GPIO.OUT)

pwmLeftA = GPIO.PWM(LeftWheel_A, PWM_Frequency)
pwmLeftB = GPIO.PWM(LeftWheel_B, PWM_Frequency)

pwmRightA = GPIO.PWM(RightWheel_A, PWM_Frequency)
pwmRightB = GPIO.PWM(RightWheel_B, PWM_Frequency)

pwmLeftA.start(0)
pwmLeftB.start(0)
pwmRightA.start(0)
pwmRightB.start(0)


def leftWheelset(thr):
    if thr > 0:
        pwmLeftB.ChangeDutyCycle(0)
        pwmLeftA.ChangeDutyCycle(thr)
    elif thr < 0:
        thr = abs(thr)
        pwmLeftA.ChangeDutyCycle(0)
        pwmLeftB.ChangeDutyCycle(thr)
    else:
        pwmLeftB.ChangeDutyCycle(100)
        pwmLeftB.ChangeDutyCycle(100)


def rightWheelset(thr):
    if thr > 0:
        pwmRightB.ChangeDutyCycle(0)
        pwmRightA.ChangeDutyCycle(thr)
    elif thr < 0:
        thr = abs(thr)
        pwmRightA.ChangeDutyCycle(0)
        pwmRightB.ChangeDutyCycle(thr)
    else:
        pwmRightB.ChangeDutyCycle(100)
        pwmRightB.ChangeDutyCycle(100)


def reset():
    GPIO.cleanup()


leftWheelset(50)
rightWheelset(50)
sleep(2)
leftWheelset(-50)
rightWheelset(-50)
sleep(2)
leftWheelset(0)
rightWheelset(0)
