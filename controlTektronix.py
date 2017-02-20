#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: utf-850 -*-

#Titulo				:ControlFuentesv3_6.py
#Descripción		:Interfaz de usuario y control de fuentes marca Kepco del SESLab.
#Autor          	:Javier Campos Rojas
#Fecha            	:enero-2017
#Versión         	:3.6
#Notas          	:
#==============================================================================

from graphics import *
from button import *
from serialKepcov3_5 import *
from HarmGenv2 import *
import numpy as np
import math
import io
import base64
import usbtmc
import glob ##### para buscar los puertos USB disponibles
import datetime

class getWave:
	def __init__(self):
		osc=usbtmc.Instrument(1689, 870)
		self.osc=osc
		tek=osc.ask('*IDN?'))
		fecha=datetime.datetime.now()
		self.fecha=fecha;
		return tek

	def OscWave(self):
		foldername=str(fecha.day)+str(fecha.month)+str(fecha.hour)+str(fecha.minute);
		crearFolder='FILES:MKDir "A:'+r'\"'+foldername+r'\"'
		self.osc.write(crearFolder) ###Debe tener un largo de 7 caractéres
		guarda1='SAV:WAVE CH1, "A:'+r'\'+foldername+r'\'+'CH1'+foldername002.CSV"'
		self.osc.write('SAV:WAVE CH1, "A:\C000002\CCH1002.CSV"')
		guarda2=
		self.osc.write('SAV:WAVE CH2, "A:\C000002\CCH2002.CSV"') 
		guarda3=
		self.osc.write('SAV:IMA "A:\C000002\C000002.PNG"')
		guarda4=
		self.osc.write('SAV:SETU "A:\C000002\C000002.SET"')	
		
		
