from tkinter import *
import random
import time

level = int(input('Qual nível de dificuldade deseja jogarw 1/2/3/4/5\n'))
while level not in [1, 2, 3, 4, 5]:
    level = int(input('Qual nível de dificuldade deseja jogarw 1/2/3/4/5\n'))

# Declarando o tamanho da barra de acordo com o nível
# de dificuldade
length = 500/level

# Criando uma GUI com TKinter
tela = Tk()
tela.title("Pong Game")
tela.resizable(False, False)
tela.wm_attributes("-topmost", -1)

canvas = Canvas(tela, width = 800, height = 600, bd = 0,
                highlightthickness = 0)
canvas.pack()

tela.update()

# Variável de pontuação e derrota
count = 0
lost = False

class Bola:
    def __init__(self, canvas, Barra, color):
        self.canvas = canvas
        self.Barra = Barra
        # Criando o shape e cor da Bola
        self.id = canvas.create_oval(0, 0, 15, 15, fill = color)
        self.canvas.move(self.id, 245, 200)

        # Ponto de início da Bola
        starts_x = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts_x)

        self.x = starts_x[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.y = 3

        if pos[3] >= self.canvas_height:
            self.y = -3

        if pos[0] <= 0:
            self.x = 3

        if pos[2] >= self.canvas_width:
            self.x = -3

        self.Barra_pos = self.canvas.coords(self.Barra.id)

        if pos[2] >= self.Barra_pos[0] and pos[0] <= self.Barra_pos[2]:
            if pos[3] >= self.Barra_pos[1] and pos[3] <= self.Barra_pos[3]:
                self.y = -3
                global count
                count += 1

                # Chamando À função Score
                score()

        if pos[3] <= self.canvas_height:
            self.canvas.after(10, self.draw)
        else:
            game_over()
            global lost
            lost = True

class Barra:
    def __init__(self, canvas, color):
        self.canvas = canvas
        # Criando o shape e cor da barra do jogador
        self.id = canvas.create_rectangle(0, 0, length, 10, fill = color)
        self.canvas.move(self.id, 200, 400)
        # Posição X da barra
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        # -- CONTROLS --
        # Adicioando reação do retangulo se apertar "left"
        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        # Adicioando reação do retangulo se apertar "right"
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        self.pos = self.canvas.coords(self.id)

        if self.pos[0] <= 0:
            self.x = 0

        if self.pos[2] >= self.canvas_width:
            self.x = 0

        global lost

        if lost == False:
            self.canvas.after(10, self.draw)

    # Função de mover para esquerda
    def move_left(self, event):
        if self.pos[0] >= 0:
            # Velocidade de andar à esquerda da barra
            self.x = -3

    # Função de mover para direita
    def move_right(self, event):
        if self.pos[2] <= self.canvas_width:
            self.x = 3

# Função de iniciar o jogo
def start_game(event):
    global lost, count
    lost = False
    count = 0

    score()

    canvas.itemconfig(game, text = " ")

    time.sleep(1)
    Barra.draw()
    Bola.draw()

# Função de pontuação
def score():
    canvas.itemconfig(score_now, text = "Pontos: " + str(count))

# Função de Game_Over, que será chamada pela classe Bola
def game_over():
    canvas.itemconfig(game, text = "Game Over!")

# Instâncias dos objetos Barra e Bola
Barra = Barra(canvas, "red")
Bola = Bola(canvas, Barra, "blue")

# Variáveis que recebem os resultados das funções
score_now = canvas.create_text(430, 20, text = "Pontos: " + str(count),
                               fill = "green", font = ("Arial", 16))
game = canvas.create_text(400, 300, text = " ", fill = "red",
                          font = ("Arial", 40))
canvas.bind_all("<Button-1>", start_game)

# Executa a tela TKinter e o jogo
tela.mainloop()