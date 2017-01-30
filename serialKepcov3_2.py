import serial
import numpy as np
import time


k=serial.Serial('/dev/ttyUSB0',baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=0.5, xonxoff=True, rtscts=False, write_timeout=0.5, dsrdtr=False, inter_byte_timeout=None);

class Source:
	def __init__(self, name):
		self.name=name;
		
	def WriteTrian(self, voltList,t,f,n,t2,C):
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
		step=10;
		m=len(self.voltList)//step
		m=m*step
		voltList1=self.voltList[0:m]
		voltList2=self.voltList[m:len(self.voltList)]
		for j in range(0,step):
			k.write('LIST:VOLT ');
			for i in range(j*len(voltList1)/step,(j+1)*len(voltList1)/step):
				self.volt_out=str(voltList1[i]);
				if i < ((j+1)*(len(voltList1)-1)/step):
					k.write(self.volt_out);
					k.write(',');
				else:
					k.write(self.volt_out);
					k.write('\n');
		k.write('LIST:VOLT ');
		for i in range(0,len(voltList2)):
				self.volt_out=str(voltList2[i]);
				if i < len(voltList2):
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
					a.append(self.volt_out+',')
				else:
					k.write(self.volt_out);
					a.append(self.volt_out)
					k.write('\n');
		print(a)
		"""
		
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
		k.write('CURR ');
		k.write(str(self.C));
		k.write('\n');
		k.write('VOLT:MODE LIST\n');


	def WriteVoltSine(self, voltList,t,f,n,t2,C):
		self.voltList=voltList;
		self.t=t;
		self.f=f
		self.n=n
		self.t2=t2
		self.C=C
		#T0=1.0/self.f
		self.timeStep=len(self.t)
		k.write('*RST\n');
		k.write('LIST:CLE\n');
		
		step=10;
		m=len(self.voltList)//step
		m=m*step
		voltList1=self.voltList[0:m]
		voltList2=self.voltList[m:len(self.voltList)]
		for j in range(0,step):
			k.write('LIST:VOLT ');
			for i in range(j*len(voltList1)/step,(j+1)*len(voltList1)/step):
				self.volt_out=str(voltList1[i]);
				if i < ((j+1)*(len(voltList1)-1)/step):
					k.write(self.volt_out);
					k.write(',');
				else:
					k.write(self.volt_out);
					k.write('\n');
		k.write('LIST:VOLT ');
		for i in range(0,len(voltList2)):
				self.volt_out=str(voltList2[i]);
				if i < len(voltList2):
					k.write(self.volt_out);
					k.write(',');
				else:
					k.write(self.volt_out);
					k.write('\n');
		"""
		
		a=[]

		for i in range(0,len(self.voltList)):
				self.volt_out=str(self.voltList[i]);
				if i < len(self.voltList)-1:
					k.write(self.volt_out);
					k.write(',');
					a.append(self.volt_out+',')
				else:
					k.write(self.volt_out);
					a.append(self.volt_out)
					k.write('\n');
		print(a)
		"""
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
		k.write('CURR ');
		k.write(str(self.C));
		k.write('\n');
		k.write('VOLT:MODE LIST\n');
	def WriteVolt(self, voltValue,C):
		self.voltValue=voltValue;
		k.write('*RST\n');
		k.write('OUTP ON\n');
		k.write('VOLT ');
		k.write(str(self.voltValue));
		k.write('\n');
		k.write('CURR ');
		k.write(str(self.C));
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
		
	def connect(self):
		try: 
			k.open()
			return "Conectado"
		except Exception, e:
			return "error al abrir puerto serial: " + str(e)
			exit()
			
		if k.isOpen():
			try:
				flushInput()
				k.flushOutput()
				k.write('*idn?\n')
				time.sleep(0.1)
				n=0;
				while True:
					respuesta = k.readline()
					return("Fuente: "+respuesta)

				k.close()
			except Exception, e1:
				return "error de comunicacion: " + str(e1)
		
		else:
			return "No se pudo abrir puerto serial"
