# Fan Control
#Raspberry Pi PWM Fan Control 

# ![prototype scheme](https://github.com/maltsevvv/server/raw/main/fan_control/img/rpi-pwm-fan-3d.png)

**HOW TO USE IT**

#Клонируем из github.
    git clone https://github.com/maltsevvv/server.git
    
#Копируем каталог PI_Status_OLED в /usr/local/bin/

    sudo cp -r /home/pi/server/fan_control /usr/local/bin/

#Копируем service для автоматического запуска

    sudo cp /usr/local/bin/fan_control/fan_control.service /etc/systemd/system/

#Запускаем fan_ctrl.service

    sudo systemctl enable fan_control.service
    sudo systemctl start fan_control.service
