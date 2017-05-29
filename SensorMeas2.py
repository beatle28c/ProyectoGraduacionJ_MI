import time
import Adafruit_ADS1x15 as ADC
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter
import RPi.GPIO as GPIO

##PWM y IO de la Raspberry##
Led=14;
GPIO.setwarnings(False);
GPIO.setmode(GPIO.BCM)
GPIO.setup(Led, GPIO.OUT,initial=GPIO.HIGH)
GPIO.output(Led, GPIO.LOW);
time.sleep(1)


adc1 = ADC.ADS1115()

# Ganancias
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V

GAIN = 16

#Volt2.start_adc(2, gain=GAIN)
adc1.start_adc(1, gain=GAIN, data_rate=860)
#Curr1.start_adc(0, gain=GAIN)
vout=[]
tm=0.00001;
tf=0.5
start = time.time()
while (time.time() - start) <= tf:
	volt1 = adc1.get_last_result()
	#volt1=adc1.read_adc(1, gain=GAIN, data_rate=860)
	#volt2=adc1.read_adc(2, gain=GAIN)
	#curr1=adc1.read_adc(0, gain=GAIN)
	#volt1Meas=0.512*float(volt1)/32767.0
	vout.append(volt1)
	#print 'Voltage 1: ', volt1Meas
	#time.sleep(tm)
GPIO.output(Led, GPIO.HIGH);
t=np.linspace(0,tf,len(vout))
vout=np.array(vout)
Cal=460.5659
volt1Meas=Cal*vout/32767.0
a=max(volt1Meas)-((max(volt1Meas)-min(volt1Meas))/2.0)
volt1Meas=volt1Meas-a
w=savgol_filter(volt1Meas,5,1,mode='nearest')
#w=savgol_filter(w,11,1)
print(max(volt1Meas)/np.sqrt(2))
plt.style.use('ggplot')
#plt.plot(t,vout,t,w)
plt.plot(t,w)
#plt.plot(t,vout)
plt.show()
adc1.stop_adc()
