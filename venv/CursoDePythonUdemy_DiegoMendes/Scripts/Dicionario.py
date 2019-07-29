dic = {}
dic['a'] = 1
dic['b'] = 2
dic['c'] = 3
dic['d'] = 4
print(dic)

#Posso criar um dicionário desta forma também
dic2 = {'1': 'A', '2': 'B'}
print(dic2['1'])

dic3 = {'A': 'Linux', 'B':'Windows', 'C':'Maverick'}
submit = input('Digite:\nA:Linux\n'
               'B:Windows\n'
               'C:Maverick\n')

print(dic3[submit])

dic4 = dict(a='Linux',b='Windows',c='Maverick')
print(dic4.get('d'))