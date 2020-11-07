# RomiBuild

sudo apt-get install avrdude
git clone https://github.com/jpokornyiii/RomiBuild.git
avrdude -v -patmega32u4 -cavr109 -P/dev/ttyACM0 -b57600 -D -Uflash:w:RomiBuild/wpilib-ws-romi.ino.arduino_leonardo.hex

But getting error:
Connecting to programmer: .avrdude: butterfly_recv(): programmer is not responding
