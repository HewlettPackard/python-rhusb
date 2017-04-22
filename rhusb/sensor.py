#
#  Copyright (C) 2017, Hewlett-Packard Development Company
#  Author: Dave Brookshire <dsb@hpe.com>
#
#

import serial
import time

default_device = "/dev/ttyUSB0"
default_speed = 9600


class RHUSB():
    def __init__(self,
                 device=default_device,
                 speed=default_speed,
                 timeout=None):
        self.dev = serial.Serial(device, speed)
        self.dev.bytesize = serial.EIGHTBITS
        self.dev.parity = serial.PARITY_NONE
        self.dev.stopbits = serial.STOPBITS_ONE
        self.dev.timeout = timeout
        self.dev.xonxoff = False
        self.dev.rtscts = False
        self.dev.dsrdtr = False
        self.dev.writeTimeout = 0

        if self.dev.isOpen() == False:
            self.dev.open()

        self.dev.flushInput()
        self.dev.flushOutput()

    def CMD(self, cmd):
        self.dev.flushInput()
        self.dev.flushOutput()
        self.dev.write("{0}\r\n".format(cmd))
        time.sleep(0.5)
        return self.dev.readline().strip()

    def PA(self):
        return self.CMD(cmd="PA")

    def F(self):
        return self.CMD(cmd="F")

    def C(self):
        return self.CMD(cmd="C")

    def H(self):
        return self.CMD(cmd="H")
