#listaCriada = [[1,'Allan','SP','SP'],
#               [2,'Fulano','RJ','RJ'],
#               [3,'Bruno','MG','MG'],
#               [4,'Snake','MT','MT'],
#               [5,'Kleber','TO','TO']]

#arq = open('convidados.txt','w')

#for item in listaCriada:
#    valor = '{:8},{:>40},{:30},{:2}\n'.format(item[0],item[1],item[2],item[3])
 #   arq.write(valor)

#arq.close()

arqRead = open('convidados.txt','r')

linha = arqRead.readline()
codigo = linha[0:8]
nome = linha[8:49]
cidade = linha[49:79]
estado = linha[79:83]

print(linha)
print(codigo + nome + cidade + estado)
