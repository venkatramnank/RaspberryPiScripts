#Program to Read status of Switch, Operate LED/Relay/Buzzer&amp; Display the status of switch on
#OLED.
import RPi.GPIO as GPIO
import time
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
RST=24
disp=Adafruit_SSD1306.SSD1306_128_64(rst=RST,i2c_address=0x3c)
GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23
GPIO.setup(24, GPIO.OUT)  #LED to GPIO24
def oled_status(status):
    disp.begin()
    disp.clear()
    disp.display()
    width=disp.width
    height=disp.height
    image=Image.new('1',(width,height))
    draw=ImageDraw.Draw(image)
    draw.rectangle((0,0,width,height),outline=0,fill=0)
    padding=0
    top=padding
    x=padding
    font=ImageFont.load_default()
    draw.text((x,top),status,font=font,fill=1)
    disp.image(image)
    disp.display()
    time.sleep(0.2)
    disp.clear()
    disp.display()   

try:
    while True:
         button_state = GPIO.input(23)
         if button_state == False:
             GPIO.output(24, True)
             print('Button Pressed...')
             oled_status('LED ON')
             time.sleep(0.2)
         
         elif button_state == True:
             #oled_status('LED OFF')
             GPIO.output(24, False)
except:
    GPIO.cleanup()