# piStatus
 Raspberry Pi Status Monitor with SSD1306 128x32 OLED 

![prototype scheme](https://github.com/maltsevvv/server/pi_status_oled/raw/main/icon/oled128x32.png)

**HOW TO USE IT**

Enable I2C from Raspberry Configuration and Reboot your RPI.

    sudo raspi-config

Install modules

    sudo apt-get install -y git python3-pip python3-pil i2c-tools
    sudo pip3 install adafruit-circuitpython-ssd1306

Find I2C

    sudo i2cdetect -y 1
	
Clone it from github.

    cd ~
    git clone https://github.com/maltsevvv/server/pi_status_oled.git

Run the code

    sudo python3 /usr/local/bin/pi_status_oled/pistatus.py

If you want it start on Raspberry Pi Startup you must do that.
Open terminal.

    sudo nano /etc/rc.local

Add this line before exit 0

    sudo python3 /usr/local/bin/pi_status_oled/pistatus.py &

Save and reboot your RPI.
