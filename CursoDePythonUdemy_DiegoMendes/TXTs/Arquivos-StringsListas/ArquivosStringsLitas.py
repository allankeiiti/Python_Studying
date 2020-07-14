lista = [[1,'Allan Keiiti',20,983234535],
        [2,'Allancerevo XIII',2,121212],
        [3,'Identity is my id',32,12331],
        [4,'INETCPL.CPL',23,1212121212],
        [5,'forceuninstall',13,131231231]]


arq = open('file2.txt','w')

#item = lista[0]
#print('Código: {}'.format(item[0]))
#print('Nome: {}'.format(item[1]))
#print('Idade: {}'.format(item[2]))
#print('Cel: {}'.format(item[3]))

#Cod: 5
#Nome: 40 caracteres
#idade: 2 caracteres
#telefone: 35 caracteres
for item in lista:

    cod = item[0]
    nome = item[1]
    idade = item[2]
    cel = item[3]

    registro = '{: <5} {: <40} {: <2} {: >35}'.format(cod, nome, idade, cel)
    arq.write('\n{}'.format(registro))

arq.close()