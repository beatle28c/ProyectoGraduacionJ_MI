import serial
import time

k=serial.Serial('/dev/ttyUSB0',baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=None, xonxoff=True, rtscts=False, write_timeout=0.5, dsrdtr=False, inter_byte_timeout=None);
for i in range (0,100):
	k.write('*idn?\n');
	time.sleep(1);
	
