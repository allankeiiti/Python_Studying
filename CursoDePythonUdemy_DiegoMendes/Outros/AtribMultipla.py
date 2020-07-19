#Atribuição multipla
#Curso de Python

#x = 10
#y = 10

x, y = 10, 20
print('{} - {}'. format(x,y))

#operadores de atribuicao

mais = menos = vezes = dividido = 2

mais+=2

menos -= 5

vezes *= 10

dividido /= 2

print('{} {} {} {}'.format(mais, menos,vezes,dividido))

nota = 5

if nota>=7:
    situacao = 'true'
else:
    situacao = 'false'

if situacao == 'true':
    print(type(situacao))
    print('Aluno aprovado!')
elif situacao == 'false' and nota>=5:
    print('Aluno de recuperacao!')
else:
    print('Aluno reprovado!')

situacao = 'Aprovado' if nota>=7 else 'Reprovado'
print('O aluno com nota {} está {}'.format(nota, situacao))