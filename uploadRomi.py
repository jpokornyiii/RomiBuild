#!/usr/bin/env python

# This file uploads to the Romi using a USB cable

import time
import serial
import os
import sys
import getopt

def main(argv):
	
	try:
		opts, args = getopt.getopt(argv,"hp:f:",["port=","file="]);
	except getopt.GetoptError as err:
		print(err);
		print("Example: uploadRomi.py -p /dev/ttyACM0 -f firmware/.pio/build/a-start32U4/firmware.hex");
		sys.exit(1)

	# Set Defaults
	usbport = '/dev/ttyACM0';
	hexfile = '$NVM_BIN/../lib/node_modules/wpilib-ws-robot-romi/firmware/.pio/build/a-star32U4/firmware.hex';

	for opt, arg in opts:
		if opt == "-h":
			print("uploadRomi.py -p <full_port_path> -f <file_path>");
			sys.exit();
		if opt in ("-p", "--port"):
			usbport = arg;
		if opt in ("-f", "--file"):
			hexfile = arg;

	print("Beginning binary upload to Romi ...");
    
	# baudrate of 1200 resets the Arduino to boot mode for 8 seconds
	brate = 1200;
	print("Resetting Romi to boot mode (should see quickly flashing yellow LED");
	conn = {};
	try:
		conn = serial.Serial(port=usbport, baudrate=1200);
	except serial.SerialException as err:
		print(err);
		sys.exit(1);
   	
	if conn.isOpen() != True:
		print("Problem connecting to port " + usbport);
    
	conn.close();
	# Allow Romi to go into boot mode
	time.sleep(1);
	# Upload binary to Romi
	cmd = 'avrdude -v -patmega32u4 -cavr109 -P' + usbport + ' -b57600 -D -Uflash:w:' + hexfile + ':i';
	print(cmd);
	os.system(cmd);

if __name__ == "__main__":
	main(sys.argv[1:])

