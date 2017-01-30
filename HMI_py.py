from Tkinter import *

root=Tk()
root.title("Control de Fuentes Kepco")
root.geometry("500x300")

app=Frame(root)
app.grid()
button1=Button(app,text="Hello")
button1.grid()

button2=Button(app)
button2.grid()
button2.configure(text="Anybody")

button3=Button(app)
button3.grid()
button3.configure(text="Out there")

root.mainloop()
