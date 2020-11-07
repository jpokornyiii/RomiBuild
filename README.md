# RomiBuild

1. sudo apt-get install avrdude
1. git clone https://github.com/jpokornyiii/RomiBuild.git
1. avrdude -v -patmega32u4 -cavr109 -P/dev/ttyACM0 -b57600 -D -Uflash:w:RomiBuild/wpilib-ws-romi.ino.arduino_leonardo.hex

<pre>
But getting error:
Connecting to programmer: .avrdude: butterfly_recv(): programmer is not responding
</pre>
