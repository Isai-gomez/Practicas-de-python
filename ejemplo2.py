#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Las dos líneas siguientes son necesaias para hacer 
# compatible el interfaz Tkinter con los programas basados 
# en versiones anteriores a la 8.5, con las más recientes. 

#from tkinter import *    # Carga módulo tk (widgets estándar)
#from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
#import Tkinter
#from Tkinter import *
#from tkinter import ttk
# Define la ventana principal de la aplicación

#raiz = Tk()

# Define las dimensiones de la ventana, que se ubicará en 
# el centro de la pantalla. Si se omite esta línea la
# ventana se adaptará a los widgets que se coloquen en
# ella. 

#raiz.geometry('300x200') # anchura x altura

# Asigna un color de fondo a la ventana. Si se omite
# esta línea el fondo será gris

#raiz.configure(bg = 'beige')

# Asigna un título a la ventana

#raiz.title('Aplicación')

# Define un botón en la parte inferior de la ventana
# que cuando sea presionado hará que termine el programa.
# El primer parámetro indica el nombre de la ventana 'raiz'
# donde se ubicará el botón

#ttk.Button(raiz, text='Salir', command=quit).pack(side=BOTTOM)

# Después de definir la ventana principal y un widget botón
# la siguiente línea hará que cuando se ejecute el programa
# construya y muestre la ventana, quedando a la espera de 
# que alguna persona interactúe con ella.

# Si la persona presiona sobre el botón Cerrar 'X', o bien,
# sobre el botón 'Salir' el programa llegará a su fin.

#raiz.mainloop()
#from tkinter import *
 
#app = Tk()
#app.title("Aplicacion grafica en python")
#etiqueta = Label(app, text="Hola mundo!!!")
#boton = Button(app, text="OK!!")
 
#etiqueta.pack()
#boton.pack()
#app.mainloop() 
import sys
from tkinter import *
 
def hacer_click():
 try:
  _valor = int(entrada_texto.get())
  _valor = _valor * 5
  etiqueta.config(text=_valor)
 except ValueError:
  etiqueta.config(text="Introduce un numero!")
 
 
app = Tk()
app.title("Mi segunda App Grafica")
 
#Ventana Principal
vp = Frame(app)
vp.grid(column=0, row=0, padx=(50,50), pady=(10,10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)
 
etiqueta = Label(vp, text="Valor")
etiqueta.grid(column=2, row=2, sticky=(W,E))
 
boton = Button(vp, text="OK!", command=hacer_click)
boton.grid(column=1, row=1)
 
valor = ""
entrada_texto = Entry(vp, width=10, textvariable=valor)
entrada_texto.grid(column=2, row=1)
 
app.mainloop()
