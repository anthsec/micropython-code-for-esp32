'''
Description: This is a demo for ESP32 using SSD1306 OLED
Screen Model: SSD1306 OLED
Libwiki: https://github.com/stlehmann/micropython-ssd1306
Lib_Author:stlehmann@github
Author: Anthsec@github
'''

import machine
from ssd1306 import SSD1306_I2C
#i2c.scan() #It's not necessary
i2c = machine.I2C(sda=machine.Pin(8), scl=machine.Pin(7))
oled = SSD1306_I2C(128, 64, i2c) #(width, height, I2C_Object)
oled.fill(0) #(0-black,1-white)
oled.text('Hello World', 0, 0) #(Text, x, y)
oled.show()