#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import math

class fft_osc:
	def file(self, name, row, col):
		m=len(name);
		w=np.genfromtxt(name[0], dtype=float, delimiter=',', skip_header=0, usecols=1, max_rows=1);
		w=int(w)
		tm=np.genfromtxt(name[0], dtype=float, delimiter=',', skip_header=1, usecols=1, max_rows=1);
		S=np.empty(shape=[m,w-1]);
		#Y=np.empty(shape=[m,w-1]);
		L=np.empty(shape=[m]);
		for p in range(0,m):
			S[p]=np.loadtxt(name[p],dtype=float,delimiter=',',skiprows=row,usecols=(col,));
		L=float(len(S[0]));
		tm=float(tm);
		Fs=1/tm;
		t = np.linspace(0,tm*L,L+1);
		
		n=L;
		dim=1;
		for i in range(0,4):
			n=int(pow(2, math.ceil(math.log(n+1, 2))));
		Y=np.empty(shape=[m,n]);
		for p in range(0,m):
			Y[p]=abs(np.fft.fft(S[p],n));
		f=np.linspace(0,round(n/100)*(Fs/n),round(n/100)+1);
		for p in range(1,m+1):
			plt.subplot(2,m,p)
			plt.plot(t[0:2499],S[p-1]);
			#plt.title('FFT de senal')
			plt.xlabel('Tiempo (s)')
			plt.ylabel('Amplitud (V)')
		for p in range(1,m+1):
			plt.subplot(2,m,p+m)
			plt.plot(f[0:200],Y[p-1].real[0:200]);
			#plt.title('Senal de entrada')
			plt.xlabel('Frecuencia (Hz)')
		plt.show()
