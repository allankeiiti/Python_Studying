'''
Ex>1
Crie um script que leia o nome completo de uma pessoa, depois mostre:
O nome com todas as letras maiusculas
O nome com todas as letras minusculas
Quantas letras tem o nome sem considerar os espaços?
Quantas letras possui o primeiro nome?

nome = input('Digite um nome completo: ')

print(nome)
print(nome.upper())

print(nome.lower())

frase = nome.replace(" ","")
frase = " ".join(frase.split())
print('{} \nCount: {}'.format(frase,len(frase)))

nome2 = (nome.split())

nome3 = nome2[0]

print(len(nome3))

Ex:2
O user vai digitar um numero entre 0 e 999. então exiba cada um dos dígitos separados
Ex: 547 - unidade: 7 dezenha 4 centena 5

try:
    numero = (input('Digite um valor entre 0 e 999: '))
    if int(numero) < 10:
        print('Unidade: {}.'.format(numero))
        print('Dezena : 0.')
        print('Centena: 0.')
    elif int(numero) < 100:
        print('Unidade: {}.'.format(numero[1]))
        print('Dezena : {}.'.format(numero[0]))
        print('Centena: 0.')
    else:
        print('Unidade: {}.'.format(numero[2]))
        print('Dezena : {}.'.format(numero[1]))
        print('Centena: {}.'.format(numero[0]))
except(ValueError):
    print('Digite um valor numérico!!!')

Ex:3
O user entra com o nome de uma cidade
Analisar se o nome da cidade começa ou não com 'SÂO'

cidade = input('Digite o nome de uma cidade: ')
cadeia = (cidade.split(' '))
if(cadeia[0].lower() == 'são'):
    print('A cidade {} começa com São!'.format(cidade))
else:
    print('A cidade {} não começa com São!'.format(cidade))

Ex:4
Verifique se o nome de uma pessoa possui SILVA nele
nome = input('Digite um nome: ')
teste = nome.lower().find('silva')
if(teste<0):
    print('O nome digitado não possui Silva.')
else:
    print('O nome digitado possui Silva.')


Ex;5
Nesse script, o usuário irá entrar com uma frase, de saída fica:
Quantas vezes apareceu a letra A
Em que posição ela aparece pela primeira vez
Em que posição ela aparece pela última vez
'''
frase = input('Digite uma frase: ')
letra = input('Digite a letra que você quer saber quantas vezes apareceu nesta frase: ')
print('A letra {} apareceu: {} vezes.'.format(letra, frase.lower().count(letra)))
print('A letra {} aparaece pela primeira vez na posição {}'.format(letra, frase.lower().find(letra)))
print('A letra {} aparaece pela ultima vez na posição {}'.format(letra, frase.lower().rfind(letra)))
