# Оповещение об ошибках состояния systemd в Telegram

**Автоустановка**

    sudo apt install git
    git clone https://github.com/maltsevvv/server.git
    sudo chmod +x /home/pi/server/telegram-notifier/README.md
    sudo /home/pi/server/telegram-notifier/README.md
    
**Ручная установка**

    sudo apt install git
    git clone https://github.com/maltsevvv/server.git
    sudo cp /home/pi/server/telegram-notifier/telegram /usr/bin/
    sudo chmod +x /usr/bin/telegram

#Вводим наши данные для Telegram BOT

    sudo nano /home/pi/server/telegram-notifier/key.sh
    sudo mkdir /etc/telegram/
    sudo cp /home/pi/server/telegram-notifier/key.sh /etc/telegram/

#Отправка тестового сообщения в Ваш BOT

    telegram "Test Message"

#Cообщить о статусе модуля systemd

    sudo cp /home/pi/server/telegram-notifier/unit-status-telegram /usr/bin/
    sudo chmod +x /usr/bin/unit-status-telegram

#Отправка тестового сообщения от systemd в Ваш BOT

    unit-status-telegram systemd-journald

#Добавить unit-status-telegram@.serivce в systemd

    sudo cp /home/pi/server/telegram-notifier/unit-status-telegram@.serivce /etc/systemd/system/


#**Для отслеживания сервисов systemd, необходимо добавить OnFailure=unit-status-telegram@%n.service в раздел [Unit]**

#[Unit]  
#OnFailure=unit-status-telegram@%n.service
