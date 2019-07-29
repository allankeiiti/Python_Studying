'''
Exercícios de Python para a assimilação do conteúdo de Estrutura de Repetição
Curso de Python

Diego M. Rodrigues
'''

'''
Exercício 1
---
Faça um script que mostre na tela uma contagem regressiva, de 10 até 0,
com uma pausa de 1 segundo entre cada exibição.
Dica: Para pausar você pode utilizar time.sleep().

from time import sleep
for n in range(10,-1,-1):
    print(n)
    sleep(1)
    
Exercício 2
---
Exiba na tela todos os números ímpares entre 1 e 50.
for n in range(1,50,2):
    print(n)

Exercício 3
---
Calcule a soma de todos os números ímpares que são múltiplos de 3
no intervalo de 1 até 500.
soma = 0
for n in range(1,500,1):
    if(n%3) == 0:
        soma = soma + n
print(soma)

Exercício 4
---
Solicite um número para o usuário final, depois exiba a tabuada desse
número utilizando o laço for.

Exercício 5
---
Crie um script que leia 6 números inteiros do usuário.
Mostre a soma apenas dos números pares que foram digitados.


Exercício 6
---
O usuário irá digitar um número, depois o script irá dizer se
esse é um número primo.


Exercício 7
---
Crie um script que leia o ano de nascimento de 5 pessoas.
Depois o script mostra quantas pessoas já atingiram a maioridade
e quantas não atingiram.
Dica: Maior de idade é quem já possui 18 anos ou mais.


Exercício 8
---
Leia o peso de 5 pessoas.
Depois, mostre o maior e o menor pesos digitados.


Exercício 9
---
Leia uma frase do usuário.
Exiba essa frase de trás para frente.
Exemplo: 'Curso de Python' --> 'nohtyP ed osruC'
frase = input('Digite uma frase: ')
for n in range(len(frase)-1,-1,-1):
    print(frase[n])
    
Exercício 10
---
Leia uma frase do usuário.
Exiba essa frase sem as vogais.
Exemplo: 'Curso de Python' --> 'Crs d Pythn'
'''

frase = input('Digite uma frase: ')
for n in frase:
    if n in 'aeiou':
        continue
    else:
        print(n)