try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!")
import time

servoPIN = 13

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)
    p = GPIO.PWM(servoPIN, 50)  # GPIO PIN for PWM with 50Hz
    return p

def right(p):
    try:
        p.ChangeDutyCycle(2.5)
        time.sleep(0.5)
    except KeyboardInterrupt:
        GPIO.cleanup()


def center(p):
    try:
        p.ChangeDutyCycle(2.5)
        time.sleep(0.5)
    except KeyboardInterrupt:
        GPIO.cleanup()


def left(p):
    try:
        p.ChangeDutyCycle(2.5)
        time.sleep(0.5)
    except KeyboardInterrupt:
        GPIO.cleanup()


def __correr(p):
    try:
        while True:
            p.ChangeDutyCycle(2.5)
            time.sleep(0.5)
            p.ChangeDutyCycle(7.5)
            time.sleep(0.5)
            p.ChangeDutyCycle(10)
            time.sleep(0.5)
            p.ChangeDutyCycle(12.5)
            time.sleep(0.5)
            p.ChangeDutyCycle(10)
            time.sleep(0.5)
            p.ChangeDutyCycle(7.5)
            time.sleep(0.5)
            p.ChangeDutyCycle(5)
            time.sleep(0.5)
            p.ChangeDutyCycle(2.5)
            time.sleep(0.5)
    except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()
