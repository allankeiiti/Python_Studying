'''
Exercícios de fixação - OS e DateTime
Curso de Python

Diego M. Rodrigues
'''
import os
'''
Exercício 1
---
Exiba na tela o diretório de execução do seu script.
Depois altere o diretório de trabalho do script para outro, como C:\, C:\Windows,
ou qualquer outro diretório de sua escolha, então exiba todos os arquivos
e subdiretórios desse novo local.

dir = os.getcwd()
print('Exibindo o diretorio de execução do script: {}'.format(dir))
dir = os.listdir('D:')
count = 0
for item in dir:
    print('{}: {}'.format(count, item))
    count+=1

Exercício 2
---
Faça um script que crie um novo diretório com o nome NOVO,
depois exiba todos os arquivos e subdiretórios do local
de execução do script.
Altere o nome desse novo diretório para BACKUP, depois
exiba novamente exiba todos os arquivos e subdiretórios
do local de execução do script.
Remova o diretório BACKUP.
'''
#os.mkdir('pastaX')
#print(os.listdir('pastaY'))
#os.rename('PastaY','BACKUP')
#os.remove('BACKUP\jabiraca')
#os.rmdir('BACKUP')

'''
Exercício 3
---
Exiba a hora 09h30m25s na tela. Adicione 35 minutos
nessa hora e exiba novamente, agora no formato ISO-8601.
Altere a hora para 15 e mostre na tela, no seguinte
formato: HH#MM#SS.
'''

# import datetime
# dt = datetime.time(9,30,25)
# print(dt)
#
# minTotais = dt.hour * 60 + dt.minute
# # Seria então 9 * 60 = 540 + 30 minutos
# print(minTotais)
# minTotais += 35
# horasTotais = minTotais // 60
# minutosTotais = minTotais % 60
# segundosTotais = dt.second
#
# dt2 = datetime.time(horasTotais,minutosTotais,segundosTotais)
# print('DT2: {}'.format(dt2))
#
# #Alterando a hora pra 15 e colocando no formato
# formato = 'DT3: %H:%M:%S'
# dt3 = dt.replace(15).strftime(formato)
# print(dt3)
# '''
# Exercício 4
# ---
# Mostre a data e hora atuais.
# Exiba o dia e o minuto atual.
# Crie uma nova data que seja 1,8 dias a mais que a atual.
# Exiba essa nova data na tela e a diferença entre ela e a data atual.
# '''
# data = datetime.datetime.now()
# print('Data e Hora Atual: {}'.format(data))
# print('Dia e Minuto Atual: {}, {}'.format(data.day,data.minute))



'''
Exercício 5
---
Crie uma hora usando a função time() e um dia usando a date().
Combine as duas informações para gerar uma informação de data
e hora, exibindo na tela.
'''
import datetime

