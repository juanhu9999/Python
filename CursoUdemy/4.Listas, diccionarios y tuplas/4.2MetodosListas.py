Lista = ["Tomate", "Cebolla", "Huevos", "Leche", "Arroz"]
Lista2 = [1, 2, 3, 4, 5]
Lista3 = [6, 7, 8, 9, 10]
Lista4 = ['d', 'f', 'a', 'b', 'e', 'c']

Lista.append(50)
print(Lista)

del Lista[3]
print(Lista)

Lista2.extend(Lista3)
print(Lista2)

Lista.remove("Arroz")
print(Lista)

Lista4.sort()
print(Lista4)