#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: utf-850 -*-

#Titulo				:caracterizarv0_1.py
#Descripción		:Programa de caracterización.
#Autor          	:Javier Campos Rojas
#Fecha            	:enero-2017
#Versión         	:3.6
#Notas          	:
#==============================================================================

from graphics import *
from button import *
from serialKepco_tmsv2 import *
from HarmGenv2 import *
import matplotlib.pyplot as plt
import numpy as np
import math
import io
import base64
import Tkinter as tk
from urllib2 import urlopen
import glob ##### para buscar los puertos USB disponibles
from controlTektronix import *

def main():
	xgrid=27;
	ygrid=23;
	refy=22;
	refx=2;
	refx2=12;
	width_b=3;
	heigh_b=1.5;
	Tm=0.0005;
	puertos=glob.glob('/dev/tty[U]*')
	try:
		puerto1 = puertos[0]
	except IndexError:
		puerto1 = 'no hay dispositivo'
	try:
		puerto2 = puertos[1]
	except IndexError:
		puerto2 = 'no hay dispositivo'
	
	#### Prueba: barrido de frecuencia ####
	
	
	V=24*np.sqrt(2);
	C=10;
	osc1=getWave();
	for f in range(45,65):
		n=f;
		kepco1.WriteVoltSine(V,f,n,C);
		if (f%2)==0:
			osc1.OscWave();
	
	#### Prueba: Cambio de amplitudes #### 	
	
	
	#### Prueba: inyección de armonicos #### 
	

main()
