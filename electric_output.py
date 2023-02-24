import RPi.GPIO as GPIO
from time import sleep

led_pin = 17 #define which pin you want power to

GPIO.setmode(GPIO.BCM) #Set mode to BCM, alternative -> Board

GPIO.setup(led_pin, GPIO.OUT) #setup the pin

button_state = GPIO.input(button_pin) #Returner 0 eller 1

print(button_state) #if 1 then on

pwm_blink = GPIO.PWM(led_pin, 0.0) #arguement for GPIO.PWM(channel, frequency)
#want to change frequency? pwm_blink.ChangeFrequency(frequency)

pwm_blink.start(50) #.start(duty_cycle)

pwm_blink.stop()

#want to brighten/dim a light?

for dc in range(0,101):
  pwm_blink.ChangeDutyCycle(dc)
  time.sleep(0.01)
for dc in range(101,0,-1):
  pwm_blink.ChangeDutyCycle(dc)
  time.sleep(0.01)

GPIO.output(led_pin, GPIO.HIGH)

sleep(1)

GPIO.output(led_pin, GPIO.LOW)

GPIO.cleanup()
