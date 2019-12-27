"""
app.py
"""

import sys
import time

try:
    del sys.modules["m5stickc"]
except:
    pass

try:
    from m5stickc import lcd_backlight_power, power_button, axp

    lcd_backlight_power(False)
    print("Battery Voltage: {}".format(axp.battery_voltage()))
    print("Battery Current: {}".format(axp.battery_current()))
    print("Bus Voltage: {}".format(axp.bus_voltage()))
    print("Bus Current: {}".format(axp.bus_current()))
    print("Input Voltage: {}".format(axp.input_voltage()))
    print("Input Current: {}".format(axp.input_current()))

#    while True:
#        print("power button: {}".format(power_button()))
#        time.sleep_ms(100)
except Exception as e:
    sys.print_exception(e)
    del sys.modules["m5stickc"]
    del sys.modules[__name__]

