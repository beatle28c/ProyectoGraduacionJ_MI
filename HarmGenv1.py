import matplotlib.pyplot as plt
import numpy as np

class HarmGen:
	def __init__(self, amplitud,freq,nHarmonicas,t0=0,tau=np.pi/2):
		self.a=float(amplitud);
		self.f=float(freq);
		self.y=int(nHarmonicas);
		self.t0=float(t0);
		self.tau=float(tau);
		Tp=1.0/self.f;
		self.Tp=Tp;
		Tm=0.0005;
		self.Tm=Tm;
	
	def Harm(self):
		t=np.arange(0,self.Tp,self.Tm);
		w0=2*np.pi*self.f;
		Y=0;
		for i in range(0,self.y+1):
			if (np.sinc(w0*i*self.tau/2)>=0):
				if (i==0):
					Y=np.cos(2*np.pi*self.f*t*i-w0*i*(self.t0+self.tau/2))*(1/self.Tp)+Y;
				else:
					Y=np.cos(2*np.pi*self.f*t*i-w0*i*(self.t0+self.tau/2))*(2/self.Tp)*abs(np.sinc(w0*i*self.tau/2))+Y;
			elif (np.sinc(w0*i*self.tau/2)<0):
				if (i==0):
					Y=np.cos(2*np.pi*self.f*t*i+np.pi-w0*i*(self.t0+self.tau/2))*(1/self.Tp)+Y;
				else:
					Y=np.cos(2*np.pi*self.f*t*i+np.pi-w0*i*(self.t0+self.tau/2))*(2/self.Tp)*abs(np.sinc(w0*i*self.tau/2))+Y
		m1=max(Y);
		m2=min(Y);
		m=m2+(m1-m2)/2;
		A=(m1-m2)/2;
		Y=(Y-m)*(self.a/A);
		"""
		plt.plot(t,Y);
		plt.show()
		print(str(len(Y)));
		"""
		return Y
