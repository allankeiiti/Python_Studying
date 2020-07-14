#arq = open('file.txt','r')

#linhas = arq.read()
#print(linhas)

arq = open('file2.txt','r')

#cod = arq.read(3)
#print(cod)
#nome = arq.read(5)
#print(nome)
#traco = arq.read(2)

#lista = arq.readlines()
#print(lista)
#for linha in lista:
#    print(linha)
linha = arq.readline()

while len(linha) > 0:
    print(linha)
    linha = arq.readline()
arq.close()