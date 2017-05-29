import time
import Adafruit_ADS1x15 as ADC
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter
import RPi.GPIO as GPIO

class Sensor:
	def __init__(self):
		filename='C000000';
		self.adc1 = ADC.ADS1115()
		self.numeracion=open('numeracion.txt','r');
		self.a=numeracion.readline(1); 
		self.numeracion=open('numeracion.txt','w');
		self.numeracion.write(str(int(a)+1));
		self.file1=filename[0:len(filename)-len(a)-2]+'CH1'+a;
		self.file2=filename[0:len(filename)-len(a)-2]+'CH1'+a;
		self.numeracion.close();
		self.GAIN = 16
		self.adc1.start_adc(1, gain=self.GAIN, data_rate=860)
	def VoltMeas(self,time):
		self.vout=[]
		self.time=time;
		start=time.time();
		while (time.time() - start) <= self.time:
			volt1 = adc1.get_last_result()
			vout.append(volt1)
		t=np.linspace(0,tf,len(vout))
		vout=np.array(vout)
		Cal=460.5659
		volt1Meas=Cal*vout/32767.0
		a=max(volt1Meas)-((max(volt1Meas)-min(volt1Meas))/2.0)
		volt1Meas=volt1Meas-a
		w=savgol_filter(volt1Meas,5,1,mode='nearest')
		w=savgol_filter(w,11,1)
		a=np.zeros(len(w))
		atm=a;
		tm=t[1]-t[0]
		atm[0]=len(w);
		atm[1]=tm;		
		filename1=filename1+'.CSV'
		np.savetxt(filename1,np.array([a,atm,a,w,t].T,delimiter=',')
		plt.style.use('ggplot')
		plt.plot(t,w)
		plt.show()
		adc1.stop_adc()
