#print(2 in [1,2,3,4,5])

lista = [1,2,2,3,4,5,6]

if 2 in lista:
    print("A")
else:
    print("B")
print(lista.count(2))

if 10 and 1 not in lista:
    print("não há 10 na lista")
else:
    print("há 10 e 1 na lista")

if 10 or 3 not in lista:
    print("há 10 ou 3 na lista")
else:
    print("não há 10 ou 3 na lista")

x = 10
y = 20
z = 30
num = int(input('Digite um número: '))
if num == x or num == y or num == z:
    print('O número está na lista')
else:
    print('O número não está na lista')

if num in [x,y,z]:
    print('O número está na lista')
else:
    print('O número não está na lista')