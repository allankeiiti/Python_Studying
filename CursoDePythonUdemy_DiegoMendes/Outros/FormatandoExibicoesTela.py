'''
Formatando as exibições da tela - format
'''

cor = input('Escolha uma cor: ')
print('Cor escolhida {:>10}.'.format(cor))
print('Cor escolhida {:<10}.'.format(cor))
print('Cor escolhida {:^10}.'.format(cor))
#No espaço em branco, posso colocar um sinal de igual
print('Cor escolhida {:=<10}'.format(cor))
print('Cor escolhida {:=^10}.'.format(cor))

n1 = n3 = 7
n2 = 3 if n1 == 7 else 0
print('Soma {:10}'.format(n1+n2))
##print('{} {}'.format(n1,n2))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('{} - {} - {:.2f} - {} - {}'.format(s,m,d,di,e), end=' > ')