filename = input('Entender a filename: ')
with open (filename) as f:
    text = f.read()

print(text)
'''
arq = open('cores.txt','w')
Colors = ['Yellow',
          'Red',
          'Blue',
          'Green',
          'Orange',
          'Pink',
          'Purple']

for color in Colors:
    linha = color
    arq.write('\n{}'.format(linha[0]))
arq.close()
#Lendo as linhas do arquivo agora
arq = open('cores.txt','r')

linha = arq.readline()
print(linha)
while len(linha) > 0:
    linha = arq.readline()
    print(linha)
arq.close()
'''