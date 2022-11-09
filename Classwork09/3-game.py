import pygame
from pygame.draw import circle, rect, line, arc
from random import randint
pygame.init()

FPS = 30
screen = pygame.display.set_mode((1000, 700))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball(x, y, r, color):
    '''
    рисует новый шарик
    '''

    circle(screen, color, (x, y), r)


def many_balls():
    '''
    Program which draws three balls and returns theirs positions and radii as  list
    '''
    a = []
    for i in range(3):
        new_ball(x, y, r)
        a.append((x, y, r))

def face(x, y, r):
    '''

    :param x: x position of center of the face
    :param y: y position of center of the face
    :param r: radius of the face
    :return: function draws face of the given radius in the given dot of the screen
    '''
    circle(screen, (255, 255, 0), (x, y), r)
    circle(screen, (0, 0, 0), (x-0.5*r, y-0.3*r), 0.3*r)
    circle(screen, (0, 0, 0), (x+0.5*r, y-0.3*r), 0.3*r)
    circle(screen, (255, 255, 255), (x-0.58*r, y - 0.38*r), 0.15*r)
    circle(screen, (255, 255, 255), (x + 0.42*r, y - 0.38*r), 0.15*r)

    def elbow(elbowx, elbowy, deltax, deltay):
        line(screen, (0, 0, 0), (elbowx, elbowy), (elbowx + deltax, elbowy + deltay), 10)

    elbow(x-r, y-0.3*r, 0.5*r, -0.5*r)
    elbow(x+r, y-0.3*r, -0.5*r, -0.5*r)

    rect(screen, (255, 200, 200), (x-0.7*r, y+0.15*r, 0.4*r,  0.2*r))
    rect(screen, (255, 200, 200), (x+0.3*r, y+0.15*r, 0.4*r, 0.2*r))

    arc(screen, (0, 0, 0), (x-0.6*r, y+0.5*r, r, 0.5*r), 0.7, 2.3, 10)


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

n = 10
first_pos_circle = []
for i in range(n):
    first_pos_circle.append([randint(100, 900), randint(100, 600)])

radii = []
for i in range(n):
    radii.append(randint(100, 100))

velocities = []
for i in range(n):
    velocities.append([randint(-20, 20), randint(-20, 20)])

speed_face = [-30, 30]

face_pos = [500, 350]

face_radius = [100]

colors = []
for i in range(n):
    colors.append(randint(0, 5))

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            d = pygame.mouse.get_pos()
            for i in range(n):
                if distance(d, first_pos_circle[i]) <= radii[i]:
                    s += 1
            if distance(d, face_pos) <= face_radius[0]:
                s += 3
    for i in range(n):
        for j in range(2):
            first_pos_circle[i][j] += velocities[i][j]
    for i in range(n):
        if first_pos_circle[i][0] >= 1000 - radii[i] or first_pos_circle[i][0] <= radii[i]:
            velocities[i][0] = -velocities[i][0]
    for i in range(n):
        if first_pos_circle[i][1] >= 700 - radii[i] or first_pos_circle[i][1] <= radii[i]:
            velocities[i][1] = -velocities[i][1]
    for i in range(n):
        new_ball(first_pos_circle[i][0], first_pos_circle[i][1], radii[i], COLORS[colors[i]])
    face_pos[0] += speed_face[0]
    face_pos[1] += speed_face[1]
    if face_pos[0] >= 1000 - face_radius[0] or face_pos[0] <= face_radius[0]:
        speed_face[0] = -speed_face[0]
    if face_pos[1] >= 700 - face_radius[0] or face_pos[1] <= face_radius[0]:
        speed_face[1] = -speed_face[1]
    face(face_pos[0], face_pos[1], face_radius[0])
    pygame.display.update()
    screen.fill(BLACK)

print(s)
pygame.quit()
