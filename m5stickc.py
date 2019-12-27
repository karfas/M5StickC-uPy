"""
m5stickc.py

High(?) level functions for dealing with M5StickC hardware
"""

import sys
try:
    del sys.modules["axp192"]
except:
    pass

from machine import I2C, Pin
from axp192 import AXP192

hw_i2c_0 = I2C(0, sda=Pin(21), scl=Pin(22))
axp = AXP192(hw_i2c_0)
axp.set_debug(True)
axp.setup()


def lcd_backlight_power(status=True):
    """On M5StickC, LCD backlight is connected to LD02"""
    axp.set_LD02(status)


def power_button():
    if axp.button():
        return True
    return False
