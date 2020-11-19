'''Ejercicio 1

Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones,
sabiendo que la formula general es la que está en la imagen, el usuario debe ingresar los valores de
 “a”, “b” y “c”, y el programa debe hacer el proceso para que al final muestre el mensaje: “La solución es: <solucion>”'''



a = int(input('ingrese el valor de a: '))

b = int(input('ingrese el valor de b: '))

c = int(input('ingrese el valor de c: '))



#calculo de la raiz cuadrada del problema

CuentaDentroDeLaRaiz = b**2 - (4*a*c)

import math

RaizCuadrada = math.sqrt(CuentaDentroDeLaRaiz)



#Ecuación

Resultado = (b + RaizCuadrada) / (2*a)

print('La solución es:' + Resultado)





