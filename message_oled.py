#Program to display a message on specified Line &amp; Position of OLED Display.
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
image=Image.new('1',(width,height))
draw=ImageDraw.Draw(image)
draw.rectangle((0,0,width,height),outline=0,fill=0)
padding=0
top=padding
x=padding
font=ImageFont.load_default()
draw.text((x,top),'Initializing',font=font,fill=1)
draw.text((x,top+20),'GO Pikachu!!',font=font,fill=1)
disp.image(image)
disp.display()
time.sleep(10)