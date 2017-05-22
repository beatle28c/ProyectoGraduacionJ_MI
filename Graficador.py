#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: utf-850 -*-

from graphics import *
from button import *
import Tkinter as tk
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
		g=[];
		lab=['Señal Fuente','Señal Filtrada'];		
		for p in range(1,m+1):
			ax=plt.plot()
			plt.title('Señal de Salida'.decode('utf-8'),fontsize=16)
			plt.plot(t[p-1][0:2499],S[p-1],label='L'+str(p),linewidth=1.5);
			#plt.plot(t[p-1][0:2049],S[p-1][450:2499],label=lab[p-1].decode('utf-8'),linewidth=1.5);
			plt.grid(True)
			plt.xlabel('Tiempo (s)',fontsize=14)
			plt.xlim([0,0.2])
			if (max(S[p-1])>10):
				plt.ylabel('Amplitud (V)',fontsize=14)
			else:
				plt.ylabel('Amplitud (C)',fontsize=14)
		plt.legend(loc='upper left')
		plt.tight_layout()
		mng = plt.get_current_fig_manager()
		mng.resize(*mng.window.maxsize())
		plt.show(block=False)
		plt.savefig('grafico1.png')
