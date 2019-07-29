'''
Ex.1
Crie um script que leia o sexo de uma pessoa, acenitanto M ou F.
Caso o usuári digite um valor errado, solicite novamente até que ele digite o correto

sexo = str(input('Digite seu sexo (M e F apenas): '))

while sexo.lower() not in 'mf':
    sexo = str(input('Digite seu sexo (M e F apenas): '))

if sexo.lower() == 'm':
    print('Seu Sexo é Masculino!')
else:
    print('Seu sexo é feminino!')

Ez:2
Sorteia de 1 a 10
Advinhar qual foi o número que o comp. sorteou. Quando acertar, exibir as tentativss)

from random import randint
Number = randint(1,10)
trialTime = 0
print(Number)
trialNumber = int(input('Digite o número: '))
while trialNumber != Number:
    if(trialTime < 7):
        trialTime += 1
        trialNumber = int(input('Errou! {} tentativas. Digite outro número: '.format(trialTime)))
    else:
        print('Você perdeu! Ultrapassou o limite de tentativas!')
        break
print('Você Venceu! {} tentativas!'.format(trialTime))


'''

