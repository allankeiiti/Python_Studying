
#nome = str(input('Digite o nome para o arquivo: '))
#arq = open('{}.txt'.format(nome),'r')
arq = open('file.txt','r')

linha = arq.readline()

while len(linha) > 0:

    cod = linha[0:4]
    nome = linha[4:45]
    idade = linha[45:47]
    telefone = linha[47:100]

    print('\nCódigo..: {}'.format(cod))
    print('Nome....: {}'.format(nome))
    print('Idade...: {}'.format(idade))
    print('Telefone: {}'.format(telefone))

    linha = arq.readline()

arq.close()