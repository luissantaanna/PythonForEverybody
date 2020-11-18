#jugueteria, calcula el peso del pedido segun la cantidad de su contenido.

payaso = 112
muneca = 75

cp = float(input("Ingrese el numero de payasos en el pedido: "))
cm = float(input("Ingrese el numero de munecas en el pedido: "))

pa = cp * payaso
pm = cm * muneca

total = pa + pm
tot = float(total)
print("El peso del pedido es de " + str(tot))
