import serial
import numpy as np
import time

k=serial.Serial('/dev/ttyUSB0',baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=0.5, xonxoff=True, rtscts=False, write_timeout=0.5, dsrdtr=False, inter_byte_timeout=None);

class Source:
	def __init__(self, name):
		self.name=name;

	def WriteVoltSine(self, voltList,t,f,n,t2):
		self.voltList=voltList;
		self.t=t;
		self.f=f
		self.n=n
		self.t2=t2
		#T0=1.0/self.f
		self.timeStep=len(self.t)
		k.write('*RST\n');
		k.write('LIST:CLE\n');
		k.write('LIST:VOLT ');
		step=4;
		"""
		for i in range(0,step):
			for i in range(i*len(self.voltList)/step,(i+1)*len(self.voltList)/step):
				self.volt_out=str(self.voltList[i]);
				if i < ((i+1)*(len(self.voltList)-1)/step):
					k.write(self.volt_out);
					k.write(',');
				else:
					k.write(self.volt_out);
					k.write('\n');
		"""
		for i in range(0,len(self.voltList)):
				self.volt_out=str(self.voltList[i]);
				if i < len(self.voltList)-1:
					k.write(self.volt_out);
					k.write(',');
				else:
					k.write(self.volt_out);
					k.write('\n');
		#print(self.volt[2:len(self.volt)-1]);
		k.write('LIST:VOLT:POIN \n');
		k.readline();
		k.write('LIST:DWEL ');
		k.write(str(self.t2));
		k.write('\n');
		k.write('LIST:COUN ');
		k.write(str(self.n));
		k.write('\n');
		k.write('LIST:VOLT?\n');
		k.readline();
		k.write('OUTP ON\n');
		k.write('CURR 1 \n');
		k.write('VOLT:MODE LIST\n');
	def WriteVolt(self, voltValue):
		self.voltValue=voltValue;
		k.write('*RST\n');
		k.write('OUTP ON\n');
		k.write('VOLT ');
		k.write(str(self.voltValue));
		k.write('\n');
		k.write('CURR 1');
		k.write('\n');
		k.write('MEAS:VOLT?');
		k.write('\n');
	def identify(self):
		k.write('*idn?\n');
		name = k.readline()
		return name;
	def stop(self):
		k.write('*RST\n');
		k.write('LIST:CLE\n');
	def measV(self):
		k.write('MEAS:VOLT?\n')
	def readM(self):
		volt = k.readline()
		return volt;
	def measC(self):
		k.write('MEAS:CURR?\n')
		curr = k.readline()
		return curr;
		
