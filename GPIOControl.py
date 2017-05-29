#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: utf-850 -*-

#Titulo				:MicroInverterPVCharacterization(MIPVC).py
#Descripción		:Interfaz de usuario y control de fuentes marca Kepco del SESLab.
#Autor          	:Javier Campos Rojas
#Fecha            	:Marzo-2017
#Versión         	:1.0
#Notas          	:
#==============================================================================

from graphics import *
from button import *
import matplotlib.pyplot as plt
import numpy as np
import math
import io
import base64
import Tkinter as tk
from urllib2 import urlopen
import glob ##### para buscar los puertos USB disponibles
#from controlTektronix import *
import tkFileDialog
from fft_medicionv1_4 import *
import RPi.GPIO as GPIO

def main():
	relay=14;
	xgrid=30;
	ygrid=30;
	refy=15;
	refx=15;
	refx2=12;
	width_b=9;
	heigh_b=3;
	Tm=0.0005;
	GPIO.setwarnings(False);
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(relay, GPIO.OUT,initial=GPIO.HIGH)
		
	win = GraphWin("MicroInverter Characterization",width=500, height=200)
	win.setCoords(0,0,ygrid,xgrid)
	#win.setBackground('#BCC6CC')
	background = Image(Point(15,15), 'back2.gif')
	background.draw(win)
	logoTEC = Image(Point(22,25), 'TEC.gif')
	logoTEC.draw(win)
	LogoSESLab = Image(Point(7,25), 'SESLab.gif')
	LogoSESLab.draw(win)
	
	Encender = Button(win, Point(refx-7,refy), width_b, heigh_b, "Encender")
	Encender.activate()
	Apagar = Button(win, Point(refx+7,refy), width_b, heigh_b, "Apagar")
	Apagar.activate()
	Salir = Button(win, Point(refx+7,refy-8), width_b, heigh_b, "Salir")
	Salir.activate()
	
		################## Mensaje de lectura ##################
	mensaje=Text(Point(refx,refy-12),"")
	mensaje.setFace('arial')
	mensaje.setStyle('bold')
	mensaje.setSize(11)
	mensaje.setTextColor("black")
	mensaje.draw(win)
	
	
	pt = win.getMouse()
	
	while not Salir.clicked(pt):

		if Encender.clicked(pt):
			GPIO.output(relay, GPIO.LOW);
		if Apagar.clicked(pt):
			GPIO.output(relay, GPIO.HIGH);	

		pt = win.getMouse()
	win.close()
main()
