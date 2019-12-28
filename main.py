"""
main.py

main program
"""

import sys
import network
import time

# TESTING: remove used modules from system.
#
try:
    del sys.modules["app"]
except:
    pass

try:
    print("start wifi manager")
    import wifi_manager
    sta_if = wifi_manager.get_connection()
    if sta_if is None:
        wifi_manager.start()

    if sta_if.isconnected():
        print("connected: {}".format(sta_if.ifconfig()))
        import webrepl
        webrepl.start(password="secret")
    else:
        print("no network, skip weprepl start")

except Exception as e:
    sys.print_exception(e)
