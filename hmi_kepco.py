from graphics import *
from button import *
import matplotlib.pyplot as plt
import numpy as np
import math


def main():
	win = GraphWin("Control de Fuentes Kepco",width=500, height=200)
	win.setCoords(0,0,10,10)
	win.setBackground("white")
	sin = Button(win, Point(1,9), 2, 1, "sin(wt)")
	sin.activate()
	info = Button(win, Point(1,7), 2, 1, "info")
	info.activate()
	stop = Button(win, Point(1,5), 2, 1, "Stop")
	stop.activate()
	quitButton = Button(win, Point(9,1), 2, 1, "Quit")
	quitButton.activate()
	
	freq=Text(Point(7,9),"Frecuencia(Hz): ")
	freq.setFace('arial')
	freq.setStyle('bold')
	freq.setSize(12)
	freq.setTextColor("black")
	freq.draw(win)
	
	freq_val=Entry(Point(9,9),10)
	freq_val.setFace('arial')
	freq_val.setSize(10)
	freq_val.setTextColor("black")
	freq_val.draw(win)
	
	
	volt=Text(Point(7,7),"Tension(V): ")
	volt.setFace('arial')
	volt.setStyle('bold')
	volt.setSize(12)
	volt.setTextColor("black")
	volt.draw(win)
	
	volt_val=Entry(Point(9,7),10)
	volt_val.setFace('arial')
	volt_val.setSize(10)
	volt_val.setTextColor("black")
	volt_val.draw(win)
	
	period=Text(Point(7,5),"Periodos: ")
	period.setFace('arial')
	period.setStyle('bold')
	period.setSize(12)
	period.setTextColor("black")
	period.draw(win)
	
	period_val=Entry(Point(9,5),10)
	period_val.setFace('arial')
	period_val.setSize(10)
	period_val.setTextColor("black")
	period_val.draw(win)
	
	pt = win.getMouse()
	mensaje=Text(Point(5,2),"")
	mensaje.setFace('arial')
	mensaje.setStyle('bold')
	mensaje.setSize(11)
	mensaje.setTextColor("black")
	mensaje.draw(win)
	while not quitButton.clicked(pt):	
		if sin.clicked(pt):
			
			t2=0.0005;
			n=float(period_val.getText())
			f=float(freq_val.getText())
			T=1.0/f
			V=float(volt_val.getText())
			t=np.arange(0,T,t2)
			funct=V*np.sin(2*math.pi*f*t)
			funct=np.round(funct,2)
			#plt.plot(t,funct)
			#plt.show(block=False)

		if info.clicked(pt):
			graf2=[]
			for i in range(0,len(funct)):
				graf2.append(funct[i])
			plt.plot(t,graf2)
			plt.show(block=False)
		
		if stop.clicked(pt):
			mensaje.setText("Javier")
		pt = win.getMouse()
	win.close()
main()
