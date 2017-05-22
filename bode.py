#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

Lx=75e-6;Ly=116e-6;Lz=70.05e-6;
Lw=65.04e-6;Lq=80.75e-6;
L1=Lx+Ly+Ly;
L2=Lw+Lq;
C=670e-6;
L3=103.39e-3;
fr1=(1/(2*np.pi))*np.sqrt((L1+L2+L3)/(L1*C*(L2+L3)));
fr2=(1/(2*np.pi))*np.sqrt((L1+L2)/(L1*C*L2));

HlclL=signal.lti([1],[L1*C*(L2+L3), 0, L1+L2+L3, 0]);
Hlcl =signal.lti([1],[L1*C*L2, 0, L1+L2, 0]);

#s1 = signal.lti([1], [1, 1])
w1, mag1, phase1 = signal.bode(Hlcl)
w2, mag2, phase2 = signal.bode(HlclL)
plt.figure()
plt.subplot(2,1,1)
plt.semilogx(w1, mag1,label='Filtro LCL', linewidth=1.5)
plt.xlim([10e1,10e4])
plt.title('Respuesta en frecuencia'.decode('utf-8'),fontsize=16);
plt.grid(True)
plt.ylabel('Magnitud (dB)',fontsize=14)
plt.xlabel('Frecuencia(rad/s)',fontsize=14)
plt.subplot(2,1,2)
plt.semilogx(w1, phase1)  # Bode phase plot
plt.xlim([10e1,10e4])
plt.ylabel('Fase ('+'$^\circ$'+')',fontsize=14)
plt.xlabel('Frecuencia(rad/s)',fontsize=14)
plt.grid(True)
plt.tight_layout()
plt.savefig('bode1.png')
plt.show()
