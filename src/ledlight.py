# -*- coding: utf-8 -*-
from sakshat import SAKSHAT
import time

SAKS = SAKSHAT()
#批量设置LED排灯的状态，从左到右依次为：亮，灭，亮，灭，亮，灭，亮，灭
SAKS.ledrow.set_row([True, False, True, False, True, False, True, False])
time.sleep(3)
#批量设置LED排灯的状态，从左到右依次为：不变，亮，灭，不变，不变，不变，不变，亮
SAKS.ledrow.set_row([None, True, False, None, None, None, None, True])
time.sleep(3)
#点亮LED排灯的第8个灯，0代表第1个灯，依次类推
SAKS.ledrow.on_for_index(7)
time.sleep(3)
#灭掉LED排灯的第1个灯
SAKS.ledrow.off_for_index(0)
time.sleep(3)
#LED排灯全亮
SAKS.ledrow.on()
time.sleep(3)
#LED排灯全灭
SAKS.ledrow.off()
time.sleep(3)
#注意，新的SDK不再支持 SAKS.ledrow.items[3].on() 这种用法了。
#数码管的用法完全兼容之前的 SDK，由于硬件层使用了专用芯片，数码管的显示不再闪烁，效果更稳定了！
# 将显示“1234”4位数字，并且每一位右下角的小点点亮
SAKS.digital_display.show("1.2.3.4.")
time.sleep(3)
# 将显示“1234”4位数字，并且数字2后面的小点点亮
SAKS.digital_display.show("12.34")
time.sleep(3)
# 在第4位数码管显示“1”，其他3位数码管不显示
SAKS.digital_display.show("###1")
time.sleep(3)
# 关闭数码管
SAKS.digital_display.off()
