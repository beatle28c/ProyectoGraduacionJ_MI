import time
import Adafruit_ADS1x15 as ADC
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter
import savitzky_golay as sg

N=100;

adc1 = ADC.ADS1115()

# Ganancias
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V

GAIN = 8

#Volt2.start_adc(2, gain=GAIN)
#Volt1.start_adc(1, gain=GAIN)
adc1.start_adc(1, gain=GAIN, data_rate=860)
#Curr1.start_adc(0, gain=GAIN)
vout=[]
start = time.time()
tm=0.00001;
tf=0.5
while (time.time() - start) <= tf:
	volt1 = adc1.get_last_result()
	#volt1=adc1.read_adc(1, gain=GAIN, data_rate=860)
	#volt2=adc1.read_adc(2, gain=GAIN)
	#curr1=adc1.read_adc(0, gain=GAIN)
	#volt1Meas=0.512*float(volt1)/32767.0
	vout.append(volt1)
	#print 'Voltage 1: ', volt1Meas
	#time.sleep(tm)
t=np.linspace(0,tf,len(vout))
a=(max(vout)-min(vout))/2.0
#f=a*np.sin(2*np.pi*60*t)+(max(vout)-a)
w=savgol_filter(vout,5,1,mode='nearest')
#w=savgol_filter(vout,11,2)
w=savgol_filter(w,11,1)
print(len(vout))
#plt.plot(t,vout,t,w)
plt.plot(t,w)
plt.show()
adc1.stop_adc()
