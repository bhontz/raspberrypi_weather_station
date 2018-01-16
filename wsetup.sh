#!/bin/bash
sudo apt-get update
sudo apt-get install -y build-essential python-dev
sudo apt-get install -y lighthttp
sudo chown www-data:www-data /var/www
sudo chmod 775 /var/www
sudo usermod -a -G www-data pi
https://github.com/bhontz/raspberrypi_weather_station/blob/master/my_weather_station.py
mv my_weather_station.py /var/www
https://github.com/adafruit/Adafruit_Python_DHT/archive/master.zip
unzip Adafruit_Python_DHT-master
cd Adafruit_Python_DHT
sudo python setup.py install