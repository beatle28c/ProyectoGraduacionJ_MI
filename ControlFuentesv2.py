from graphics import *
from button import *
from serialKepcov2 import*
import matplotlib.pyplot as plt
import numpy as np
import math


def main():
	refy=20;
	refx=3;
	refx2=13;
	width_b=3;
	heigh_b=1.5;
	
	win = GraphWin("Control de Fuentes Kepco",width=1000, height=300)
	win.setCoords(0,0,20,25)
	win.setBackground("white")
	
	line = Line(Point(10, 0), Point(10, 25))
	
	line.draw(win)
	
	sin = Button(win, Point(refx,refy), width_b, heigh_b, "sin(wt)")
	sin.activate()
	info = Button(win, Point(refx,refy-3), width_b, heigh_b, "info")
	info.activate()
	stop = Button(win, Point(refx,refy-6), width_b, heigh_b, "Stop")
	stop.activate()

	sin2 = Button(win, Point(refx2,refy), width_b, heigh_b, "sin(wt)")
	sin2.activate()
	info2 = Button(win, Point(refx2,refy-3), width_b, heigh_b, "info")
	info2.activate()
	stop2 = Button(win, Point(refx2,refy-6), width_b, heigh_b, "Stop")
	stop2.activate()
	
	connects1 = Button(win, Point(refx+6.5,refy+3), width_b-2.5, heigh_b, "ok")
	connects1.activate()
	connects2 = Button(win, Point(refx2+6.5,refy+3), width_b-2.5, heigh_b, "ok")
	connects2.activate()
	
	quitButton = Button(win, Point(18.5,2), 2, 2, "Quit")
	quitButton.activate()
	
	
	###############################---Datos Fuente 1---###############################
		################## Frecuencia 1 ##################
	
	freq=Text(Point(refx+4,refy),"Frecuencia(Hz): ")
	freq.setFace('arial')
	freq.setStyle('bold')
	freq.setSize(12)
	freq.setTextColor("black")
	freq.draw(win)
	
	freq_val=Entry(Point(refx+6,refy),10)
	freq_val.setFace('arial')
	freq_val.setSize(10)
	freq_val.setTextColor("black")
	freq_val.draw(win)
	
		################## Tension 1 ##################
		
	volt=Text(Point(refx+4,refy-3),"Tension(V): ")
	volt.setFace('arial')
	volt.setStyle('bold')
	volt.setSize(12)
	volt.setTextColor("black")
	volt.draw(win)
	
	volt_val=Entry(Point(refx+6,refy-3),10)
	volt_val.setFace('arial')
	volt_val.setSize(10)
	volt_val.setTextColor("black")
	volt_val.draw(win)
	
		################## Periodos 1 ##################

	period=Text(Point(refx+4,refy-6),"Periodos: ")
	period.setFace('arial')
	period.setStyle('bold')
	period.setSize(12)
	period.setTextColor("black")
	period.draw(win)
	
	period_val=Entry(Point(refx+6,refy-6),10)
	period_val.setFace('arial')
	period_val.setSize(10)
	period_val.setTextColor("black")
	period_val.draw(win)
	
		################## Puerto Serial 1 ##################

	
	port1_name=Text(Point(refx,refy+3),"Puerto Serial 1: ")
	port1_name.setFace('arial')
	port1_name.setStyle('bold')
	port1_name.setSize(12)
	port1_name.setTextColor("black")
	port1_name.draw(win)
	
	port1_val=Entry(Point(refx+4,refy+3),25)
	port1_val.setFace('arial')
	port1_val.setSize(10)
	port1_val.setTextColor("black")
	port1_val.draw(win)
	
	#############################################################################################3
	
	###############################---Datos Fuente 2---###############################
		################## Frecuencia 2 ##################
	
	freq2=Text(Point(refx2+4,refy),"Frecuencia(Hz): ")
	freq2.setFace('arial')
	freq2.setStyle('bold')
	freq2.setSize(12)
	freq2.setTextColor("black")
	freq2.draw(win)
	
	freq2_val=Entry(Point(refx2+6,refy),10)
	freq2_val.setFace('arial')
	freq2_val.setSize(10)
	freq2_val.setTextColor("black")
	freq2_val.draw(win)

		################## Tension 2 ##################

	volt2=Text(Point(refx2+4,refy-3),"Tension(V): ")
	volt2.setFace('arial')
	volt2.setStyle('bold')
	volt2.setSize(12)
	volt2.setTextColor("black")
	volt2.draw(win)
	
	volt2_val=Entry(Point(refx2+6,refy-3),10)
	volt2_val.setFace('arial')
	volt2_val.setSize(10)
	volt2_val.setTextColor("black")
	volt2_val.draw(win)
	
		################## Periodos 2 ##################
		
	period2=Text(Point(refx2+4,refy-6),"Periodos: ")
	period2.setFace('arial')
	period2.setStyle('bold')
	period2.setSize(12)
	period2.setTextColor("black")
	period2.draw(win)
	
	period2_val=Entry(Point(refx2+6,refy-6),10)
	period2_val.setFace('arial')
	period2_val.setSize(10)
	period2_val.setTextColor("black")
	period2_val.draw(win)
	
		################## Puerto Serial 2 ##################
	
	port2_name=Text(Point(refx+10,refy+3),"Puerto Serial 2: ")
	port2_name.setFace('arial')
	port2_name.setStyle('bold')
	port2_name.setSize(12)
	port2_name.setTextColor("black")
	port2_name.draw(win)
	
	port2_val=Entry(Point(refx+14,refy+3),25)
	port2_val.setFace('arial')
	port2_val.setSize(10)
	port2_val.setTextColor("black")
	port2_val.draw(win)
	
	#'/dev/ttyUSB0'
	
		################## Mensaje de lectura ##################
	mensaje=Text(Point(5,2),"")
	mensaje.setFace('arial')
	mensaje.setStyle('bold')
	mensaje.setSize(11)
	mensaje.setTextColor("black")
	mensaje.draw(win)
	port1=port1_val.getText()
	port1='/dev/tty'+port1;
	port2=port1_val.getText()
	port2='/dev/tty'+port2;
	pt = win.getMouse()
	#kepco1=Source("Fuente1",port1)
	#kepco2=Source("Fuente1",port2)
	while not quitButton.clicked(pt):
		
		if connects1.clicked(pt):
			kepco1=Source("Fuente1",port1)
			
		if connects2.clicked(pt):
			kepco2=Source("Fuente1",port2)	
		if sin.clicked(pt):
			
			"""
			V=float(volt_val.getText())
			kepco1.WriteVolt(V)
			"""
			
			ts=0.0005;
			n=float(period_val.getText())
			f=float(freq_val.getText())
			T=1.0/f
			V=float(volt_val.getText())
			t=np.arange(0,T,ts)
			funct=V*np.sin(2*math.pi*f*t)
			funct=np.round(funct,2)
			kepco1.WriteVoltSine(funct,t,f,n,ts)
			
			"""
			t2=1;
			n=float(period_val.getText())
			f=float(freq_val.getText())
			T=1.0/f
			V=float(volt_val.getText())
			t=np.arange(0,T,t2)
			funct=[0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,9.0,8.0,7.0,6.0,5.0,4.0,3.0,2.0,1.0]
			funct=np.round(funct,2)
			kepco1.WriteVoltSine(funct,t,f,n,t2)
			"""
		if sin2.clicked(pt):
			ts2=0.0005;
			n2=float(period_val2.getText())
			f2=float(freq_val2.getText())
			T2=1.0/f2
			V2=float(volt_val2.getText())
			t2=np.arange(0,T,ts2)
			funct2=V2*np.sin(2*math.pi*f2*t2)
			funct2=np.round(funct2,2)
			kepco2.WriteVoltSine(funct2,t2,f2,n2,ts2)

		if info.clicked(pt):
			source1=kepco1.identify()
			print(source1)
			mensaje.setText(source1)
		
		if info2.clicked(pt):
			source2=kepco2.identify()
			print(source2)
			mensaje.setText(source2)
		
		if stop.clicked(pt):
			graf=[]
			for i in range(0,len(ts)):
				meas=kepco1.stop()
				graf.append(float(meas))
				print(meas)
				mensaje.setText(meas)
			plt.plot(t,graf)
			plt.show(block=False)
		
		if stop2.clicked(pt):
			graf2=[]
			for i in range(0,len(ts2)):
				meas2=kepco2.stop()
				graf.append(float(meas2))
				print(meas2)
				mensaje.setText(meas2)
			plt.plot(t2,graf2)
			plt.show(block=False)
			
		pt = win.getMouse()
	win.close()
main()
