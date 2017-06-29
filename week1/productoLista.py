lista = []

for pos in range(0,5):
    valor = input("Ingrese valor ")
    lista.append(valor)

print(lista)

producto = int(lista[0])
for x in lista:
    producto = int(x) * producto
print(producto)