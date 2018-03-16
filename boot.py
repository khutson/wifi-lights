# This file is executed on every boot (including wake-boot from deepsleep)
import esp
esp.osdebug(None)

import network
import time

def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('tsati', 'hutonetwo')
        curtime = time.time()
        while not sta_if.isconnected() and (time.time()-curtime)<30 :
            pass
    print('network config:', sta_if.ifconfig())

do_connect()
time.sleep(4)

#import webrepl
#webrepl.start(password='micropython')

import gc
gc.collect()

import httpneo
httpneo.run()