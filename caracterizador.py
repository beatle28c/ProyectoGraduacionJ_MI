#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: utf-850 -*-

#Titulo				:RutinaCaracterizador.py
#Descripción		:Interfaz de usuario y control de fuentes marca Kepco del SESLab.
#Autor          	:Javier Campos Rojas
#Fecha            	:Marzo-2017
#Versión         	:1.0
#Notas          	:
#==============================================================================

from graphics import *
from button import *
import serialKepco_tmsv3 as SK
from HarmGenv3 import *
import matplotlib.pyplot as plt
import numpy as np
import math
import io
import base64
import Tkinter as tk
from urllib2 import urlopen
import glob ##### para buscar los puertos USB disponibles
#from controlTektronix import *
global SK

def main():

	while not quitButton.clicked(pt):
		puertos=glob.glob('/dev/tty[U]*')
		try:
			puerto1 = puertos[0]
		except IndexError:
			puerto1 = 'no hay dispositivo'
		try:
			puerto2 = puertos[1]
		except IndexError:	
			puerto2 = 'no hay dispositivo'
		port1_val.setText(puerto1)
		port2_val.setText(puerto2)
		try:
			mensaje.setText(puerto1)
			mensaje2.setText(puerto2)
		except Exception, e:
			mensaje.setText('no hay dispositivo')
			mensaje2.setText('no hay dispositivo')
		
			
		if connects1.clicked(pt):
			port1=port1_val.getText()
			kepco1=SK.Source("Fuente1",port1)
			m1=kepco1.connectport()
			m2=kepco1.identify()
			mensaje.setText(m1 + "\n" + m2)
			
		if connects2.clicked(pt):
			port2=port2_val.getText()
			kepco2=SK.Source("Fuente2",port2)
			m1=kepco2.connectport()
			m2=kepco2.identify()
			mensaje2.setText(m1 + "\n" + m2)
		
		if dcout.clicked(pt):
			V=float(volt_val.getText())
			C=float(curr_val.getText())
			kepco1.WriteVolt(V,C)
		
		if dcout2.clicked(pt):
			V2=float(volt2_val.getText())
			C2=float(curr2_val.getText())
			kepco2.WriteVolt(V2,C2)
		
		if currM.clicked(pt):
			V=float(volt_val.getText())
			C=float(curr_val.getText())
			estado=kepco1.WriteCurr(V,C)
			mensaje.setText(estado)
		
		if currM2.clicked(pt):
			V2=float(volt2_val.getText())
			C2=float(curr2_val.getText())
			estado2=kepco2.WriteCurr(V2,C2)
			mensaje2.setText(estado2)
						
		if Harm.clicked(pt):
			y1=harm_val.getText();
			y1=y1.split(',');
			y=[int(i) for i in y1]
			n=float(period_val.getText())
			f=float(freq_val.getText())
			V=float(volt_val.getText())
			C=float(curr_val.getText())
			kepco1.WriteHarm(V,f,n,C,y)

		if Harm2.clicked(pt):
			y3=harm2_val.getText()
			y2=[];
			for i in range(0,len(y3),2):
				y2.append(int(y3[i]))
			n2=float(period2_val.getText())
			f2=float(freq2_val.getText())
			V2=float(volt2_val.getText())
			C2=float(curr2_val.getText())
			kepco2.WriteHarm(funct2,f2,n2,C2)
		
		if sin.clicked(pt):
			n=float(period_val.getText())
			f=float(freq_val.getText())
			V=float(volt_val.getText())
			C=float(curr_val.getText())
			#ts=float(tsm.getText())
			kepco1.WriteVoltSine(V,f,n,C)

		if sin2.clicked(pt):
			n2=float(period2_val.getText())
			f2=float(freq2_val.getText())
			V2=float(volt2_val.getText())
			C2=float(curr2_val.getText())
			kepco2.WriteVoltSine(V2,f2,n2,C2)

		if info.clicked(pt):
			source1=kepco1.identify()
			print(source1)
			mensaje.setText(source1)
		
		if info2.clicked(pt):
			source2=kepco2.identify()
			print(source2)
			mensaje2.setText(source2)
		
		if cal.clicked(pt):
			execfile('calv2.py')	
		
		if stop.clicked(pt):
			kepco1.stop()
			
		if stop2.clicked(pt):
			kepco2.stop()
		"""	
		if caracterizar.clicked(pt):
			#osc1=getWave()
			#osc1.OscWave()
		"""
		pt = win.getMouse()
	win.close()
main()
