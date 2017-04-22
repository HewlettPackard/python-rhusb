#!/usr/bin/env python
#
# based on tutorials:
# http://www.roman10.net/serial-port-communication-in-python/
# http://www.brettdangerfield.com/post/raspberrypi_tempature_monitor_project/
#
import serial
import time

CMD = "PA"
RHUSBPORT = "/dev/ttyUSB0"
BAUDRATE = 9600

ser = serial.Serial(RHUSBPORT, BAUDRATE)

ser.bytesize = serial.EIGHTBITS  # number of bits per bytes

ser.parity = serial.PARITY_NONE  # set parity check: no parity

ser.stopbits = serial.STOPBITS_ONE  # number of stop bits

# ser.timeout = None          #block read

# ser.timeout = 0             #non-block read

ser.timeout = 6  # timeout block read

ser.xonxoff = False  # disable software flow control

ser.rtscts = False  # disable hardware (RTS/CTS) flow control

ser.dsrdtr = False  # disable hardware (DSR/DTR) flow control

ser.writeTimeout = 0  # timeout for write

# print 'Starting Up Serial Monitor'

if ser.isOpen() == False:
    try:
        ser.open()

    except Exception, e:
        print "error open serial port: " + str(e)
        exit()

if ser.isOpen():

    try:
        ser.flushInput()  # flush input buffer, discarding all its contents
        ser.flushOutput()  # flush output buffer, aborting current output

        ser.write("{0}\r\n".format(CMD))
        # print("write data: {0}".format(CMD))
        time.sleep(0.5)
        numberOfLine = 0

        response = ser.readline()
        print(response)

        # while True:
        #
        #     response = ser.readline()
        #     print("read data: " + response)
        #
        #     # numberOfLine = numberOfLine + 1
        #     # if (numberOfLine >= 5):
        #     #     break

        ser.close()

    except Exception, e:
        print "error communicating...: " + str(e)

else:
    print "cannot open serial port "
