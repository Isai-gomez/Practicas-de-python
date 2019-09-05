#import turtle

# Las dos líneas siguientes son necesaias para hacer
# compatible el interfaz Tkinter con los programas basados
# en versiones anteriores a la 8.5, con las más recientes.

#from tkinter import *    # Carga módulo tk (widgets estándar)
#from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)

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
#el_mundo_es_plano = True
#if el_mundo_es_plano:
#    print("Tener cuidado de no caerte")

#segundo ejemplo de python
#impuesto = 12.5 / 100
#precio = 100.50
#print("Precio es /t",precio)
#print("Impuesto es/t",impuesto)
#print("Total es /t",precio * impuesto)
#print(3 * r"cd\documetos\rabajos"+' que paso'  )
#print("Se cobra ",precio )

# Segundo ejemplo con cadenas
#texto = ('Esto es algo que es muy largo , puedecontener muchos textos para que el usuario los vea en la pantalla')
#palabra = 'saludo'
#t("\print La palabra es " + palabra +" "+ " La palabra que se hace es\t" + palabra[0:3]+ palabra[4:6])
#print(palabra[:6] + palabra[4:])


#comienza unnuevo ejemplo donde anexamos un registro a una cadena
#cadena = "Es to es una cadena muy larga"
#print('sulodo' + cadena[8:])
#print( cadena[8:] + 'saludo')
#print(len(cadena))

#Ejemplos de listas
#como definir una lista en python (tienen que ser del mismo tipo o diferentes
#cuadrados = [4,5,6,7,2,67,23]
#print(cuadrados)
#print('la lista es la siguinte  I see good')
#print( cuadrados[5:])# sacar rebanadas

#print(cuadrados + [12,34])
#cuadrados.append(12)
#print(len(cuadrados))

# INICIANODO CON  LA PROGRAMACION
#a, b = 0, 1
#while b < 20:
#  print(b, end=',')
 # a, b = b, a+b


# SENTENCIAS IF EJEMPLOS
#x = int(input("Ingresa un entero porfabor"))
#if x < 0:
#	x = 0
#	print('negativo cambiado a cero')
#elif x == 0:
#	print('cero')
#elif x == 1:
#	print('Simple')
#else:
#	print('Mas')

#palabras = ['gato','ventana','condensador']
#for p in palabras:
#	print(p, len(p))
#print(palabras[:])
#for p in palabras[:]:
#	if len(p) > 6:
#		palabras.insert(0, p)
#print(palabras)
#----------------------------
#Combertir de json a python
#----------------------------
#import json

# some JSON:
#x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
#y = json.loads(x)

# the result is a Python dictionary:
#print(y["name"])
#-------------------
#Conbertir de python a json
#import json

# a Python object (dict):
#x = {
 # "name": "John",
  #"age": 30,
 # "city": "New York"
#}

# convert into JSON:
#y = json.dumps(x)

# the result is a JSON string:
#print(y)
#---------
#Matriz
#---------

"""#ropa = ["Camizas","Playeras","Pantalo", "Trusa", "Short","Pantis"]
#for x in ropa:
#	print(x)
#d=0
#c=""
#print("\n")
#while d <= 10:
    c = input("Ingresa prenda de ropas\n")
    s = input("Ingresa n para salir \t # enter para seguir capturando") #21 para salir
    if s == "n":
        break
    ropa.append(c)
    d+=1
print("\ncon todos los datos agragados\n\n")
for x in ropa:
	print(x)
"""
#uso del while
"""while True:
	nombre = input("Indique su nombre: ")
	if nombre:
		break
"""
#uso del for 
#for anio in range(2001, 2013):
#	print("Informes del Año", str(anio))
"""
monto_bruto = 175
tasa_interes = 12
monto_interes = monto_bruto * tasa_interes / 100
print(monto_interes)
"""
# tumplas no se pueden modificar ellas 
#mi_tumpla = ("Nombre",12,23,"SEXO")
#for i in mi_tumpla:
#	print(i)

#lista es diferente se pueden modificar
"""mi_lista = ["Nombre",12,23,"SEXO"]
for i in mi_lista:
	print(i)
#modificar lista
mi_lista[0] = 22
print(mi_lista)"""

# diccionarios tinen etiquetas
"""
mi_dic = {'Nombre':'isai','edad':12,'altura':23,'SEXO':"mujer"}
for i in mi_dic:
	print(i)
#modificar lista y eliminar contenido
mi_dic['Nombre'] = 22
print(mi_dic)
del(mi_dic['Nombre'])
print(mi_dic)
"""

#condiciones if elif else
"""semaforo = input("Color del semaforo\t")
if semaforo == 'verde':
	print("Cruzar la carretera")
else:
	print('Esperar un tiempo')
"""
def informe():
	año = 2000
	while año <= 2018:
		return("Informe del año ",año) 
		año+=1 	
	
a = informe()	
print(a)	
	

