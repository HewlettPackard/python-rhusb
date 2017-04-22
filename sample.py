#!/usr/bin/env python
#
#  Copyright (C) 2017, Hewlett-Packard Development Company
#  Author: Dave Brookshire <dsb@hpe.com>
#
#
import time

from src.rhusb.sensor import RHUSB

delay = 1
count = 10

if __name__ == '__main__':
    sens = RHUSB()
    print("PA: [{0}]".format(sens.PA()))
    print("C: [{0}]".format(sens.C()))
    print("F: [{0}]".format(sens.F()))
    print("H: [{0}]".format(sens.H()))

    print("\nStarting periodic readings every {0} seconds".format(delay))

    while count:
        print("--> {0}".format(sens.PA()))
        count -= 1
        time.sleep(delay)
