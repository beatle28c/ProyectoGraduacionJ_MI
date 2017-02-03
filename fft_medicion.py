import matplotlib.pyplot as plt
import numpy as np
import math

class fft_osc:
	def file(self, name, row, col):
		t=np.genfromtxt(name, dtype=float, delimiter=',', skip_header=1, usecols=1, max_rows=1)
		S=np.loadtxt(name,dtype=float,delimiter=',',skiprows=row,usecols=(col,));
		L=float(len(S));
		tm=float(t);
		Fs=1/tm;
		t = np.linspace(0,tm*L,L+1);
		Y = np.fft.fft(S);
		n=L;
		dim=1;
		for i in range(0,4):
			n=int(pow(2, math.ceil(math.log(n+1, 2))));
		Y=abs(np.fft.fft(S,n));
		f=np.linspace(0,round(n/100)*(Fs/n),round(n/100)+1);
		plt.plot(f[0:200],Y.real[0:200]);
		plt.show(block=False)
