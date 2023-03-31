#!/usr/bin/env python3
import RPi.GPIO as GPIO
from time import sleep
# 5, 6, 13, 19
def test():
 GPIO.setmode(GPIO.BCM)
 GPIO.setup(5, GPIO.OUT)
 GPIO.setup(6, GPIO.OUT)
 GPIO.setup(13, GPIO.OUT)
 GPIO.setup(19, GPIO.OUT)
 pwm_v = GPIO.PWM(13, 100)
 pwm_h = GPIO.PWM(6, 100)
 pwm_v.start(25)
 pwm_h.start(25)
 while True:
 pass
def main():
 try:
 test()
 except KeyboardInterrupt:
 print("\nStopped by user")
 finally:
 GPIO.cleanup()


if __name__ == '__main__':
 main()
