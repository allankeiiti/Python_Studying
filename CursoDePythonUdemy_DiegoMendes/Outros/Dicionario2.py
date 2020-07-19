d1 = dict(python='linguagem de alto nível',
          c='linguagem de baixo nivel',
          sql='linguagem para DB',
          java='linguagem chata')
d2 = d1
d3 = {'A':'Zero','B':'X','C':'AXL'}
print(d2)
print(d1)

#utilizando este método é mais seguro, pois apenas instanciar um dicionário e tentar imprimir ocorrerá erro

print(d2.get('c'))
print(d2.get('a')) #'a' não existe no d2.

#print(d3['X']) #Viu como ocorre um erro??

d3 = dict(python='linguagem de alto nível',
          c='linguagem de baixo nivel',
          sql='linguagem para DB',
          java='linguagem chata')

d4 = d3.copy()
print(d3)
print(d4)

del(d3['c'])
d3['d'] = 'Java'
print(d3)
print(d4)
