'''
Exercícios de fixação - Strings
Curso de Python

Diego M. Rodrigues
'''

'''
Exercício 1
---
Solicite que o usuário entre com o primeiro nome de uma pessoa, depois 
solicite o sobrenome.
Crie uma variável que irá armazenar o nome completo, depois exiba 
o nome completo na tela.
Exiba o 2º caractere do nome e o 3º do sobrenome.

nome = input('Digite o primeiro nome: ')
if nome != "":
    sobrenome = input('Digite o sobrenome do {}: '.format(nome))
    nomeCompleto = nome + sobrenome
    print(nomeCompleto)
    print("{}\n{}".format(nome[1], sobrenome[2]))
else:
    print('O usuário não digitou um nome!')

Exercício 2
---
Nesse programa você irá trabalhar com a string ‘Curso de Python na Web’.
Altere a palavra Python para SQL e exiba na tela.
Quebre a frase utilizando como delimitador os espaços, depois, exiba os 
elementos com índice 0, 3 e 4 da lista.
string = 'Curso de Python na Web'
string2 = string.replace('Python','SQL')
print(string2)
string2 = string2.split(' ')
print(string2[0])
print(string2[3])
print(string2[4])

Exercício 3
---
Crie uma lista com as principais cores, como branco, preto, vermelho, 
azul, amarelo, verde, etc.
Solicite que o usuário digite uma cor.
Utilize a comparação para verificar se a cor digitada está na lista.

cores = ['Azul','Laranja','Verde','Vermelho']
corDigitada = input('Digite uma cor: ')
if corDigitada in cores:
    print('A cor {} está disponível nesta lista!'.format(corDigitada))
else:
    print('A cor {} não está disponível nesta lista!'.format(corDigitada))

Exercício 4
---
Crie um script que o usuário precisa entrar com uma frase.
Troque os espaços da frase pelo caractere de escape referente a 
uma quebra de linha.
Exiba a nova frase na tela.

frase = input('Digite uma frase: ')
frase2 = frase.replace(" ","\n")
print(frase2)

Exercício 5
---
Nesse script o usuário precisa entrar com uma palavra, depois, 
utilizando um laço, exiba cada caractere em uma linha, sendo 
que em cada linha você deve adicionar o caractere de escape 
de tabulação.
'''

wordUser = input('Digite uma palavra e tecle [ENTER]: ')
tab = ''
for n in wordUser:
    print(n + tab)
    tab +='\t'
