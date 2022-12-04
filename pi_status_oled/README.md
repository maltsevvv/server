# piStatus
#Raspberry Pi Status Monitor with SSD1306 128x32 OLED 

# ![prototype scheme](https://github.com/maltsevvv/server/pi_status_oled/raw/main/icon/oled128x32.png)

# ![prototype scheme](https://github.com/maltsevvv/server/raw/main/pi_status_oled/icon/oled128x32.png)

**HOW TO USE IT**

#Включаем I2C интерфейс на Raspberry

    sudo raspi-config

#Устанавливаем необходимые модули

    sudo apt-get install -y git python3-pip python3-pil i2c-tools
    sudo pip3 install adafruit-circuitpython-ssd1306

#Проверяем опридиление I2C 

    sudo i2cdetect -y 1
	
#Клонируем из github.

    git clone https://github.com/maltsevvv/server.git
    
#Копируем каталог PI_Status_OLED в /usr/local/bin/

    sudo cp -r server/pi_status_oled /usr/local/bin/

#Запустить

    sudo python3 /usr/local/bin/pi_status_oled/pistatus.py

#Создаем service для автоматического запуска

    sudo nano /etc/systemd/system/pistatus.service
    
    [Unit]
    Description=RPI status on OLED i2c
    [Service]
    Type=simple
    ExecStart=/usr/bin/python /usr/local/bin/pi_status_oled/pistatus.py
    Restart=always
    [Install]
    WantedBy=multi-user.target
    
#Запускаем pistatus.service

    sudo systemctl enable pistatus.service
    sudo systemctl start pistatus.service