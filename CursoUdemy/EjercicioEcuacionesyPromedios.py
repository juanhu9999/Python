'''Ejercicio 1

Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones,
sabiendo que la formula general es la que está en la imagen, el usuario debe ingresar los valores de
 “a”, “b” y “c”, y el programa debe hacer el proceso para que al final muestre el mensaje: “La solución es: <solucion>”'''



a = int(input('ingrese el valor de a: '))

b = int(input('ingrese el valor de b: '))

c = int(input('ingrese el valor de c: '))


#calculo de la raiz cuadrada del problema



from math import sqrt 

CuentaDentroDeLaRaiz = sqrt((b**2) - (4*a*c))

RaizCuadrada = (CuentaDentroDeLaRaiz)



#Ecuación

Resultado = (-b + RaizCuadrada) / (2*a)

print('La solución es: ' + str(Resultado))

#Resolucion del profesor.

#3x^2-5x+2=0 x=1 x=2/3

A = int(input('Ingrese el valor de A:'))
B = int(input('Ingrese el valor de B:'))
C = int(input('Ingrese el valor de C:'))

x1 = 0
x2 = 0

if ((B**2)) - (4*A*C) < 0:
    print('No se puede realizar')
else:
    x1 = (-B + sqrt((B**2) - (4*A*C)))/(2*A)
    x2 = (-B - sqrt((B**2) - (4*A*C)))/(2*A)
print("La solución es:\n x1= ",x1,"\nx2= ",x2)




