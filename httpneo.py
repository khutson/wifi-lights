import socket 
import machine
from neopixel import NeoPixel
import time

#HTML to send to browsers
html = """<!DOCTYPE html>
<html>
<head> <title>ESP8266 LED ON/OFF</title> </head>
<center><h2>A simple webserver for changing neopixels with Micropython</h2></center>
<form>
Color: 
<button name="color" value="red" type="submit">Red</button>
<button name="color" value="blue" type="submit">Blue</button><br><br>
<br>
Command:
<button name="cmd" value="cycle" type="submit">Cycle</button>

</form>
</html>
"""

#Setup PINS

pin=machine.Pin(15,machine.Pin.OUT)
np=NeoPixel(pin,30)

#Setup Socket WebServer
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
# xxx need to catch kill to clean up after interrupt

def run():
    print("Waiting for connection...")
    while True:
        conn, addr = s.accept()
        print("Got a connection from %s" % str(addr))
        request = conn.recv(1024)
        print("Content = %s" % str(request))
        request = str(request)
        if request.find('/?color=red') >=0:
            np.fill((255,0,0))
            np.write()
        elif request.find('/?color=blue') >=0:
            np.fill((0,0,255))
            np.write()
        elif request.find('/?cmd=cycle') >=0:
            n=np.n
            for i in range(4 * n):
                np.fill((0,0,0))
                np[i % n] = (255, 255, 255)
                np.write()
                time.sleep_ms(25)
            np.fill((0,0,0))
            np.write()


        response = html
        conn.send(response)
        conn.close()