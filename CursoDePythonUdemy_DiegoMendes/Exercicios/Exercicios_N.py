'''
Exercícios de fixação - Funções
Curso de Python

Diego M. Rodrigues
'''

'''
Exercício 1
---
Crie um script com as seguintes funções:
• media: Recebe 2 números e retorna a média deles
• meuNome: Exibe o seu nome na tela
• exibeNome: Recebe um nome e um sobrenome, em 2 argumentos, 
retornando o nome completo
• inverso: Recebe uma palavra e exibe o inverso dela, 
por exemplo Curso  osruC

def calculaMedia(num1 , num2):
    media = (num1 + num2) /2
    return int(media)
print(calculaMedia(4,4))

def meuNome(nome, sobrenome):
    nomeCompleto = nome + " " + sobrenome
    return nomeCompleto
print(meuNome('Allan','Nakakita'))

def inverteNome(nome):
    print(nome[::-1])
inverteNome('Allan')

Exercício 2
---
Crie uma lista com carros e seus valores, depois uma função 
onde o usuário informa qual carro ele deseja e ela exiba o valor.
Faça um laço que exiba os carros disponíveis, perguntando para o 
usuário qual o carro que ele deseja saber o valor de venda.

carList =   [[1, 'Nissan Skyline GT-R R34',  330000],
            [2, 'Nissan Skyline GT-R R35',  500000],
            [3, 'Hyundai Sonata GL',         50000],
            [4, 'Lexus LFA',                100000],
            [5, 'Mitsubishi Lancer Evo',    200000],
            [6, 'Nissan Altima 2.5',        200000]]

def ExibeCarList():
    print('ID,      Carro,        Valor')
    print('-'*50)
    for carro in carList:
        id = str(carro[0])
        nome = (carro[1])
        valor = (carro[2])
        print('{}       {}         R#:{:.2f}'.format(id, nome, valor))

def ExibeValor(id = 0):
    print('Carro: {}\nValor: {}.'.format(carList[id][1], carList[id][2]))

while True:
    ExibeCarList()
    print('0 - Sair do programa')
    id = int(input('Digite o carro desejado: '))
    if id == 0:
        break
    ExibeValor(id-1)

Exercício 3
---
Crie uma agenda de telefones, em uma lista, armazenando o nome 
e o telefone de pessoas.
Ao entrar no script o usuário deve enxergar o seguinte menu:
• Listar os contatos
• Exibir informações de um contato
• Incluir um contato
• Apagar um contato
• Sair
Cada opção do menu deve ser realizada por uma função.
'''
agenda =   [[1, 'Allan Keiiti Nakakita' ,'1198323-4535'],
            [2, 'Jonathan Mathie Tigre' ,'1198232-4854'],
            [3, 'Gustavo Mathias'       ,'1123466-7071'],
            [4, 'Teste de Infra'        ,'1345645-3434']]

def exibeMenu():
    print('AGENDA\n{}'.format('-'*60))
    print('1 - Listar Contatos\n2 - Exibir informações de um contato\n3 - Incluir Contato\n4 - Apagar Contato\n0 - Sair')
    print('-' * 60)

def listaContatos():
    print('ID       |       NOME        |   TELEFONE')
    for contato in agenda:
        id = contato[0]
        nome = contato[1]
        cel = contato[2]
        print('{}       {}       {}'.format(id, nome, cel))

def exibeInfoContato():
    cod = int(input('Digite o código do contato: '))
    print('Contato: '+agenda[cod-1][1])
    print('Número: '+agenda[cod-1][2])

def incluirContato():
    nome = input('Digite o nome do contato a ser incluso: ')
    codigo = int(input('Digite o ID para {}: '.format(nome)))
    telefone = int(input('Digite o número do {}: '.format(nome)))
    novoContato = [codigo, nome, telefone]
    agenda.append(novoContato)

def excluirContato():
    codigo = int(input('Digite o código do usuário a ser removido: '))
    agenda.pop(codigo-1)

while True:
    exibeMenu()
    opcao = int(input('Digite uma opção do menu: '))
    if opcao == 1:
        listaContatos()
    elif opcao == 2:
        exibeInfoContato()
    elif opcao == 3:
        incluirContato()
    elif opcao == 4:
        excluirContato()
    elif opcao == 0 or opcao > 4:
        break
