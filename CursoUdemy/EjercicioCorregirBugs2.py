"""El siguiente fragmento de código tiene un total de 7 bugs (O tal vez más, o tal vez menos), tu deber es encontrarlos, corregirlos, pasar el código a tu editor de código y verificar que estén resueltos. Fíjate muy bien en el código, no solo pueden haber errores de sintaxis...



variable1 = int("Ingresa el primer número: ")    # FALTA EL INPUT

variable2 = input("Ingresa el segundo número: ") #FALTA EL INT



resultado = varible1 + varable2 #variable1 esta mal escrito y variable2 tambien, es una multiplicación, no una suma.



print("El resultado de multiplicacion de ambos numeros es de: [ ]"format(resutado))) #SON {} NO [] Y FALTA EL . ANTES DE FORMAT. Y TIENE UN PARENTESIS DE MAS AL FINAL, RESULTADO ESTA MAL
ESCRITO.

"""

#CODIGO CORREGIDO

variable1 = int(input("Ingresa el primer número: "))   

variable2 = int(input("Ingresa el segundo número: ")) 


resultado = variable1 * variable2 


print("El resultado de multiplicacion de ambos numeros es de: {}".format(resultado))