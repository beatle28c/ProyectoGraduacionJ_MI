from graphics import *
from button import *
from serialKepcov3_3 import*

import matplotlib.pyplot as plt
import numpy as np
import math


def main():
	refy=20;
	refx=3;
	refx2=13;
	width_b=3;
	heigh_b=1.5;
	Tm=0.0005;
	
	win = GraphWin("Control de Fuentes Kepco",width=1000, height=300)
	win.setCoords(0,0,20,25)
	#win.setBackground('#BCC6CC')
	myImage = Image(Point(10,12.5), '/home/javier/backg.gif')
	myImage.draw(win)
	
	line = Line(Point(10, 0), Point(10, 25))
	line.setFill("white")
	line.setWidth(2)
	line.draw(win)
	
	sin = Button(win, Point(refx,refy), width_b, heigh_b, "sin(wt)")
	sin.activate()
	info = Button(win, Point(refx,refy-3), width_b, heigh_b, "info")
	info.activate()
	trian = Button(win, Point(refx,refy-6), width_b, heigh_b, "Triangular")
	trian.activate()
	#meas = Button(win, Point(refx,refy-6), width_b, heigh_b, "Medir V1")
	#meas.activate()
	stop = Button(win, Point(refx,refy-9), width_b, heigh_b, "Stop")
	stop.activate()

	sin2 = Button(win, Point(refx2,refy), width_b, heigh_b, "sin(wt)")
	sin2.activate()
	info2 = Button(win, Point(refx2,refy-3), width_b, heigh_b, "info")
	info2.activate()
	trian2 = Button(win, Point(refx2,refy-6), width_b, heigh_b, "Triangular")
	trian2.activate()
	#meas2 = Button(win, Point(refx2,refy-6), width_b, heigh_b, "Medir V")
	#meas2.activate()
	stop2 = Button(win, Point(refx2,refy-9), width_b, heigh_b, "Stop")
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
	#freq.setTextColor("#8EB84A")
	freq.setTextColor("black")
	freq.draw(win)
	
	freq_val=Entry(Point(refx+6,refy),10)
	freq_val.setFace('arial')
	freq_val.setSize(10)
	freq_val.setTextColor("white")
	freq_val.setFill('#6B6B6B')
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
	volt_val.setTextColor("white")
	volt_val.setFill('#6B6B6B')
	volt_val.draw(win)

		################## Corriente 1 ##################
		
	curr=Text(Point(refx+4,refy-6),"Corriente(A): ")
	curr.setFace('arial')
	curr.setStyle('bold')
	curr.setSize(12)
	curr.setTextColor("black")
	curr.draw(win)
	
	curr_val=Entry(Point(refx+6,refy-6),10)
	curr_val.setFace('arial')
	curr_val.setSize(10)
	curr_val.setTextColor("white")
	curr_val.setFill('#6B6B6B')
	curr_val.draw(win)
	
		################## Periodos 1 ##################

	period=Text(Point(refx+4,refy-9),"Periodos: ")
	period.setFace('arial')
	period.setStyle('bold')
	period.setSize(12)
	period.setTextColor("black")
	period.draw(win)
	
	period_val=Entry(Point(refx+6,refy-9),10)
	period_val.setFace('arial')
	period_val.setSize(10)
	period_val.setTextColor("white")
	period_val.setFill('#6B6B6B')
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
	port1_val.setTextColor("white")
	port1_val.setFill('#6B6B6B')
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
	freq2_val.setTextColor("white")
	freq2_val.setFill('#6B6B6B')
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
	volt2_val.setTextColor("white")
	volt2_val.setFill('#6B6B6B')
	volt2_val.draw(win)

		################## Corriente 2 ##################

	curr2=Text(Point(refx2+4,refy-6),"Corriente(A): ")
	curr2.setFace('arial')
	curr2.setStyle('bold')
	curr2.setSize(12)
	curr2.setTextColor("black")
	curr2.draw(win)
	
	curr2_val=Entry(Point(refx2+6,refy-6),10)
	curr2_val.setFace('arial')
	curr2_val.setSize(10)
	curr2_val.setTextColor("white")
	curr2_val.setFill('#6B6B6B')
	curr2_val.draw(win)

		################## Periodos 2 ##################
		
	period2=Text(Point(refx2+4,refy-9),"Periodos: ")
	period2.setFace('roman')
	#period2.setStyle('bold')
	period2.setSize(12)
	period2.setTextColor("black")
	period2.draw(win)
	
	period2_val=Entry(Point(refx2+6,refy-9),10)
	period2_val.setFace('arial')
	period2_val.setSize(10)
	period2_val.setTextColor("white")
	period2_val.setFill('#6B6B6B')
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
	port2_val.setTextColor("white")
	port2_val.setFill('#6B6B6B')
	port2_val.draw(win)
	
	#'/dev/ttyUSB0'
	
		################## Mensaje de lectura ##################
	mensaje=Text(Point(5,6),"")
	mensaje.setFace('arial')
	mensaje.setStyle('bold')
	mensaje.setSize(11)
	mensaje.setTextColor("black")
	mensaje.draw(win)
	
	mensaje2=Text(Point(15,6),"")
	mensaje2.setFace('arial')
	mensaje2.setStyle('bold')
	mensaje2.setSize(11)
	mensaje2.setTextColor("black")
	mensaje2.draw(win)
	
	port2=port1_val.getText()
	port2='/dev/tty'+port2;
	pt = win.getMouse()
	#kepco1=Source("Fuente1",port1)
	#kepco2=Source("Fuente1",port2)
	#kepco1=Source("Fuente1")
	
	while not quitButton.clicked(pt):
		
		if connects1.clicked(pt):
			port1=port1_val.getText()
			port1=port1.upper();
			port1='/dev/tty'+port1
			kepco1=Source("Fuente1",port1)
			estado=kepco1.connectport()
			mensaje.setText(estado)
			#estado=kepco1.connect()
			#mensaje.setText(estado)
			
		if connects2.clicked(pt):
			port2=port2_val.getText()
			port2=port2.upper()
			port2='/dev/tty'+port2;
			kepco2=Source("Fuente2",port2)
			estado=kepco2.connectport()
			mensaje2.setText(estado)
		
		
		
		if trian.clicked(pt):
			
			#ts=0.001;
			n=float(period_val.getText())
			f=float(freq_val.getText())
			V=float(volt_val.getText())
			C=float(curr_val.getText())
			T=1.0/f
			ts=Tm;
			m=T/ts;
			m=round(m/2)*2;
			t=np.arange(0,T,ts)
			funct1=V*np.arange(0,1,1/(m/2))
			funct2=V*np.arange(1,0,-1/(m/2))
			funct=np.concatenate([funct1,funct2])
			funct=np.round(funct)
			if len(t) < len(funct):
				m=len(t);
				funct=funct[0:m]
				t=t[0:m]
			elif len(funct) < len(t):
				m=len(funct);
				funct=funct[0:m]
				t=t[0:m]
			kepco1.WriteTrian(funct,t,f,n,ts,C)
			#plt.plot(t,funct)
			#plt.show(block=False)
			
		if trian2.clicked(pt):
			n2=float(period_val2.getText())
			f2=float(freq_val2.getText())
			V2=float(volt_val2.getText())
			C2=float(curr_val2.getText())
			T2=1.0/f2
			ts2=Tm;
			m2=T2/ts2;
			m2=round(m2/2)*2;
			t2=np.arange(0,T2,ts2)
			funct2=V2*np.sin(2*math.pi*f2*t2)
			if len(t2) < len(funct2):
				m2=len(t2);
				funct2=funct2[0:m2]
				t2=t2[0:m2]
			elif len(funct2) < len(t2):
				m2=len(funct2);
				funct2=funct[0:m2]
				t2=t[0:m2]
			"""
			m=m/2;
			funct=funct[0:m]
			t=t[0:m]
			"""
			funct2=np.round(funct2,3)
			kepco2.WriteVoltSine(funct2,t2,f2,n2,ts2,C2)
			#plt.plot(t,funct)
			#plt.show(block=False)
		
		if sin.clicked(pt):

			n=float(period_val.getText())
			f=float(freq_val.getText())
			V=float(volt_val.getText())
			C=float(curr_val.getText())
			T=1.0/f
			ts=Tm;
			m=T/ts;
			m=round(m/2)*2;
			
			t=np.arange(0,T,ts)
			funct=V*np.sin(2*math.pi*f*t)
			if len(t) < len(funct):
				m=len(t);
				funct=funct[0:m]
				t=t[0:m]
			elif len(funct) < len(t):
				m=len(funct);
				funct=funct[0:m]
				t=t[0:m]
			funct=np.round(funct,3)
			kepco1.WriteVoltSine(funct,t,f,n,ts,C)
			#plt.plot(t,funct)
			#plt.show(block=False)

		if sin2.clicked(pt):
			n2=float(period_val2.getText())
			f2=float(freq_val2.getText())
			V2=float(volt_val2.getText())
			C2=float(curr_val2.getText())
			T2=1.0/f2
			ts2=Tm;
			m2=T2/ts2;
			m2=round(m2/2)*2;
			t2=np.arange(0,T2,ts2)
			funct2=V2*np.sin(2*math.pi*f2*t2)
			if len(t2) < len(funct2):
				m2=len(t2);
				funct2=funct2[0:m2]
				t2=t2[0:m2]
			elif len(funct2) < len(t2):
				m2=len(funct2);
				funct2=funct[0:m2]
				t2=t[0:m2]
			funct2=np.round(funct2,3)
			kepco2.WriteVoltSine(funct2,t2,f2,n2,ts2,C2)
			#plt.plot(t,funct)
			#plt.show(block=False)

		if info.clicked(pt):
			source1=kepco1.identify()
			print(source1)
			mensaje.setText(source1)
		
		if info2.clicked(pt):
			source2=kepco2.identify()
			print(source2)
			mensaje.setText(source2)

		if stop.clicked(pt):
			kepco1.stop()
		if stop2.clicked(pt):
			kepco2.stop()
		pt = win.getMouse()
	win.close()
main()
