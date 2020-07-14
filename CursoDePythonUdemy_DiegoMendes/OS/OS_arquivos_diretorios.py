import os

print(os.getcwd())

listaPython = os.listdir('/Users/Allan')

for item in listaPython:
    print(item)

listaArquivos = os.listdir('.')
print(listaArquivos)

#a pasta abaixo cria um novo diretorio
#os.mkdir('TESTE')

#Remove arquivos, para remover dir, rmdir
#os.remove('')
#os.rmdir('TESTE')

#Renomeia arquivos ('Nome antigo','Nome novo')
#os.rename('TESTE','Pasta')

# with os.scandir('.') as items:
#     for entrada in items:
#         if not entrada.name.startswith('.') and entrada.is_file():
#             print(entrada.name)

#print(os.stat('Pasta'))

os.truncate('arquivo.txt',10)
#
# cpu = os.cpu_count()
# print(cpu)