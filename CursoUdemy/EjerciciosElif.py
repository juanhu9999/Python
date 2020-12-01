"""Ejercicio 1

Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos últimas tiene que decir 
que riman un poco y si no, que no riman.



Ejercicio 2

Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verde, 
candidato C por el partido azul. Según el candidato elegido (A, B ó C) se le debe imprimir el mensaje “Usted ha votado por el partido [color que corresponda al candidato elegido]”. 
Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar “Opción errónea”.

Pista: Si la letra ingresada por el usuario es en minúscula, el programa debe convertirla en mayúscula"""

#Ejercicio1

Palabra1 = input("Ingresa la primer palabra: ")
Palabra2 = input("Ingresa la segunda palabra: ")

if Palabra1[-3] == Palabra2[-3]:
    print("Estas palabras riman!")

elif Palabra1[-2] == Palabra2[-2]:
    print("Estas palabras riman un poco!")

else:
    print("Estas palabras no riman")

