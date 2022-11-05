# pus' smile
import pygame
from pygame.draw import circle, rect, line, arc

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (255, 255, 255), (0, 0, 400, 400))
circle(screen, (255, 255, 0), (200, 200), 100)
circle(screen, (0, 0, 0), (150, 170), 30)
circle(screen, (0, 0, 0), (250, 170), 30)
circle(screen, (255, 255, 255), (150 - 8, 170 - 8), 15)
circle(screen, (255, 255, 255), (250 - 8, 170 - 8), 15)


def elbow(elbowx, elbowy, deltax, deltay):
    line(screen, (0, 0, 0), (elbowx, elbowy), (elbowx + deltax, elbowy + deltay), 10)


elbow(100, 170, 50, -50)
elbow(300, 170, -50, -50)

rect(screen, (255, 200, 200), (130, 215, 40, 20))
rect(screen, (255, 200, 200), (230, 215, 40, 20))

arc(screen, (0,0,0), (140, 250, 100, 50), 0.7, 2.3, 10)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
