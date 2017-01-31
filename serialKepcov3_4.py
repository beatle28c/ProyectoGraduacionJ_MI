import serial
import numpy as np
import time


#'/dev/ttyUSB0'



class Source:
	def __init__(self, name, port):
		k=serial.Serial()
		k.baudrate=9600;
		k.bytesize=serial.EIGHTBITS;
		k.parity=serial.PARITY_NONE;
		k.stopbits=serial.STOPBITS_ONE;
		k.timeout=0.5;
		k.xonxoff=True;
		k.rtscts=False;
		k.write_timeout=0.5;
		k.dsrdtr=False;
		k.inter_byte_timeout=None;
		k.port=port;
		self.port=port;
		self.k=k;
		self.name=name;
		#k.open();
		
	def connectport(self):
		try: 
			self.k.open()
			return "Conectado en puerto: " + self.k.port
		except Exception, e:
			return ("Error: " + "\n" +  str(e)[0:len(str(e))/2] + "\n" + str(e)[len(str(e))/2:len(str(e))])
			#exit()
		
		if self.k.isOpen():
			try:
				self.k.write('*idn?\n')
			except Exception, e1:
				return ("error de comunicacion: " + "\n" +  str(e)[0:len(str(e1))/2] + "\n" + str(e1)[len(str(e1))/2:len(str(e1))])
		
		else:
			return ("No se pudo abrir puerto serial")

	def WriteTrian(self, voltList,t,f,n,t2,C):
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
		step=10;
		m=len(self.voltList)//step
		m=m*step
		voltList1=self.voltList[0:m]
		voltList2=self.voltList[m:len(self.voltList)]
		for j in range(0,step):
			self.k.write('LIST:VOLT ');
			for i in range(j*len(voltList1)/step,(j+1)*len(voltList1)/step):
				self.volt_out=str(voltList1[i]);
				if i < ((j+1)*(len(voltList1)-1)/step):
					self.k.write(self.volt_out);
					self.k.write(',');
				else:
					self.k.write(self.volt_out);
					self.k.write('\n');
		self.k.write('LIST:VOLT ');
		for i in range(0,len(voltList2)):
				self.volt_out=str(voltList2[i]);
				if i < len(voltList2):
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
		self.k.write('CURR ');
		self.k.write(str(self.C));
		self.k.write('\n');
		self.k.write('VOLT:MODE LIST\n');


	def WriteVoltSine(self, voltList,t,f,n,t2,C):
		self.voltList=voltList;
		self.t=t;
		self.f=f
		self.n=n
		self.t2=t2
		self.C=C
		#T0=1.0/self.f
		self.timeStep=len(self.t)
		self.k.write('*RST\n');
		self.k.write('LIST:CLE\n');
		
		step=10;
		m=len(self.voltList)//step
		m=m*step
		voltList1=self.voltList[0:m]
		voltList2=self.voltList[m:len(self.voltList)]
		for j in range(0,step):
			self.k.write('LIST:VOLT ');
			for i in range(j*len(voltList1)/step,(j+1)*len(voltList1)/step):
				self.volt_out=str(voltList1[i]);
				if i < ((j+1)*(len(voltList1)-1)/step):
					self.k.write(self.volt_out);
					self.k.write(',');
				else:
					self.k.write(self.volt_out);
					self.k.write('\n');
		self.k.write('LIST:VOLT ');
		for i in range(0,len(voltList2)):
				self.volt_out=str(voltList2[i]);
				if i < len(voltList2):
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
		self.k.write('CURR ');
		self.k.write(str(self.C));
		self.k.write('\n');
		self.k.write('VOLT:MODE LIST\n');
	def WriteVolt(self, voltValue,C):
		self.voltValue=voltValue;
		self.C=C
		self.k.write('*RST\n');
		self.k.write('OUTP ON\n');
		self.k.write('VOLT ');
		self.k.write(str(self.voltValue));
		self.k.write('\n');
		self.k.write('CURR ');
		self.k.write(str(self.C));
		self.k.write('\n');
		self.k.write('MEAS:VOLT?');
		self.k.write('\n');
	def identify(self):
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
		
	def calPlusFine(self,val):
		self.k.write('CAL:DATA ');
		self.k.write(str(val));
		self.k.write('\n');
	
	def calMinusFine(self,val):
		self.k.write('CAL:DATA ');
		self.k.write('-');
		self.k.write(str(val));
		self.k.write('\n');
	
	def calPlusCoarse(self,val):
		self.k.write('CAL:DPOT ');
		self.k.write(str(val));
		self.k.write('\n');
	
	def calMinusCoarse(self,val):
		self.k.write('CAL:DPOT ');
		self.k.write('-');
		self.k.write(str(val));
		self.k.write('\n');
	
	def calStart(self,password):
		self.k.write('*RST\n');
		self.k.write('SYST:PASS:CEN ');
		self.k.write(str(password));	
		self.k.write('\n');
		self.k.write('CAL:STAT 1\n');
	def calZero(self):
		self.k.write('CAL:VOLT ZERO\n');
	def calMax(self):
		self.k.write('CAL:VOLT MAX\n');
	def calMin(self):
		self.k.write('CAL:VOLT MIN\n');
	def calVPRmax(self):
		self.k.write('CAL:VPR MAX\n');
	def calVPRmin(self):
		self.k.write('CAL:VPR MIN\n');
	def calSave(self):
		self.k.write('CAL:DATA SAVE\n');
		self.k.write('CAL:STAT 0\n');
		self.k.write('CAL:STAT?\n');
		status = self.k.readline()
		return status;
	
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
