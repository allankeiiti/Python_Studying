frase = "Curso de Python"

for c in frase[2:]:
    print(c)

for c in frase[::2]:
    print(c)

#idx = 0
#while idx < len(frase):
#    print('Índice {}.\nCaractere {}.'.format(idx, frase[idx]))
#    idx+=1

idx = 0
for idx, c in enumerate(frase):
    print('Índice {}.\nCaractere {}.'.format(idx, frase[idx]))