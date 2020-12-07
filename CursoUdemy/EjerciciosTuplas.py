"""Ejercicios
Ejercicio 1

Escribir una tupla con los meses del año, luego, pide al usuario un numero, el que haya ingresado, es el mes que debe mostrar en la tupla



Ejercicio 2

Escribir una tupla que tenga las letras del alfabeto. Luego, debes pedir al usuario un número, el que haya ingresado, es la letra que debe imprimir el programa"""

#Ejercicio1

meses = ("No existe el mes 0", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

MesdelUsuario = int(input("Escribe el numero de tu mes preferido: "))

print("Tu mes preferido es: {}".format(meses[MesdelUsuario]))