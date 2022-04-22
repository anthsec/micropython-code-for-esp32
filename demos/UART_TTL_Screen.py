'''
Description: This is a demo for ESP32 using UART TTL Screen
Screen Model: TJC4832T135_011N/R/C TJC4832T135_011N/R_Z01
Screen Wiki: http://wiki.tjc1688.com/doku.php
Author: Antsec@github
'''

from machine import UART
import time

while True:
    
    uart1 = UART(1, baudrate=115200, tx=7, rx=8)
    uart1.write('t0.txt="Hi DiaoMao"')
    uart1.write(b'\xff\xff\xff') #Ending Tag Hex
    time.sleep(1)
