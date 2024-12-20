import turtle
import time
import sys
from collections import deque  # Para criar filas otimizadas

# Configuração da tela principal
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("MazeWalk_AI com BFS")
wn.setup(1200, 600)

# Classe para criar labirinto
class Maze(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)

# Classe para o quadrado final do labirinto
class Black(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)

# Classe para o ponto inicial
class Yellow(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)

# Classe para o marcador do caminho solucionado
class Brown(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("brown")
        self.penup()
        self.speed(0)

# Labirinto
grid = [
    "++++++++++++++++++++++++++",
    "+               +        +",
    "+  ++++++++++  +++++++++++",
    "+s          +        ++  +",
    "+  +++++++  +++  ++++++++ ",
    "+  +     +  +        +  + ",
    "+  +  +  +  +  +  ++++   +",
    "+  +  +  +  +  +  +       ",
    "+  +  ++++  +  +++++++++  ",
    "+  +     +  +          +  ",
    "+  ++++  +  +++++++ ++++++",
    "+     +  +     +          ",
    "++++++++++++++e+++++++++++",
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
                walls.append((screen_x, screen_y))

            if character == " " or character == "e":  # Caminho ou saída
                path.append((screen_x, screen_y))

            if character == "e":  # Marca a posição de saída
                black.goto(screen_x, screen_y)
                end_x, end_y = screen_x, screen_y
                black.stamp()

            if character == "s":  # Marca a posição de início
                start_x, start_y = screen_x, screen_y
                yellow.goto(screen_x, screen_y)

# Algoritmo de busca em largura (BFS)
def search(x, y):
    frontier.append((x, y))  # Adiciona o ponto inicial à fronteira
    solution[(x, y)] = (x, y)  # Marca a célula inicial na solução

    while frontier:  # Continua enquanto houver células na fronteira
        time.sleep(0.05)  # Controla o tempo de execução
        x, y = frontier.popleft()  # Remove a célula da fronteira

        # Verifica os vizinhos da célula atual e adiciona à fronteira
        for dx, dy in [(-24, 0), (24, 0), (0, -24), (0, 24)]:
            neighbor = (x + dx, y + dy)
            if neighbor in path and neighbor not in visited:
                solution[neighbor] = (x, y)
                frontier.append(neighbor)
                visited.add(neighbor)

        black.goto(x, y)  # Marca a célula atual
        black.stamp()

# Traça a rota de volta para o início
def backRoute(x, y):
    brown.goto(x, y)
    brown.stamp()
    while (x, y) != (start_x, start_y):
        x, y = solution[(x, y)]
        brown.goto(x, y)
        brown.stamp()

# Instancia os objetos
maze = Maze()
black = Black()
brown = Brown()
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
