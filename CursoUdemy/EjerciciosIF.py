"""Ejercicio 1

Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal



Ejercicio 2

Escribir un programa que, dado un número entero, muestre su valor absoluto. Nota: para los números positivos su valor absoluto es igual al número
 (el valor absoluto de 52 es 52), mientras que, para los negativos, su valor absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52)."""


#Ejercicio1

Letra = input("ingresa una letra: ")

if Letra in "aeiouAEIOU" :
    print("Es vocal")
else:
    print("no es vocal")

#Ejercicio2

Numero = 10

if Numero >= 0 :
    print(Numero)
else :
    print(Numero * -1)


#El profesor los resolvio de la misma manera