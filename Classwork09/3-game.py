import pygame
from pygame.draw import circle
from random import randint
pygame.init()

FPS = 1
screen = pygame.display.set_mode((1000, 700))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball():
    '''
    рисует новый шарик
    '''
    global x, y, r
    x = randint(100, 900)
    y = randint(100, 600)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


def many_balls():
    '''
    Program which draws three balls and returns theirs positions and radii as  list
    '''
    global a
    a = []
    for i in range(3):
        new_ball()
        a.append((x, y, r))


def getter():
    '''
    gets list of radii
    '''
    return a


def click():
    '''
    gives variables for getter
    '''
    return x, y, r


def distance(a1, a2):
    '''

    :param a1: coordinates of first dot
    :param a2: coordinates of second dot
    :return: distance between two dots
    '''
    x1, y1 = a1
    x2, y2 = a2
    return((x1-x2)**2+(y1-y2)**2)**0.5


pygame.display.update()
clock = pygame.time.Clock()
finished = False
s = 0


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            d = pygame.mouse.get_pos()
            b = getter()
            c = [[b[i][0], b[i][1]] for i in range(3)]
            r = [b[i][2] for i in range(3)]
            for i in range(3):
                if distance(d, c[i]) <= r[i]:
                    s += 1
    many_balls()
    pygame.display.update()
    screen.fill(BLACK)
print(s)
pygame.quit()
