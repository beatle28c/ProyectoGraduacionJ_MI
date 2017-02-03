import matplotlib.pyplot as plt
import numpy as np
t = np.linspace(0,1,1000)
f=60
Tp=1/f
x=np.sin(2*np.pi*f*t)
L=len(x)
Fs=1000;
Y = np.fft.fft(x)
freq = np.fft.fftfreq(t.shape[-1])
plt.plot(freq, Y.real)
plt.show()
