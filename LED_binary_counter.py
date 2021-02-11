# LED Binary counter 
# counter.py
import RPi.GPIO as GPIO
import time
#220 ohm resistors

print "=== Binary counter ==="

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) # access pins by their numbers	

# Configure 8 pins to output mode
GPIO.setup(33, GPIO.OUT) # pin 33 for bit 0
GPIO.setup(37, GPIO.OUT) # pin 37 for bit 1
GPIO.setup(7,  GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT) # pin 21 for bit 7

cnt = 0
print("Press Ctrl-C to exit")

try:
	while True:
		GPIO.output(33, cnt & 0x01) # set bit 0
		GPIO.output(37, cnt & 0x02) 
		GPIO.output(7,  cnt & 0x04)
		GPIO.output(11, cnt & 0x08)
		GPIO.output(13, cnt & 0x10)
		GPIO.output(15, cnt & 0x20)
		GPIO.output(19, cnt & 0x40)
		GPIO.output(21, cnt & 0x80) # set bit 7
		time.sleep(0.1)             # wait 100 msec
		cnt += 1 %  256				# increment counter up to 255, then reset to 0

except KeyboardInterrupt:
	GPIO.cleanup()
