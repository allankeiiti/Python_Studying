import datetime

t1 = datetime.time(8,30,10)
t2 = datetime.time(15,20,12)

print('t2({}) > t1({}): {}'.format(t2,t1,t2>t1))

#Usando uma lista para obter valores do datetime
'''
FIELDS = ['year','month','day','hour','minute','second','microsecond']

date = datetime.datetime.now()

for atributo in FIELDS:
    print('{:12} : {}'.format(atributo, getattr(date, atributo)))
'''

# t = datetime.time(1,2,3)
# print(t)
#
# d = datetime.date.today()
# print(d)
#
# dt = datetime.datetime.combine(d,t)
# print(dt)

formato = '%a %b %d %H:%M:%S %Y'

hoje = datetime.datetime.today()
print('ISO: {}'.format(hoje))

s = hoje.strftime(formato)
print(s)