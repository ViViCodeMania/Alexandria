# -*- coding: utf-8 -*-

import max7219.led as led
import time
import datetime

device = led.matrix()

while True:
    t = time.time()
    ctime = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')
    device.show_message(ctime)