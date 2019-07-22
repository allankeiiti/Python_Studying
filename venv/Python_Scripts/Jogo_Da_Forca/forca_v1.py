# -*- coding: utf-8 -*-

# Jogo da Froca
# Programação Orientada a Objetos
import random
import ascii_lowercase

# Board (tabuleiro)
board = ['''
>>>>>>>>>>Hangman<<<<<<<<<<
+---+
|   |
    |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
|   |
    |
    |
=========''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

class boneco:
    def __init__(self, palavra):
        self.palavra = palavra

    def guess(selfself, letra):
        self.letra = letra
'''       
    def boneco_derrota(self):
    
    def boneco_vitoria(self):
        
    def esconde_palavra(self):
        
    def print_status_jogo(self):
'''

def check_txt():
    # verificando arquivo txt
    txt = open('palavras.txt', 'r', encoding='utf8')
    palavras = []
    for line in txt:
        palavras.append(str(line.strip()))
    txt.close()
    return palavras[random.randint(0, len(palavras))]

def main():
    palavra = check_txt()
    letras = []
    palpites = []
    for letra in ascii_lowercase:
        letras.append(letra)

    letra = input('Digite uma Letra: ').lower()
    if letra not in letras:
        if letra not in palpites:
            palpites.append(letra)
        else:
            print('A letra {} já foi utilizada. Digite outra.')
    else:
        print('Digite uma letra apenas.')

    