# Добавить кнопку перезагрузки. Подключаемя к 37pin и 39pin
#Кнопку подключаем к GPIO 26 на Raspberry

**HOW TO USE IT**

#Копируем reboot.py в /usr/local/bin/

    sudo cp server/button_reboot/reboot.py /usr/local/bin/

#Копируем service для автозапуска

    sudo cp server/button_reboot/reboot.service /etc/systemd/system/

#Запускаем pistatus.service

    sudo systemctl enable reboot.service
    sudo systemctl start reboot.service
