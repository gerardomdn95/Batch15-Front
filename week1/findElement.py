lista = []

for pos in range(0,5):
    valor = input("Type an element ")
    lista.append(valor)

print(lista)
x = input("Type an element to find ")
pos = (lista.index(x))

if pos != 0:
    print("I found the element in the position %s"% (pos))
else:
    print("Sorry, the element is not in the list.")