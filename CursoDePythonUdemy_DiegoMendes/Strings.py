'''
Strings
Curso de Python

Diego M. Rodrigues
'''

idade = '30'
peso = '55.4'
print(idade)
print(type(idade))
print(peso)
print(type(peso))

print(idade + peso)

# idade2 = int(idade)
# peso2 = float(peso)
#
# print(type(idade2))
# print(type(peso2))
#
# print(idade2 + peso2)

# texto1 = 'Curso de '
# texto2 = 'Python'
#
# nome = texto1 + texto2
# print(nome)


# nome = 'Ana'
# idade = '30'
#
# texto = 'A {} possui {} anos.'.format(nome, idade)
# print(texto)
#
# print(texto[4])
# print(texto[6])
#
# #texto[4] = 'P'
frase = 'Curso de Python'#
#print(frase[:5])

#A linha abaixo não funciona, pois String é uma lista imutável
#frase[5] = 'x'
#Para fazer a alteração então, deve ser feito os seguintes procedimentos:

fraseSplit = frase.split(' ')
print(fraseSplit)

frase2 = frase.replace('Python','SQL')
print(frase2)
frase2 = frase2.replace('S', 'X')
print(frase2)

print(chr(64))