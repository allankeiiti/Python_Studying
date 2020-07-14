'''
Exercícios de fixação - Dicionários
Curso de Python

Diego M. Rodrigues
'''

'''
Exercício 1
---
Faça um script onde você irá armazenar as seguintes informações 
de pessoas: nome; sobrenome; idade; peso.
Depois exiba as informações na tela da seguinte forma:
NOME SOBRENOME com IDADE anos está com PESO kg.

dicionario = {'Allan':('Allan','Nakakita','20','55.5'),
              'Kaue':('Kaue','Sloboda','20','100'),
              'Helder':('Helder','Nako','19','70'),
              'Bruno Ferreira':('Bruno','Ferreira','25','70')}

for chave, valor in dicionario.items():
    print('{} {} com {} anos está com {} kg.'.format(valor[0],valor[1],valor[2],valor[3]))

Exercício 2
---
O usuário deverá entrar com o número de cada apartamento de 
um prédio junto com o nome do proprietário. A chave deve ser 
o número do apartamento. Depois que as informações forem 
enviadas, exiba o resultado na tela.

chaves = []
valores = []
numero = int(input('Insira o número do apartamento. Digite 0 para parar: '))
chaves.append(numero)
nome = str(input('Insira o nome do proprietário do apartamento {}: '.format(numero)))
valores.append(nome)
while numero != 0:
    numero = int(input('Insira o número do apartamento. Digite 0 para parar: '))
    if numero != 0:
        chaves.append(numero)
        nome = str(input('Insira o nome do proprietário do apartamento {}: '.format(numero)))
        valores.append(nome)
print(chaves)
print(valores)
dicionario = dict(zip(chaves, valores))
print(dicionario)

Exercício 3
---
Um professor deve entrar com 3 notas de um aluno. Recebe essas 
3 notas em um dicionário com chaves 0, 1 e 2.
Depois, exiba as 3 notas e solicite que o professor exclua uma 
delas. Exiba a média das notas restantes.

chaves = [0,1,2]

notas = []
try:
    for i in chaves:
        nota = float(input('Digite a nota {} do aluno: '.format(i+1)))
        notas.append(nota)
    dic = dict(zip(chaves,notas))
    print(dic)
    notaRemove = int(input('Digite a chave da nota a ser removida: '))
    dic.pop(notaRemove)
    print(dic)
    soma = 0
    for valor in dic.values():
        soma += valor
    print('Média: {}.'.format(soma/2))
except ValueError:
    print('ERRO! Você digitou um valor inválido!')

Exercício 4
---
Iremos atender nesse script uma loja que vende carros usados. 
Primeiro crie um dicionário com o nome dos carros, com seu ano
e seu valor.
Depois, solicite para o funcionário da loja digitar o nome 
de um carro.
Caso o carro esteja no dicionário, exiba o ano e o valor. 
Caso não esteja, exiba que a loja não possui esse carro.

INCOMPLETO!
carList = {'350z':('Nissan 350z','97','70.000'),
      'GT-R':('Nissan GT-R R35','00','200.000'),
      'F50':('ferrari F50','00','3.000.000')}
print(carList)
carSelected = str(input('Select a Car from the list: '))
while carSelected not in carList:
    print('This car is unavaiable in the store.')
    carSelected = str(input('Select a Car from the list: '))

Exercício 5
---
Iremos criar uma agenda de telefones. O usuário irá entrar 
com o nome e com o telefone de cada pessoa. 
Esses valores serão armazenados em Listas do Python.
Quando o usuário terminar de entrar com os valores, 
crie um dicionário de acordo com as listas, depois exiba na tela.
'''

nameList = []
phoneList = []

nameInserted = str(input('Digite um nome | Digite nada para parar: '))
nameList.append(nameInserted)
while nameInserted != "":
    nameInserted = str(input('Digite um nome | Digite nada para parar: '))
    if nameInserted != "":
        nameList.append(nameInserted)
for i in nameList:
    phoneInserted = int(input('Digite um número para o {} (Somente Números): '.format(i)))
    phoneList.append(phoneInserted)
contacts = dict(zip(nameList,phoneList))

for chave, valor in contacts.items():
    print('Contato: {} | Telefone: {}'.format(chave, valor))

'''
A linha abaixo cria um dicionário a partir de 2 listas
essaVariavelEUmDicionario = dict(zip(lista1,lista2))
'''