'''
Description: This is a demo for ESP32 using Remote Receiver
Sensor Model: HS0038 Remote
Libwiki: https://github.com/karlcarlo/irRemote_esp32/
Lib_Author:karlcarlo@github
Author: Anthsec@github
'''

from IRremote import IrReceiver
import time


receiver = IrReceiver(7) #HS0038

while True:
    if receiver.decode():
        print(receiver.decodedData)
