#Program to display image on OLED
import time
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
RST=24
disp=Adafruit_SSD1306.SSD1306_128_64(rst=RST,i2c_address=0x3c)
disp.begin()
disp.clear()
disp.display()
width=disp.width
height=disp.height
image=Image.open('/home/pi/Pictures/terminator.jpg').resize((width,height),Image.ANTIALIAS).convert('1')
disp.image(image)
disp.display()
time.sleep(1)