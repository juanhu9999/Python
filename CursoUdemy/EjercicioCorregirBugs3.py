"""El siguiente fragmento de código tiene un total de aproximadamente 8 Bugs. Ya sabes... tu labor es encontrarlos, luego, corregir dichos errores y verificar con tu editor de código que todo esté bien



nombre = int(input('Ingresa tu nombre: ')) #ESTA UTILIZANDO INT PARA UN STRING



if Nombre = "Maria" #NO PUSO LOS : AL FINAL. FALTA UN =

    print('Hola Maria')

elf Nombe == "Carlos":  #ES ELIF, NO ELF. LA VARIABLE ESTA MAL ESCRITA

    print("Hola Carlos")

elif nombre == 'Juan': #LA VARIABLE ESTA EN MINUSCULA.

    print("Hola Carlos") #DEBERIA SER HOLA JUAN.

else nombre == None: #NO HAY QUE PONER NADA DESPUES DEL ELSE.

    print("No te tengo en mis registros")"""

nombre = input('Ingresa tu nombre: ')

if nombre == "Maria":
    print('Hola Maria')

elif nombre == "Carlos":
    print("Hola Carlos")

elif nombre == 'Juan':
    print("Hola Juan")

else:
    print("No te tengo en mis registros")
