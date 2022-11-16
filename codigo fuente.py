import socket
from datetime import datetime
from tkinter import *
from tkinter import Button, Entry, Label, Tk

from requests import get

nombre= socket.gethostname()
ip = get('https://api.ipify.org').text
fecha = datetime.now()
formatted_date = fecha.strftime('%d-%m-%y %H-%M')
ventana =Tk()
ventana.title("IP LOGGER")
ventana.geometry("500x300")
ventana.config(bg="lightpink")
def ipprint():
    n1= ('{}'.format(ip))
    n2= ('{}'.format(nombre))
    n3= ('{}'.format(formatted_date))
    txt1.insert(0,n1)
    txt2.insert(0,n2)
    txt3.insert(0,n3)

def agregar():
    f = open("db.txt", "a")
    f.writelines('\n')
    f.writelines('{}'.format(nombre))
    f.writelines('\n')
    f.writelines('{}'.format(formatted_date))
    f.writelines('\n')
    f.writelines('{}'.format(ip))
    f.writelines('\n')
    f.close()

def abrir():
    texto = open("db.txt",'r')
    coso=texto.read()
    tabla.insert(END,coso)
    texto.close()

#------------------------LABEL---------------------------  
lbl = Label(ventana, text="IP LOGGER", font="times", fg="white", bg="lightpink3").place(relx=0.05, rely=0.01, relwidth=0.25,relheight=0.05)

lbl1=Label(ventana, text="Internet Protocol", bg="lightpink3")
lbl1.place(relx=0.05, rely=0.1, relwidth=0.25,relheight=0.1)

lbl2=Label(ventana, text="Nombre De La PC", bg="lightpink3")
lbl2.place(relx=0.05, rely=0.25, relwidth=0.25,relheight=0.1)

lbl3=Label(ventana, text="Fecha y Hora", bg="lightpink3")
lbl3.place(relx=0.05, rely=0.4, relwidth=0.25,relheight=0.1)
#-----------------------TESTO-----------------------------
txt1=Entry(ventana,text="IP",bg="lightgray")
txt1.place(relx=0.35, rely=0.1, relwidth=0.3,relheight=0.08)

txt2=Entry(ventana,text="nombre",bg="lightgray")
txt2.place(relx=0.35, rely=0.25, relwidth=0.3,relheight=0.08)

txt3=Entry(ventana,text="fecha",bg="lightgray")
txt3.place(relx=0.35, rely=0.4, relwidth=0.3,relheight=0.08)

tabla = Text(ventana,bg="lightgray") 
tabla.place(relx=0.05, rely=0.55,relwidth=0.6,relheight=0.5)
#--------------------------BOTONES-----------------------
btn1=Button(ventana,text="dar ip",bg="PaleVioletRed1", command=ipprint)
btn1.place(relx=0.75, rely=0.1, relwidth=0.1,relheight=0.1)

btn2=Button(ventana,text="agregar",bg="PaleVioletRed1", command=agregar)
btn2.place(relx=0.75, rely=0.25, relwidth=0.1,relheight=0.1)

btn3=Button(ventana,text="Ver Tabla",bg="PaleVioletRed1", command=abrir)
btn3.place(relx=0.75, rely=0.4, relwidth=0.1,relheight=0.1)

ventana.mainloop()