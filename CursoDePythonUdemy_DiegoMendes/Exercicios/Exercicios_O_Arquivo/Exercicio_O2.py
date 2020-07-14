carro = str(input('Digite o nome de um carro | Digite nada para parar: '))
arq = open('carros.txt','w')
if carro != "":
    arq.write(carro+'\n')
    while carro != "":
        carro = str(input('Digite o nome de um carro | Digite nada para parar: '))
        arq.write(carro + '\n')
arq.close()

#Realizando leitura do carros.txt

arq = open('carros.txt','r')
linha = arq.readline()
print(linha)
while len(linha) > 0:
    linha = arq.readline()
    print(linha)

