#
#  Copyright (C) 2017, Hewlett-Packard Development Company
#  Author: Dave Brookshire <dsb@hpe.com>
#
#  References:
#  http://stackoverflow.com/questions/25662489/how-to-write-on-serial-port-in-python-that-ttyusb0-will-be-interpreted-commands
#  http://www.roman10.net/serial-port-communication-in-python/
#  http://www.brettdangerfield.com/post/raspberrypi_tempature_monitor_project/
#
import serial
import time

default_device = "/dev/ttyUSB0"
default_speed = 9600
serial_delay = 0.5


class RHUSB():
    """
    Simple abstraction around the RH-USB temperature sensor
    """
    def __init__(self,
                 device=default_device,
                 speed=default_speed,
                 timeout=None):
        """
        Create an instance of the sensor abstraction
        
        :param device: Serial device
        :param speed: Baudrate
        :param timeout: Timeout
        """
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
        """
        Send a single command via the serial port, and return a single line of output
        
        :param cmd: Command to send (ie. PA, F, C or H)
        :return: Single string of output from the serial port
        """
        self.dev.flushInput()
        self.dev.flushOutput()
        self.dev.write("{0}\r\n".format(cmd).encode())
        time.sleep(serial_delay)
        return self.dev.readline().strip()

    def PA(self):
        """
        Return the current relative humidity and temperature in Fahrenheit
        :return: String output of H,F
        """
        return self.CMD(cmd="PA")

    def F(self):
        """
        Return the current temperature in Fahrenheit
        :return: String value of sensor reading
        """
        return self.CMD(cmd="F")

    def C(self):
        """
        Return the current temperature in Celsius
        :return: String value of sensor reading
        """
        return self.CMD(cmd="C")

    def H(self):
        """
        Return the current relative humidity
        :return: String value of sensor reading
        """
        return self.CMD(cmd="H")
