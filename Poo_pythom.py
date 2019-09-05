"""class MiClaseEjemplo:
    esto es un ejemplo de clase poo en pythom

    entero = 2345
    def mensaje(self,msj):
        print(msj)
x = MiClaseEjemplo()
y = MiClaseEjemplo()

print(x.entero)
print(y.mensaje("hola como estas"))"""
import random

continuar = 1
while continuar == 1:
    print("Bienvenido a Yumartermint")
    print("Elija la dificultad del juego <1=East 2=hard 3= Nightmare>")
    dificultad = int(input("Dígite el numero de dificultad"))
    #Cantidad de dificultas
    if dificultad == 1:
        cant_digitos = 3
    elif dificultad == 2:
        cant_digitos = 4
    elif dificultad == 3:
        cant_digitos = 5
    digitos = ("0","1","2","3","4","5","6","7","8","9")
    codigo = ""
    for i in range(cant_digitos):
        elegido = random.choice(digitos)
        while elegido in codigo:
            elegido = random.choice(digitos)
        codigo = codigo + elegido
    print("Tienes que adivinar un codigode ", cant_digitos,"digitos distintos")
    propuesta = input("Qué digitos propones jugador")

    intentos = 1

    while propuesta != codigo:
        intentos =  intentos + 1
        aciertos = 0
        coincidencias = 0
        for i in range(cant_digitos):
            if propuesta[i] == codigo[i]:
                aciertos = aciertos + 1
            elif propuesta[i] != codigo:
                coincidencias = coincidencias +1
        print("Tu propuesta(", propuesta,")tiene",aciertos,"Aciertos y ", coincidencias,"Coincidencia")
        propuesta = input("Propon otro código")
    print("FELICIDADES adivinate el codigo en", intentos, "intentos")
    continuar = int(input("Desea seguir jugando 1=si 0=no"))
