#!/usr/bin/env python
import re
import time
import busio
import subprocess
from threading import Timer
from board import SCL, SDA
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

i2c = busio.I2C(SCL, SDA)

disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

disp.fill(0)
disp.show()

width = disp.width
height = disp.height
image = Image.new("1", (width, height))

draw = ImageDraw.Draw(image)
draw.rectangle((0,0,width,height), outline=0, fill=0)
#draw.rectangle((0, 0, width, height), outline=0, fill=0)

padding = -5
top = padding
bottom = height - padding
x = 0

# Load default font.
font = ImageFont.truetype('/usr/local/bin/pistatus/icon/Ubuntu-R.ttf', 18)

# Variables
cpu_temp = 0
date_text = "01.01.1970"
time_text = "00.00.00"
hdd1_free = 0
hdd1_percent = 0
hdd2_free = 0
hdd2_percent = 0
screen_no = -1

def get_date_time():
    global date_text
    global time_text
    cmd = "date +%H:%M"
    time_text = subprocess.check_output(cmd, shell = True).decode("utf-8")
    cmd = "date +%d-%m-%Y"
    date_text = subprocess.check_output(cmd, shell = True).decode("utf-8")
    t = Timer(10, get_date_time)
    t.start()
get_date_time()

def get_hdd():
    global hdd1_free
    global hdd1_percent
    global hdd2_free
    global hdd2_percent
    cmd = "df -h | awk '$NF==\"/mnt/hdd\"{printf \"HDD1:  %s\", $5}'"
    hdd1_percent = subprocess.check_output(cmd, shell = True).decode("utf-8")
    cmd = "df -h | awk '$NF==\"/mnt/hdd\"{printf \"FREE: %sB\", $4}'"
    hdd1_free = subprocess.check_output(cmd, shell = True).decode("utf-8")
    cmd = "df -h | awk '$NF==\"/mnt/hdd2\"{printf \"HDD2:  %s\", $5}'"
    hdd2_percent = subprocess.check_output(cmd, shell = True).decode("utf-8")
    cmd = "df -h | awk '$NF==\"/mnt/hdd2\"{printf \"FREE: %sB\", $4}'"
    hdd2_free = subprocess.check_output(cmd, shell = True).decode("utf-8")
    t = Timer(2, get_hdd)
    t.start()
get_hdd()

def get_cpu_temp():
    global cpu_temp
    cmd = "vcgencmd measure_temp"
    cpu_temp = subprocess.check_output(cmd, shell=True).decode("utf8")
    #return float(re.findall(r'\d+\.\d+', cpu_temp)[0])
    t = Timer(5, get_cpu_temp)
    t.start()
get_cpu_temp()

def raise_screen_no():
    global screen_no
    screen_no += 1
    if screen_no > 5:
        screen_no = 0
    t = Timer(4, raise_screen_no)
    t.start()
raise_screen_no()

while True:
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    if screen_no == 1: #cpu°C
        image = Image.open("/usr/local/bin/pistatus/icon/temperature.bmp").convert("1")
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('/usr/local/bin/pistatus/icon/Ubuntu-R.ttf', 30)
        draw.text((x, top+5),       str(cpu_temp[5:9]+'°C'),   font=font, fill=255)

    elif screen_no == 2: #hdd1 /dev/sda
        image = Image.open("/usr/local/bin/pistatus/icon/disk.bmp").convert("1")
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('/usr/local/bin/pistatus/icon/Ubuntu-R.ttf', 18)
        draw.text((x, top),       str(hdd1_percent),   font=font, fill=255)
        draw.text((x, top+20),    str(hdd1_free),      font=font, fill=255)

    elif screen_no == 3: #hdd2 /dev/sdb
        image = Image.open("/usr/local/bin/pistatus/icon/disk.bmp").convert("1")
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('/usr/local/bin/pistatus/icon//Ubuntu-R.ttf', 18)
        draw.text((x, top),       str(hdd2_percent),   font=font, fill=255)
        draw.text((x, top+20),    str(hdd2_free),      font=font, fill=255)

    else: #time
        font = ImageFont.truetype('/usr/local/bin/pistatus/icon/Ubuntu-R.ttf', 39)
        draw.text((x, top),       str(time_text),      font=font, fill=255)

    # Display image.
    disp.image(image)
    disp.show()
    time.sleep(1)
