# -*- coding: utf-8 -*-

# Jogo da Froca
# Programação Orientada a Objetos
from string import ascii_lowercase
from os import system
from DataScienceAcademy_Scripts.Cap5 import CRUD_SQLite as crud
from DataScienceAcademy_Scripts.Cap5.start import check_txt, play_sound, bcolors, \
    check_word_letters, check_current_result

# Board (tabuleiro)
board = ['''
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
 O   |      TRY AGAIN
/|\  |
/ \  |
     |
=========''']

class boneco:
    def __init__(self, palavra = crud.random_word(), erros = 0, acertos = 0):
        self.palavra = palavra
        self.erros = erros
        self.acertos = acertos
        self.alvo_acertos = check_word_letters(self.palavra)
        self.lista_acertos = []

    def guess(self, letra):
        self.letra = letra
        if letra in self.palavra:
            self.lista_acertos.append(letra)
            print(bcolors.OKGREEN + '{} pertence à palavra escondida!'.format(letra) + bcolors.ENDC)
            self.acertos += 1
            if self.acertos == self.alvo_acertos:
                self.boneco_vitoria(board, self.erros)
                self.x = 0
        else:
            print(bcolors.FAIL + '{} não pertence à palavra escondida!'.format(letra) + bcolors.ENDC)
            self.erros += 1
            if self.erros >= 6:
                self.boneco_derrota(board)
                self.x = 0

    def boneco_derrota(self, board):
        print(bcolors.FAIL + 'Você perdeu!' + bcolors.ENDC)
        print(bcolors.FAIL + '' + board[-1] + ''  + bcolors.ENDC)
        print(bcolors.FAIL + 'Palavra sorteada: {}'.format(self.palavra) + bcolors.ENDC)

    def boneco_vitoria(self, board, erros):
        print(bcolors.OKGREEN + 'Você venceu!' + bcolors.ENDC)
        print(bcolors.OKGREEN + '' + board[erros] + '' + bcolors.ENDC)
        print(bcolors.OKGREEN + 'Palavra sorteada: {}'.format(self.palavra) + bcolors.ENDC)

    def status_boneco(self):
        print(board[self.erros])
        check_current_result(self.lista_acertos, self.palavra)


    def main(self):
        letras = []
        palpites = []
        for letra in ascii_lowercase:
            letras.append(letra)
        self.x = 1
        while self.x == 1:
            play_sound()
            self.status_boneco()
            print('Palpites: {}'.format(palpites).upper())
            letra = input('Digite APENAS uma Letra: ').lower()
            if len(letra) == 1:
                if letra in letras:
                    if letra not in palpites:
                        palpites.append(letra)
                        self.guess(letra)
                    else:
                        print(bcolors.WARNING + 'A letra {} já foi utilizada. Digite outra.'.format(letra) + bcolors.ENDC)
            else:
                print('Digite uma letra apenas.')

print ('JOGO DA FORCA')
system('pause')
boneco1 = boneco()
boneco1.main()