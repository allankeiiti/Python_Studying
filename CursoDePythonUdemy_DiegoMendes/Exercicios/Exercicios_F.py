'''
Ex:1
Faça um script que o computador sorteia um número inteiro entre 0 e 5. Depois o usuário deve tentar advinhar
o número escolhido pelo computador. No final o script deverá escrever na tela se o usuário venceu ou perdeu, ou seja,
se ele acertou ou não o número sorteado pelo computador.

import random
lista = [1,2,3,4,5]
sorteado = int(random.choice(lista))
print(sorteado)
escolha = int(input('Digite um valor de 1 a 5: '))
if escolha > 0 and escolha <=5:
    if escolha == sorteado:
        print('Parabéns! Você advinhou o número que a máquina selecionou!')
    else:
        print('Você perdeu!')
else:
    print('Você digitou um número inválido!!!')

Ex:2
Pergunte ao usuário a velocidade do carro dele. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi
multado, A multa vai custar R$5,00 para cada Km acima do limite de velocidade.

velocidade = float(input('Digite a velocidade do carro do usuário: '))
if velocidade > 80.0:
    print('Usuário ultrapassou a velocidade com {} Km/h a mais. A sua multa será de R$: {:.2f}.'.format(velocidade-80, (velocidade-80)*5))
else:
    print('Usuário não ultrapassou a velocidade.')

Ex:3
Faça um programa que o usuário entre com um número inteiro e você mostra se ele é impar ou par

numero = int(input('Digite um valor: '))
if numero%2 == 0:
    print('O número {} é par!'.format(numero))
else:
    print('O número {} é impar!'.format(numero))

Ex:4
Faça um script onde o usuário digita o ano e ele indica se o ano é bissexto
'''

try:
    ano = int(input('Digite um ano: '))
except ValueError:
    print('Digite um valor do tipo inteiro!!!')
if ano%4 == 0:
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))