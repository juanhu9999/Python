"""Ejercicio 1

En la siguiente lista, debes hacer un programa que muestre los valores al usuario, a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el primer y 
segundo lugar:

[20, 50, "Curso", 'Python', 3.14]

Ejercicio 2

Escribe una lista que tenga los números de 1 al 10. Luego, debes hacer que los datos que están en las posiciones 4, 7 y 9 sean multiplicados por 2; por último, 
mostrar la lista nueva con los nuevos datos"""

[20, 50, "Curso", 'Python', 3.14]

#Ejercicio1

Valores = [20, 50, "Curso", 'Python', 3.14]

print(Valores)
dato1 = input("Ingresa el primer dato: ")
dato2 = input("Ingresa el segundo dato: ")

Valores[0] = dato1 
Valores[1] = dato2

print(Valores)

#Ejercicio2

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista)

lista[4] = lista[4] * 2
lista[7] = lista[7] * 2
lista[9] = lista[9] * 2
print(lista)

#Resolución del profesor:

Lista1 = [20, 50, "Curso", 'Python', 3.14]

print(Lista1)

Palabra1 = input("Ingrese el primer valor a modificar dentro de la lista: ")
Palabra2 = input("Ingrese el segundo valor a modificar dentro de la lista: ")

Lista1[0] = Palabra1
Lista1[1] = Palabra2

print("El nuevo valor de la lista1 es: {}".format(Lista1))



