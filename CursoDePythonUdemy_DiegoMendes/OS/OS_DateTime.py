import datetime
#from datetime import datetime as dt

# data = datetime.date.today()
#
# data1 = dt.today()
# data2 = dt.now()
# print(data1, data2)
#
# print(data1.year)
# print(data1.month)
# print(data1.day)

# d = data1.timetuple()
# print('Dia: {}'.format(d.tm_mday))
# print('Mês: {}'.format(d.tm_mon))
# print('Ano: {}'.format(d.tm_year))
# print('Hora: {}'.format(d.tm_hour))
# print('Minuto: {}'.format(d.tm_min))
# print('Segundo: {}'.format(d.tm_sec))

#GREGORIANO
# o = 736739
# print('o: {}'.format(o))
# print(datetime.date.fromordinal(o))


# print(datetime.date.min)
# print(datetime.date.max)
# print(datetime.date.resolution)

# d1 = datetime.date(2018,2,22)
# print(d1)
#
# d2 = d1.replace(year=2019)
# print(d2)

# TRABALHANDO COM TIMEDELTA

# print('microsegundos: {}'.format(datetime.timedelta(microseconds=1)))
# print('segundos: {}'.format(datetime.timedelta(seconds=1)))
# print('minutos: {}'.format(datetime.timedelta(minutes=1)))
# print('horas: {}'.format(datetime.timedelta(hours=1)))
# print('dias: {}'.format(datetime.timedelta(days=1)))
# print('semanas: {}'.format(datetime.timedelta(weeks=1)))

hoje = datetime.date.today()
print('Hoje: {}'.format(hoje))

um_dia = datetime.timedelta(days=1)
print(um_dia)

ontem = hoje - um_dia
print(ontem)