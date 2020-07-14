print('FIBONACCI\n')

qnt = int(input('Digite a quantidade de números a visualizar no fibonacci\nNúmero:  '))
i = 0
a = 1;
b = 1;
print(0)
print(a)
print(b)
for i in range(qnt):
    a = a + b
    print(a)
    b = b + a
    print(b)
    i+=1