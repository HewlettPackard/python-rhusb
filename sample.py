#!/usr/bin/env python
#
#  Copyright (C) 2017, Hewlett-Packard Development Company
#  Author: Dave Brookshire <dsb@hpe.com>
#
#
import time
import serial
import platform

from rhusb.sensor import RHUSB

delay = 1
count = 10

if __name__ == '__main__':
    print("Platform: {0}".format(platform.system()))
    if platform.system() == "Windows":
        device = "COM4"
    else:
        device = "/dev/ttyUSB0"
    print("Device: {0}".format(device))
    print()

    try:
        sens = RHUSB(device=device)
        print("PA: [{0}]".format(sens.PA()))
        print("C: [{0}]".format(sens.C()))
        print("F: [{0}]".format(sens.F()))
        print("H: [{0}]".format(sens.H()))

        print("\nStarting {0} periodic readings every {1} seconds".format(count, delay))

        while count:
            print("--> {0}".format(sens.PA()))
            count -= 1
            time.sleep(delay)

    except serial.serialutil.SerialException:
        print("Error: Unable to open RH-USB Serial device {0}.".format(device))