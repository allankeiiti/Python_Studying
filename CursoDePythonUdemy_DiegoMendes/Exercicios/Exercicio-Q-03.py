'''
Exercícios de fixação - OS e DateTime
Curso de Python

Diego M. Rodrigues

Exercício 3
---
Exiba a hora 09h30m25s na tela. Adicione 35 minutos
nessa hora e exiba novamente, agora no formato ISO-8601.
Altere a hora para 15 e mostre na tela, no seguinte
formato: HH#MM#SS.
'''

import datetime

hora = datetime.time(9, 30, 25)
print(hora)

minutosTotais = hora.hour * 60 + hora.minute

minutosTotais += 35 # Somando 35 minutos na hora

novaHora = minutosTotais // 60
novosMinutos = minutosTotais % 60
novosSegundos = hora.second

hora2 = datetime.time(novaHora, novosMinutos, novosSegundos)
print(hora2)

hora3 = hora2.replace(15)
print(hora3.strftime('%H:%M:%S'))