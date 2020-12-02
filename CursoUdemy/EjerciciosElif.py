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

if Palabra1[-3:] == Palabra2[-3:]:
    print("Estas palabras riman!")

elif Palabra1[-2:] == Palabra2[-2:]:
    print("Estas palabras riman un poco!")

else:
    print("Estas palabras no riman")

#Ejercicio2

Candidatos = input("Elija su candidato: candidato A por el partido rojo, candidato B por el partido verde, candidato C por el partido azul. ")

if Candidatos in "Aa" :
    print("Ha escogido {}. Usted ha votado por el partido rojo".format(Candidatos.upper()))
elif Candidatos in "Bb" :
    print("Ha escogido {}. Usted ha votado por el partido verde".format(Candidatos.upper()))
elif Candidatos in "Cc" :
    print("Ha escogido {}. Usted ha votado por el partido azul".format(Candidatos.upper()))
else :
    print("Ha escogido {}. Esta opcion es erronea".format(Candidatos.upper()))

#Resolución del profesor.

primerpablabra = input("Ingrese su primera palabra: ")
segundapalabra = input("Ingrese su segunda palabra: ")

if len(primerpablabra) < 3 or len(segundapalabra) < 3:
    print("No riman, por que una de ellas tiene menos de 3 caracteres")
elif primerpablabra[-3:] == segundapalabra[-3:]:
    print("las palabras riman")
elif primerpablabra[-2:] == segundapalabra[-2:]:
    print("Riman un poco")
else:
    print("Estas palabras no riman")