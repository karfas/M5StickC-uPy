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
    del sys.modules["webrepl"]
    del sys.modules["uftpd"]
except:
    pass


def startup_net():
    print("start uftpd")
    import uftpd 	# implicit starts the server
    # uftpd.start(port=21, verbose=1, splash=True)

    print("start webrepl")
    import webrepl
    webrepl.start(password="secret")

try:
    print("start wifi manager")
    import wifimgr
    sta_if = wifimgr.get_connection()
    if sta_if is None:
        wifimgr.start()

    if sta_if.isconnected():
        startup_net()
    else:
        print("no network, skip weprepl start")

except Exception as e:
    sys.print_exception(e)
