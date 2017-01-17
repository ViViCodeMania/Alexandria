# -*- coding: utf-8 -*-

from sakshat import SAKSHAT
import time

Saks = SAKSHAT()

Saks.digital_display.off()
Saks.digital_display.on()
Saks.ledrow.off()
i = 0
switch = True
while True:
    t = time.localtime()
    h = t.tm_hour
    m = t.tm_min
    s = t.tm_sec

    # print '%02d:%02d:%02d' % (h, m, s)

    if i % 2 == 0:
        timetable = '%02d.%02d'
    else:
        timetable = '%02d%02d'

    if switch:
        Saks.digital_display.show(timetable % (h, m))
        Saks.ledrow.on_for_index(i % 8)
    else:
        Saks.digital_display.show(timetable % (h, m))
        Saks.ledrow.off_for_index(i % 8)
        i += 1

    switch = not switch
    time.sleep(0.25)