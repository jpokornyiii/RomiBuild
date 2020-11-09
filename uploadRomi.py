#!/usr/bin/env python

# This file uploads to the Romi using a USB cable

import time
import serial
import os

def main():
	print("Beginning binary upload to Romi ...");
        usbport = '/dev/ttyACM0';
	hexfile = '/home/pi/RomiBuild/wpilib-ws-romi.ino.arduino_leonardo.hex';
	# baudrate of 1200 resets the Arduino to boot mode for 8 seconds
	brate = 1200;
	print("Resetting Romi to boot mode (should see quickly flashing yellow LED");
	conn = serial.Serial(port=usbport, baudrate=1200)
        if conn.isOpen() != True:
		print("Problem connecting to port " + usbport);
        conn.close();
	# Allow Romi to go into boot mode
	time.sleep(1);
	# Upload binary to Romi
	os.system('avrdude -v -patmega32u4 -cavr109 -P/dev/ttyACM0 -b57600 -D -Uflash:w:' + hexfile + ':i');

if __name__ == "__main__":
	main()
