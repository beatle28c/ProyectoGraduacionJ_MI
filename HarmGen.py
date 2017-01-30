import matplotlib.pyplot as plt
import numpy as np

class HarmGen:
	def __init__(self, amplitud,freq,nHarmonicas,t0=0,tau=np.pi/2):
		self.a=amplitud;
		self.f=freq;
		self.y=nHarmonicas;
		self.t0=to;
		self.tau=tau;
		
		
ampl=10;
f=60;
y=2;
t0=0;
tau=np.pi/2;
#function Y=series_fourier2(a,f,y,t0,tau)
Tp=1.0/f;
w0=2*np.pi*f;
Tm=0.0005;
t=np.arange(0,Tp,Tm);

Y=0;
for i in range(0,y+1):
    if (np.sinc(w0*i*tau/2)>=0):
        if (i==0):
            Y=np.cos(2*np.pi*f*t*i-w0*i*(t0+tau/2))*(1/Tp)+Y;
        else:
            Y=np.cos(2*np.pi*f*t*i-w0*i*(t0+tau/2))*(2/Tp)*abs(np.sinc(w0*i*tau/2))+Y;
    elif (np.sinc(w0*i*tau/2)<0):
        if (i==0):
            Y=np.cos(2*pi*f*t*i+pi-w0*i*(t0+tau/2))*(1/Tp)+Y;
        else:
            Y=np.cos(2*pi*f*t*i+pi-w0*i*(t0+tau/2))*(2/Tp)*abs(np.sinc(w0*i*tau/2))+Y
m1=max(Y);
m2=min(Y);
m=m2+(m1-m2)/2;
A=(m1-m2)/2;
Y=(Y-m)*(ampl/A);
plt.plot(t,Y);
plt.show();
print(str(len(Y)));
