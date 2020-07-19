'''
Listas - Python
'''

num = [8,9,10,11,12]
print(num)
'''
    num.append(20)
    num.insert(0,10)
    num.insert(-1, 44)
    num.insert(-1,55)
    print(num)
'''

num.append(20)
num.insert(0,10)
num.insert(-1, 44)
num.insert(-1,55)
print(num)

num[1] = 'X'
num[-1] = 'K'
print(num)

del num[1]
print(num)

del(num[2:4])
print(num)

#a linha abaixo limpa a lista num inteira
num.clear()
print(num)

#pop é o ultimo valor da lista a ser removido
num = [1,2,3,4,5]
print(num)
print(num.pop(2))
print(num)


lista2 = ['ALLAN','RENNAN','VINYCIUS','BRUNO']
lista2.sort(reverse=True)
print(lista2)
lista2 = ['ALLAN','RENNAN','VINYCIUS','BRUNO']
lista2.reverse()
print(lista2)