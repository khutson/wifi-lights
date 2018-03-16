# wifi-lights
Manitou Art Center lightning project to make wi-fi controllable lights

Notes
To connect to ESP8266:
screen /dev/ttyUSB0 115200

To install micropython:
esptool.py --port /dev/ttyUSB0 erase_flash

esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect -fm dio 0 esp8266-20171101-v1.9.3.bin 
