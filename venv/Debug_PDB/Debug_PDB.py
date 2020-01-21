import pdb

lista = ['1', 'b', 'a', 'x']
lista2 = []
for i in lista:
    lista2.append(i)
    pdb.set_trace()
    lista2.append(i + "|a")

print(lista2)