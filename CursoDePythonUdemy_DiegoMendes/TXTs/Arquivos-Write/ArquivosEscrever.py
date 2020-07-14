arq = open('teste.txt','w')
indice = 1000
while indice < 2000:
    arq.write('{} - Curso de Writting\n'.format(indice+1))
    indice+=1
arq.close()

# COPIANDO DADOS DO AMIGOS.TXT PARA TESTE.TXT
arq1 = open('teste.txt','a')
arq2 = open('amigos.txt','r')
linhas = arq2.read()
arq1.write(linhas)
arq1.close()
arq2.close()

# COPIANDO DADOS DO AMIGOS.TXT PARA TESTE.TXT, querendo copiar todos menos a Ju
arq1 = open('teste.txt','a')
arq2 = open('amigos.txt','r')
while True:
    texto = arq2.readline()
    if texto == '':
        break
    if texto[:5] == 'Julia':
        continue
    arq1.write('\n{}'.format(texto))
'''
w - ESCREVE TEXTOS NO ARRQUIVO
A - REALIZA MESMAS FUNÇÕES DO W, porém ele coloca um cursor no final do texto digitado e permite continuar o texto, 
ao invés de substituir todo conteúdo do arquivo

exemplo: com open('file.txt','w'), eu executei o comando arq.write('A') e depois arq.write('B'), no arquivo aparecerá
apenas B, com a aparecerá A e B
'''