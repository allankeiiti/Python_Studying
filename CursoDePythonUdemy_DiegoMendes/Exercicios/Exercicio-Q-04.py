'''
Exercícios de fixação - OS e DateTime
Curso de Python

Diego M. Rodrigues

Exercício 4
---
Mostre a data e hora atuais.
Exiba o dia e o minuto atual.
Crie uma nova data que seja 1,8 dias a mais que a atual.
Exiba essa nova data na tela e a diferença entre ela e a data atual.
'''

import datetime

hoje = datetime.datetime.now()
print('Data atual: {}'.format(hoje))
print('Dia: {}'.format(hoje.day))
print('Minutos: {}'.format(hoje.minute))

intervalo = datetime.timedelta(days=1.8)
data2 = hoje + intervalo
print('Nova data: {}'.format(data2))

diferenca = data2 - hoje
print('Diferença: {}'.format(diferenca))