#import emoji
#import random
#import playsound
#from math import floor, cos, tan, sin, radians

'''
Ex:1
Crie um script que leia um num real e mostre na tela sua parte inteira. 5.165 -> 5

num = float(input('Digite um número real: '))
print('Número real: {}.\nNúmero Inteiro: {:.0f}.'.format(num, num))


Ex:2
Leia um ângulo do usuário final, depois exiba na tela o seno, cosseno e a tangente

ang = float(input('Digite um ângulo, o script será gerado o seno, cosseno e a tangente do mesmo: '))
angR = radians(ang)
print(emoji.emojize('Ângulo: {:.2f}.\nSen: {:.2f}.\nCos: {:.2f}.\nTan:{:.2f}.\n :thumbs_up:'.format(ang, sin(angR), cos(angR), tan(angR))))

Ex:3
Um professor quer sortear um dos seus 3 alunos para apagar o quadro. Leia o nome desses 3 alunos
e depois exiba na tela o escolhido. Módulo: Random

nomes = []
for i in range(3):
    aluno = input('Digite um número para o Aluno {} : '.format(i+1))
    nomes.insert(i,aluno)

for i in range(3):
    print('Nomes:{}.'.format(nomes[i]))

print('Aluno sorteado: {:=^10}.'.format(random.choice(nomes)))

Ex:4
Faça um script que abra e execute um arquivo Mp3 Módulo: pygame
'''

import pygame
pygame.init()
pygame.mixer.music.load('mvc.mp3')
pygame.mixer.music.play()
pygame.event.wait()


# Este eu não fiz por conta do python 3.7 não funcionar o pygame.mixer.music