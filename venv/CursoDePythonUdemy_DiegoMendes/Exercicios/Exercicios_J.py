"""
Exercícios de fixação - Listas
Curso de Python

Diego Mendes Rodrigues
"""

"""
Exercício 1
---
Faça um script com duas listas: números inteiros (como 4, 5, 1, 8) e outra com caracteres (b, n, e, t).
• Exiba as duas listas na tela.
• Crie uma terceira lista que seja a junção das duas primeiras e exiba na tela.
• Mostre o item com o índice ‘5’ dessa nova lista.
• Mostre todos os elementos da nova lista, cada um em uma linha, usando uma estrutura de laço.

list1 = [1,2,5,4,8,3]
list2 = ['a','b','n','e','t','c']
print('{},\n{}'.format(list1, list2))
list3 = list1 + list2
print(list3)

for i in list3:
    print(list3[i])

Exercício 2
---
Crie um programa onde o usuário final irá digitar nomes de pessoas. Armazene os nomes em uma lista. 
Quando o usuário não digitar nada, ou seja, apenas apertar o <ENTER>, você deve ordenar os nomes 
apresentados e exibir na tela.
Depois solicite que o usuário exclua um dos nomes da lista. 
Você então deve remover esse nome da lista e apresentar a lista final para o usuário na tela outra vez.

lista = []
valor = input('Digite um nome: ')
lista.insert(0,valor)
while valor != "":
    valor = input('Digite outro nome: ')
    lista.append(valor)
lista.sort()
print('{}\nDigite a posição do nome que queira excluir da lista: '.format(lista))
del lista[int(input('Digite o valor: '))]
print(lista)

Exercício 3
---
Iremos solicitar para o usuário digitar o nome e a idade de pessoas. Essas informações devem ser armazenadas 
em uma lista que possui listas dentro dela, como foi visto em aulas anteriores. Quando o usuário não digitar nada, 
ou seja, apenas apertar o <ENTER>, no nome e na idade, você deve apresentar:
• A lista com o nome e a idade das pessoas
• O primeiro e o último item da lista.

list1 = []
list2 = []
lista = [list1,list2]
nome = str(input("Digite um nome: "))
idade = input('Digite a idade do(a) {}: '.format(nome))
while nome != "":
    nome = str(input("Digite um nome: "))
    list1.append(nome)
    idade = input('Digite a idade do(a) {}: '.format(nome))
    list2.append(idade)
print(lista)

Exercício 4
---
Receba números inteiros do usuário final. Depois exiba na tela:
• Os valores digitados pelo usuário ordenados.
• Os valores digitados pelo usuário multiplicados por 50.
• A primeira metade dos itens da lista.

list = []
try:
    num = int(input('Digite um número inteiro: '))
    list.insert(0,num)
    while num != 999:
        num = int(input('Digite outro número inteiro ou 999 para parar: '))
        if num != 999:
            list.append(num)
        else:
            continue
    print(list)
    list.sort()
    print(list)
    for n in list:
        print(n*50)
    metadeIndice = int(len(list)//2)
    print(list[:metadeIndice])
except ValueError:
    print('ERRO: Você não digitou um valor inteiro!!!')

Exercício 5
---
Crie um script com uma lista de números inteiros.
Agora inclua um número no final da lista, depois outro número no início da lista, e finalmente um número 
no índice 2. Exiba o resultado na tela.
Altere o item no índice 3 para uma palavra.
Apague o item no índice 4 e exiba o resultado na tela.
Exiba o último elemento da lista, com a função que já remove esse elemento no momento da exibição.
Mostre e lista final na tela.
"""
lista = [1,2,4,5,10,99,88,16,70]
lista.append(-28)
lista.insert(0,10)
print(lista)
lista[3] = "Joker"
lista.pop(4)
print(lista[-1])
lista.pop(-1)
print(lista)