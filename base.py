import turtle
import time
import sys
import random
from collections import deque  # Para criar filas otimizadas

# Configuração da tela principal
wn = turtle.Screen()
wn.bgcolor("DarkBlue")
wn.title("MazeWalk_AI com BFS")
wn.setup(1300, 700)

# Classe para criar labirinto
class Maze(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("DarkGreen")
        self.penup()
        self.speed(0)

# Classe para o quadrado final do labirinto
class Black(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("DarkOrange")
        self.penup()
        self.speed(0)

    def stamp(self):
        self.goto(self.xcor(), self.ycor() - 24 / 2)
        self.write("🦀", align="center", font=("Arial", int(24 / 1.5), "normal"))


# Classe para o ponto inicial
class Yellow(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)

# Classe para o marcador do caminho solucionado
class White(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("White")
        self.penup()
        self.speed(0)

# Labirinto
grid = [
    "+++++++++++++++++++++++++++++++++++++++++++++++++++",
    "s               +                +                +",
    "+  ++++++++++  +++++++++++++  +++++++  ++++++++++++",
    "+           +                 +               ++  +",
    "+  +++++++  +++++++++++++  +++++++++++++++++++++  +",
    "+  +     +  +           +  +                 +++  +",
    "+  +  +  +  +  +  ++++  +  +  +++++++++++++  +++  +",
    "+  +  +  +  +  +  +        +  +  +        +       +",
    "+  +  ++++  +  ++++++++++  +  +  ++++  +  +  ++   +",
    "+  +     +  +          +   +           +  +  ++  ++",
    "+ ++  +  + ++++++++ +++++++++++  ++++++++++  +++  +",
    "+  +  +                    +     +     +  +  +++  +",
    "+  +  ++++  +++++++++++++  +  ++++  +  +     ++   +",
    "+  +  +     +     +     +     +     +     +  ++  ++",
    "+  +  +  +++++++  ++++  +  +  +  ++++++++++  ++  ++",
    "+                       +     +              ++  ++",
    "+ ++++++             +  +  +  +  +++        +++  ++",
    "+ ++++++ ++++++ +++ +++++    ++ ++   ++++++++++  ++",
    "+ +    +    +++ +     +++++++++ ++  +++++++    + ++",
    "+ ++++ ++++ +++ + + + +++    ++    ++    ++ ++ + ++",
    "+ ++++    +     + + + +++ ++ ++++++++ ++ ++ ++   ++",
    "+      ++ +++++           ++          ++    +++++++",
    "+++++++++++++++++++e+++++++++++++++++++++++++++++++",
]


# Função para configurar o labirinto
def setup_maze(grid):
    global start_x, start_y, end_x, end_y  # Variáveis para início e fim do labirinto
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            character = grid[y][x]
            screen_x = -588 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "+":  # Se o caractere é "+", desenha uma parede
                maze.goto(screen_x, screen_y)
                maze.stamp()
                maze.shapesize(24/20)
                walls.append((screen_x, screen_y))

            if character == " " or character == "e":  # Caminho ou saída
                path.append((screen_x, screen_y))

            if character == "e":  # Marca a posição de saída
                white.goto(screen_x, screen_y)
                white.shapesize(24/20)
                end_x, end_y = screen_x, screen_y
                white.stamp()

            if character == "s":  # Marca a posição de início
                start_x, start_y = screen_x, screen_y
                yellow.goto(screen_x, screen_y)
                yellow.shapesize(24/20)

# Algoritmo de busca em largura (BFS)
def search(x, y):
    frontier.append((x, y))  # Adiciona o ponto inicial à fronteira
    solution[(x, y)] = (x, y)  # Marca a célula inicial na solução

    while frontier:  # Continua enquanto houver células na fronteira
        time.sleep(0.01)  # Controla o tempo de execução
        x, y = frontier.pop()  # Remove a célula da fronteira

        #Verifica se encontrou a saída
        if (x,y)==(end_x, end_y):
            print("saída encontrada.")
            return

        # Marca a célula atual como visitada
        visited.add((x, y))  

        # Cria uma lista de vizinhos e embaralha para escolha aleatória
        neighbors = [
            (x - 24, y),
            (x + 24, y),
            (x, y - 24),
            (x, y + 24)
        ]
        random.shuffle(neighbors)  # Embaralha os vizinhos

        # Percorre os vizinhos da célula atual
        for neighbor in neighbors:
            if neighbor in path and neighbor not in visited and neighbor not in frontier:
                solution[neighbor] = (x, y)  # Registra o caminho
                frontier.append(neighbor)  # Adiciona o vizinho na fronteira

        black.goto(x, y)  # Marca a célula atual
        black.stamp()

# Traça a rota de volta para o início
def backRoute(x, y):
    white.goto(x, y)
    white.stamp()
    while (x, y) != (start_x, start_y):
        x, y = solution[(x, y)]
        white.goto(x, y)
        white.stamp()

# Instancia os objetos
maze = Maze()
black = Black()
white = White()
yellow = Yellow()

# Inicializa as listas e estruturas de controle
walls = []
path = []
visited = set()
frontier = deque()
solution = {}

# Execução principal
setup_maze(grid)  # Configura o labirinto
search(start_x, start_y)  # Realiza a busca
backRoute(end_x, end_y)  # Traça o caminho de volta
wn.exitonclick()  # Fecha o programa ao clicar na janela
