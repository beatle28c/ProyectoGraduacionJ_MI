	def WriteVoltSine(self, Volt,f,n,C):
		self.k.flushInput();
		self.k.write('*OUTP OFF\n');
		self.k.write('*RST\n');
		self.V=Volt;
		self.f=f
		self.n=n
		self.C=C
		#self.tsm=tm
		tsm=0.0002;		#Tiempo de muestreo minimo
		self.tsm=tsm
		T=1.0/self.f
		#ts=self.tsm;
		m=float(int(T/self.tsm));
		ts=round(T/m,9);
		#t=np.arange(0,T,ts);
		t=np.arange(0,m*ts,ts);
		funct=self.V*np.sin(2*np.pi*self.f*t)
		"""		
		if len(t) < len(funct):
			m=len(t);
			funct=funct[0:m]
			t=t[0:m]
		elif len(funct) < len(t):
			m=len(funct);
			funct=funct[0:m]
			t=t[0:m]
		"""
		voltList=np.round(funct,3)
		self.voltList=voltList;
		step=20;
		m=len(self.voltList)//step
		m=m*step
		voltList1=self.voltList[0:m]
		voltList2=self.voltList[m:len(self.voltList)]
		self.k.write('FUNC:MODE VOLT\n');
		self.k.write('LIST:CLEAR\n');
		#self.stop();
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
		self.k.write('LIST:VOLT:POIN \n');
		self.k.write('LIST:DWEL ');
		self.k.write(str(ts));
		self.k.write('\n');
		self.k.flushInput();
		self.k.write('LIST:DWEL?\n');
		print(self.k.readline());
		self.k.write('LIST:COUN ');
		self.k.write(str(int(self.n)));
		self.k.write('\n');
		#self.k.write('LIST:VOLT?\n');
		#self.k.readline();
		self.k.write('OUTP ON\n');
		self.k.write('CURR ');
		self.k.write(str(self.C));
		self.k.write('\n');
		self.k.write('VOLT:MODE LIST\n');
		self.k.flushInput()
		#plt.plot(t,funct)
		#plt.show(block=False);
		print([ts,1.0/(ts*len(funct))]);
