'''

n = 0
for n in range(n,20,2):
    print('\033[1;20;40m{}\033[m'.format(n))
numbers = [2,3,4,5]
total = 0
for num in numbers:
    if num < 5 and num >2:
        print('Arroba',total)
        total+=num
print(total)

for c in 'Allan Keiiti Nakakita':
    if c in 'la':
        continue
    print(c)
'''
soma = 0
for c in range(0,3):
    n = int(input('Digite um número entre 0 e 10: \nA soma máxima será 20!'))
    if n >= 0 and n <= 10:
        soma = soma + n
    else:
        print('Você não digitou um número entre 0 e 10. {} não será utilizado!'.format(n))

    if soma >= 20:
        soma = 20
        print('Valor máximo da soma atingido')
        break
print('Soma = {}'.format(soma))