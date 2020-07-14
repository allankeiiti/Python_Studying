arq = 'arquivo.txt'

try:
    arqx = open(arq,'r')
    # arqx.write('try:\ncatch')
    print(arqx.read())
    arqx.close()
except IOError:
    print('Não encontrei o arquivo {} ou não tenho permissões para acessar'.format(arq))