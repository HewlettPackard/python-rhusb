#!/usr/bin/env python
#
#  Copyright (C) 2017, Hewlett-Packard Development Company
#  Author: Dave Brookshire <dsb@hpe.com>
#
#

from rhusb.sensor import RHUSB

if __name__ == '__main__':
    sens = RHUSB()
    print("[{0}]".format(sens.PA()))
    print("[{0}]".format(sens.C()))
    print("[{0}]".format(sens.F()))
    print("[{0}]".format(sens.H()))