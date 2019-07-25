import random
from pygame import mixer

def check_txt():
    # verificando arquivo txt que contém as palavras para o game
    txt = open('palavras.txt', 'r', encoding='utf8')
    palavras = []
    for line in txt:
        palavras.append(str(line.strip()))
    txt.close()
    return palavras[random.randint(0, len(palavras))]

def clear_terminal():
    return '\n'*1000

def play_sound():
    file = 'beep-07.mp3'
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()

def check_word_letters(palavra):
    lista_letra_correta = []
    for letra in palavra:
        if letra not in lista_letra_correta:
            lista_letra_correta.append(letra)
    return len(lista_letra_correta)

def check_current_result(palpites, palavra):
    palavra_formada = []
    for x in range(len(palavra)):
        palavra_formada.append('_')
    for x in range(len(palavra_formada)):
        for letras in palpites:
            if letras == palavra[x]:
                palavra_formada[x] = letras.upper()
    print(palavra_formada)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
