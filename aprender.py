def crearArray ():
   # contar = 0
   cadena = []
   while True:
      nombre = input("Salir o un nombre para hacer una lista_ ")
      if nombre == 'Salir':
         break
      else:
         cadena.append(nombre)
   return cadena
   # while  contar <= numElement:
   #    cadena.append(contar)
   #    contar+= 1
   # return cadena


# lista = crearArray(13)
lista = crearArray()

print(lista)



# calificaciones = [9,9,8,9,8]
# alumno = ["Emanuel Gomez","Rodolfo Carrillo","Samuel fuentes"]
# print(calificaciones.count(9))
# # alumno[1]="otro"
# # print(alumno[0:2])


#def calcular_importe(importe, descuento):
   # return importe-(importe*descuento/100)

#datos = {"descuento":10,"importe":10}
#print(calcular_importe(**datos),datos)
# class Fruta ():
#     def __init__(self,color,forma,size):
#         self.color = color
#         self.forma = forma
#         self.size = size 

#     def dieta(self):
#         if self.color == "verde":
#             mensaje = "Es una fruta para bajar de peso"
#             print(mensaje.center(50,"."))
#         else:
#             print("No es una fruta para bajar de peso")
    
# et = Fruta()
# print( et.color)
# print(et.forma)
# print(et.size)
# print(et.dieta( ))
