# Program to interface Servo motor to rotate based on Sensor/switch status 
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(19, GPIO.OUT)

p = GPIO.PWM(19, 50)

p.start(7.5)
try:
    while True:
        input_state_1 = GPIO.input(26)
        input_state_2 = GPIO.input(22)
        if input_state_1 == False:
            print('Button Pressed')
            while True:
                p.ChangeDutyCycle(7.5)  # turn towards 90 degree
                time.sleep(0.2) # sleep 1 second
                p.ChangeDutyCycle(2.5)  # turn towards 0 degree
                time.sleep(0.2) # sleep 1 second
                p.ChangeDutyCycle(12.5) # turn towards 180 degree
                time.sleep(0.2) # sleep 1 second 
                time.sleep(0.2)
                if (input_state_2 == False):
                    print('stopped')
                    #p.stop()
                    GPIO.cleanup()
except KeyboardInterrupt:
    #p.stop()
    GPIO.cleanup()