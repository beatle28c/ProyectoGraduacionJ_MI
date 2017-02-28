#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: utf-850 -*-

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import MultipleLocator
import numpy as np
import math

class fft_osc:
	def file(self, name, row, col):
		m=len(name);
		w=np.empty(shape=[m]);
		tm=np.empty(shape=[m]);
		Fs=np.empty(shape=[m]);
		
		#t=np.empty(shape=[m]);
		for p in range(0,m):
			w_1=np.genfromtxt(name[p], dtype=float, delimiter=',', skip_header=0, usecols=1, max_rows=1);
			tm_1=np.genfromtxt(name[p], dtype=float, delimiter=',', skip_header=1, usecols=1, max_rows=1);
			w[p]=int(w_1)
			tm[p]=float(tm_1);
			Fs[p]=1/tm[p];
		w1=int(max(w));
		t=np.empty(shape=[m,w1]);
		S=np.empty(shape=[m,w1-1]);
		#Y=np.empty(shape=[m,w1-1]);
		L=np.empty(shape=[m]);
		n=np.empty(shape=[m+1]);
		for p in range(0,m):
			S[p]=np.loadtxt(name[p],dtype=float,delimiter=',',skiprows=row,usecols=(col,));
			L[p]=float(len(S[p]));
			n[p]=L[p];
			t[p]=np.linspace(0,tm[p]*L[p],L[p]+1);
		dim=1;
		for i in range(0,m):
			for p in range(0,5):
				n[i]=int(pow(2, math.ceil(math.log(n[i]+1, 2))));
		for i in range(0,m):
			w[i]=int(round(n[i]/100)+1)
		w2=int(max(w))
		n=int(max(n));
		Y=np.empty(shape=[m,n]);
		f=np.empty(shape=[m,w2]);
		xpos=np.empty(shape=[m,5]);
		ymax=np.empty(shape=[m,5]);
		THD=np.empty(shape=[m]);
		for p in range(0,m):
			Y[p]=abs(np.fft.hfft(S[p],n));
			f[p]=np.linspace(0,round(n/100)*(Fs[p]/n),round(n/100)+1);
			maxval=max(Y[p])
			step=[i for i, j in np.ndenumerate(Y[p]) if j == maxval][0][0];
			if step==0:
				maxval=max(Y[p][15:10000])
				step=[i for i, j in np.ndenumerate(Y[p]) if j == maxval][0][0];
				#print(maxval,step)
			for u in range(0,5):
				if u==0:
					ymax[p][0]=maxval;
					xpos[p][0]=[i for i, j in np.ndenumerate(Y[p]) if j == maxval][0][0]
				else:
					print(Y[p][(step*(u+1))-1:(step*(u+1))+1])
					#ymax[p][u]=max(Y[p][(step*(u+1))-1:(step*(u+1))+1])
					xpos[p][u]=[i for i, j in np.ndenumerate(Y[p]) if j == ymax[p][u]][0][0]	
			Vthd=0.0;
			for u in range(1,5):
				Vthd=((ymax[p][u])**2)+Vthd
			THD[p]=np.sqrt(Vthd)/ymax[p][0]
			#print(f[p])
		for p in range(1,m+1):
			ax=plt.subplot(2,m,p)
			plt.title('Señal de entrada'.decode('utf-8'))
			plt.plot(t[p-1][0:2499],S[p-1]);
			plt.ylim([-15,15])
			plt.grid(True)
			plt.xlabel('Tiempo (s)')
			plt.ylabel('Amplitud (V)')
		for p in range(1,m+1):
			ax=plt.subplot(2,m,p+m)
			
			for u in range(0,5):
				ax.annotate('F'+str(u),xy=(f[p-1][int(xpos[p-1][u])],ymax[p-1][u]), xycoords='data',xytext=(f[p-1][int(xpos[p-1][u])],ymax[p-1][u]+2000), textcoords='data',size=10, va="center", ha="center", bbox=dict(boxstyle="round", fc="w"), arrowprops=dict(arrowstyle="-|>", connectionstyle="arc3,rad=0",fc="b"),)
			ax.annotate('THD='+str(round(THD[p-1]*100,4))+'%',xy=(250,0), xycoords='data',xytext=(200,17000), textcoords='data',size=11, va="center", ha="center", bbox=dict(boxstyle="square", fc="w"),)
			
			#ax.annotate('f0', xy=(50.0, yy[p-1]), xytext=(x[p-1]+10, yy[p-1]+10),arrowprops=dict(arrowstyle="->",connectionstyle="arc3"),)
			plt.title('FFT de señal'.decode('utf-8'))
			#plt.semilogy(f[p-1][0:200],20*log10((Y[p-1]).real[0:200]));
			plt.plot(f[p-1][0:len(f[p-1])],(Y[p-1]).real[0:len(f[p-1])]);
			#plt.axis([0, 250,0,15000])
			plt.xlim([0,300])
			#plt.ylim([0,18000])
			#ax.xaxis.set_major_locator(MultipleLocator(10))
			ax.xaxis.set_minor_locator(MultipleLocator(10))
			#ax.yaxis.set_major_locator(MultipleLocator(1000))
			#ax.yaxis.set_minor_locator(MultipleLocator(500))
			plt.grid(True)
			plt.xlabel('Frecuencia (Hz)')
			
		
		plt.tight_layout()
		mng = plt.get_current_fig_manager()
		mng.resize(*mng.window.maxsize())
		plt.show()	
