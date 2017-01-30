import serial
import numpy as np
import time

#'/dev/ttyUSB0'
class Source:
	def __init__(self, name,port):
		self.name=name;
		self.port=port;
		k=serial.Serial(self.port,baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=0.5, xonxoff=True, rtscts=False, write_timeout=0.5, dsrdtr=False, inter_byte_timeout=None);
		self.k=k;
		
	def WriteTrian(self, voltList,t,f,n,t2):
		self.voltList=voltList;
		self.t=t;
		self.f=f
		self.n=n
		self.t2=t2
		#T0=1.0/self.f
		self.timeStep=len(self.t)
		self.k.write('*RST\n');
		self.k.write('LIST:CLE\n');
		self.k.write('LIST:VOLT ');
		step=4;
		for i in range(0,step):
			for i in range(i*len(self.voltList)/step,(i+1)*len(self.voltList)/step):
				self.volt_out=str(self.voltList[i]);
				if i < ((i+1)*(len(self.voltList)-1)/step):
					self.k.write(self.volt_out);
					self.k.write(',');
				else:
					self.k.write(self.volt_out);
					self.k.write('\n');
		#print(self.volt[2:len(self.volt)-1]);
		self.k.write('LIST:VOLT:POIN \n');
		self.k.readline();
		self.k.write('LIST:DWEL ');
		self.k.write(str(self.t2));
		self.k.write('\n');
		self.k.write('LIST:COUN ');
		self.k.write(str(self.n));
		self.k.write('\n');
		self.k.write('LIST:VOLT?\n');
		self.k.readline();
		self.k.write('OUTP ON\n');
		self.k.write('CURR 1 \n');
		self.k.write('VOLT:MODE LIST\n');


	def WriteVoltSine(self, voltList,t,f,n,t2):
		self.voltList=voltList;
		self.t=t;
		self.f=f
		self.n=n
		self.t2=t2
		#T0=1.0/self.f
		self.timeStep=len(self.t)
		self.k.write('*RST\n');
		self.k.write('LIST:CLE\n');
		self.k.write('LIST:VOLT ');
		step=4;
		"""
		for i in range(0,step):
			for i in range(i*len(self.voltList)/step,(i+1)*len(self.voltList)/step):
				self.volt_out=str(self.voltList[i]);
				if i < ((i+1)*(len(self.voltList)-1)/step):
					self.k.write(self.volt_out);
					self.k.write(',');
				else:
					self.k.write(self.volt_out);
					self.k.write('\n');
		"""
		for i in range(0,len(self.voltList)):
				self.volt_out=str(self.voltList[i]);
				if i < len(self.voltList)-1:
					self.k.write(self.volt_out);
					self.k.write(',');
				else:
					self.k.write(self.volt_out);
					self.k.write('\n');
		#print(self.volt[2:len(self.volt)-1]);
		self.k.write('LIST:VOLT:POIN \n');
		self.k.readline();
		self.k.write('LIST:DWEL ');
		self.k.write(str(self.t2));
		self.k.write('\n');
		self.k.write('LIST:COUN ');
		self.k.write(str(self.n));
		self.k.write('\n');
		self.k.write('LIST:VOLT?\n');
		self.k.readline();
		self.k.write('OUTP ON\n');
		self.k.write('CURR 1 \n');
		self.k.write('VOLT:MODE LIST\n');
	def WriteVolt(self, voltValue):
		self.voltValue=voltValue;
		self.k.write('*RST\n');
		self.k.write('OUTP ON\n');
		self.k.write('VOLT ');
		self.k.write(str(self.voltValue));
		self.k.write('\n');
		self.k.write('CURR 1');
		self.k.write('\n');
		self.k.write('MEAS:VOLT?');
		self.k.write('\n');
	def identify(self):
		self.k.reset_input_buffer();
		self.k.write('*idn?\n');
		name = self.k.readline()
		return name;
	def stop(self):
		self.k.write('*RST\n');
		self.k.write('LIST:CLE\n');
	def measV(self):
		self.k.write('MEAS:VOLT?\n')
	def readM(self):
		volt = self.k.readline()
		return volt;
	def measC(self):
		self.k.write('MEAS:CURR?\n')
		curr = self.k.readline()
		return curr;
		
	def connect(self):
		try: 
			self.k.open()
			return "Conectado"
		except Exception, e:
			return "error al abrir puerto serial: " + str(e)
			exit()
			
		if self.k.isOpen():
			try:
				flushInput()
				self.k.flushOutput()
				self.k.write('*idn?\n')
				time.sleep(0.1)
				n=0;
				while True:
					respuesta = self.k.readline()
					return("Fuente: "+respuesta)

				self.k.close()
			except Exception, e1:
				return "error de comunicacion: " + str(e1)
		
		else:
			return "No se pudo abrir puerto serial"
