"""Ejercicio 1

Escribir un programa que solicite al usuario un vocal en minuscula, y luego una letra en mayúsculas. El programa debe convertir la letra en minúscula y la vocal en mayúscula, y al final, deben ser concatenadas ambas



Ejercicio 2

Hacer un programa que pida al usuario su nombre, su edad y su sexo y los muestre de la siguiente forma:

Te llamas: <nombre>

Tu edad es: <edad>

Eres: <sexo>

"""

#Ejercicio 1

VocalMinuscula = input("Ingresa una vocal en minuscula: ") 

LetraMayuscula = input("Ingresa una letra en mayuscula: ")

print(VocalMinuscula.upper(), LetraMayuscula.lower())

#Ejercico 2

nombre = input("indica tu nombre: ")

edad = input("indica tu edad: ")

sexo = input("indica tu sexo: ")

print("Te llamas {}, tu edad es {}, y eres {}".format(nombre, edad, sexo))

#Resolución del profesor

vocal = input("Ingrese una vocal en minuscula: ")
letra = input("Ingrese una letra en mayuscula: ")

print("Tu vocal es: {}, tu letra es: {}, y la combinación de ambas es: {}".format(vocal.upper(), letra.lower(), vocal.upper()+letra.lower()))
