#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import math
import Graficador as PQ
import tkFileDialog
from graphics import *
from button import *


def main():
	xgrid=100;
	ygrid=60;
	refy=15;
	refx=90;
	refx2=12;
	width_b=12;
	heigh_b=2.5;
	win = GraphWin("Análisis de Calidad de Energía",width=1000, height=600)
	win.setCoords(0,0,xgrid,ygrid)
	BG = Image(Point(12,15), 'backg.gif')
	BG.draw(win)
	line = Line(Point(xgrid-20, 0), Point(xgrid-20, ygrid))
	line.setFill("black")
	line.setWidth(2)
	line.draw(win)
	global PQ;
	osc1=PQ.fft_osc();
	
	SearchFile = Button(win, Point(refx,refy-6), width_b, heigh_b, "Buscar Archivo")
	SearchFile.activate()
	Salir = Button(win, Point(refx,refy-10), width_b, heigh_b, "Salir")
	Salir.activate()
		
	pt = win.getMouse()
	while not Salir.clicked(pt):

		if SearchFile.clicked(pt):
			file_name=[]
			file_name=tkFileDialog.askopenfilenames(initialdir='/media',filetypes=[('CSV files', '*.CSV'), ('all files', '*')])
			data=osc1.file(file_name,1,4);
			Medicion = Image(Point(xgrid/2-10,ygrid/2), 'grafico1.png')
			Medicion.draw(win)
			print(data)
			
		pt = win.getMouse()
	win.close()
main()
