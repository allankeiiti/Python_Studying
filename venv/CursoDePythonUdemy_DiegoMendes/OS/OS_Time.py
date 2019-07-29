import datetime as dt

hora = dt.time(10,21,30,12)
# print(hora)
#
# #print('Hora: {}\nMinuto: {}\nSegundo: {}\nMicroSegundo: {}'.format(hora.hour,hora.minute,hora.second,hora.microsecond))
#
#
# hora2 = hora.replace(14)
# print(hora2)
#
# print(hora2.isoformat())

t1 = str(dt.time(9,35,23))
t2 = str(dt.time(19,23,00))

inicio = dt.datetime.strptime(t1, '%H:%M:%S')
final = dt.datetime.strptime(t2, '%H:%M:%S')
diference = (final - inicio)
print(diference)