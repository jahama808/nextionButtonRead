#!/usr/bin/python3

# Code Version #
software = "v.1.0.0"

import os,subprocess
from serial import Serial
import time


#use this for Raspberry Pi's
port=Serial(port='/dev/ttyAMA0',baudrate=9600, timeout=1.0)


eof = b'\xff\xff\xff'


while True:
	port.write(b'page 8'+eof)

	print ('entering loop')



	pushButton = False
	while pushButton == False:
		rcv=port.readline()
		incoming = str(repr(rcv))
		# print(incoming[9:11])
		if(incoming[9:11] == '03'):
			port.write(b'page 1'+eof)
			pushButton = True
		elif(incoming[9:11] == '04'):
			port.write(b'page 2'+eof)
			pushButton = True

	print('done')
	time.sleep(10)


	