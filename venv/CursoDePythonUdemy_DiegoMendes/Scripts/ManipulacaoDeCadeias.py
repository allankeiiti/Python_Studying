
i = int(0)

while i <= 20:
    print('A: ',i)
    i+=1

frase = '   Curso de Python da Udemy'
print(frase[3])
print(frase[9:15])
print(frase[: :3])

length = int(len(frase))
print(length)

#a linha abaixo faz a contagem que quantas vezes a letra 'o' aparece na frase
#  o 0 pede para iniciar a busca a partir da posição 0 e atribuir a contagem
#  o 5 é até onde a busca será feita
print(frase.count('o',0,5))

print(frase.find('hon'))

print('Udemy' in frase)

#print(frase.replace('Python','PHP'))
#print(frase.upper())

#print(frase.lower())
#deixa a primeira letra da frase em maiuscula
print(frase.capitalize())
#title converte tudo para Lower e coloca a primeira letra de cada palavra em maiuscula
print('TITLE: {}. '.format(frase.title()))
#a função remove os espaços nulos que estão no inicio da frase
print(frase)
print(frase.strip())
#tem lstrip e rstrip, l de left e r de right

frase2 = 'Curso de Python e Banco de Dados'
print(frase2.split())
palavras = frase2.split()
linguagem = palavras[2:len(frase2)]
print(linguagem)


frase3 = '1,2,3,4,5'
#maxsplit "faça apenas 1 divisão
print(frase3.split(',',maxsplit=1))
frase4 = '-'.join(frase2)
print(frase4)