#!/usr/bin/python3

# Code Version #
software = "v.1.0.0"

import os,subprocess
from serial import Serial
import time


#use this for Raspberry Pi's
port=Serial(port='/dev/ttyAMA0',baudrate=9600, timeout=1.0)


eof = "\xff\xff\xff"
jay = "page 0"+eof
port.write(str.encode(jay))

print ('entering loop')


while True:
	rcv=port.readline()
	incoming = str(repr(rcv))
	print(incoming[9:11])
	if(incoming[9:11] == '01'):
		print('left button')
	elif(incoming[9:11] == '02'):
		print('right button')



	