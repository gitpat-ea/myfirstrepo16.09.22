import math
from random import choice, randint

import pygame
from pygame.draw import circle, rect, arc, line

FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 900
HEIGHT = 700
ball = 0
face = 1
projectiles = [ball, face]


class Gravity:
    '''
    don't need:)
    '''
    def __init__(self, fall_axeleration):
        self.fall_axeleration = fall_axeleration

    def returner(self):
        return self.fall_axeleration


g = Gravity(1)


def distance(a1, a2):
    """
    :param a1: coordinates of first dot
    :param a2: coordinates of second dot
    :return: distance between two dots
    """
    x1, y1 = a1
    x2, y2 = a2
    return((x1-x2)**2+(y1-y2)**2)**0.5


class Counter:
    '''
    counts number of hits of projectiles into targets
    '''
    def __init__(self):
        self.__count = 0

    def penetration(self, ball, obj):
        if ball.hittest(obj):
            self.__count += 1

    def getter(self):
        print("Che, interesno, skol'ko ballov???", "Malo, loh", sep='\n')
        return self.__count


class Ball:
    def __init__(self, screen: pygame.Surface, x=20, y=450, gravity=-1):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.gravity = gravity
        self.color = choice(GAME_COLORS)
        self.live = 60

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME

        if self.x >= 800 - self.r:
            self.vx = -0.8*self.vx
            self.x = 800 - self.r
        if self.x <= self.r:
            self.vx = -0.8*self.vx
            self.x = self.r
        if self.y >= 600 - self.r:
            self.vy = -0.8*self.vy
            self.y = 600 - self.r
        if self.y <= self.r:
            self.vy = -0.8 * self.vy
            self.y = self.r
        self.vy += self.gravity
        self.x += self.vx
        self.y -= self.vy
        if self.y > 600 - self.r and abs(self.vy) <= 1:
            self.gravity = 0
            self.vy = 0
            self.y = 600 - self.r
        if self.y >= 600 - self.r:
            self.vx = self.vx*0.8
        if abs(self.vy) < 1:
            self.live -= 1

    def draw(self):
        '''

        :return: draws a ball
        '''
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def ball_killer(self):
        '''
        sets ball's hp at -1, so it wouldn't appear further
        '''
        self.live = -1

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if distance((self.x, self.y), (obj.x, obj.y)) <= self.r + obj.r:
            return True
        else:
        # FIXME
            return False


class Face(Ball):
    '''
    same as ball, but cutter
    '''
    def draw(self):
        self.r = 50
        circle(screen, (255, 255, 0), (self.x, self.y), self.r)
        circle(screen, (0, 0, 0), (self.x - 0.5 * self.r, self.y - 0.3 * self.r), 0.3 * self.r)
        circle(screen, (0, 0, 0), (self.x + 0.5 * self.r, self.y - 0.3 * self.r), 0.3 * self.r)
        circle(screen, (255, 255, 255), (self.x - 0.58 * self.r, self.y - 0.38 * self.r), 0.15 * self.r)
        circle(screen, (255, 255, 255), (self.x + 0.42 * self.r, self.y - 0.38 * self.r), 0.15 * self.r)

        def elbow(elbowx, elbowy, deltax, deltay):
            line(screen, (0, 0, 0), (elbowx, elbowy), (elbowx + deltax, elbowy + deltay), 3)

        elbow(self.x - self.r, self.y - 0.3 * self.r, 0.5 * self.r, -0.5 * self.r)
        elbow(self.x + self.r, self.y - 0.3 * self.r, -0.5 * self.r, -0.5 * self.r)

        rect(screen, (255, 200, 200), (self.x - 0.7 * self.r, self.y + 0.15 * self.r, 0.4 * self.r, 0.2 * self.r))
        rect(screen, (255, 200, 200), (self.x + 0.3 * self.r, self.y + 0.15 * self.r, 0.4 * self.r, 0.2 * self.r))

        arc(screen, (0, 0, 0), (self.x - 0.6 * self.r, self.y + 0.5 * self.r, self.r, 0.5 * self.r), 0.7, 2.3, 1)


class Gun:
    '''
    gun which can shoot projectiles and move
    '''
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.bullet_type = ball
        self.y = 450

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global projectile, bullet
        if self.bullet_type == ball:
            bullet += 1
            new_ball = Ball(self.screen, y=self.y)
            new_ball.r += 5
            self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
            new_ball.vx = self.f2_power * math.cos(self.an)
            new_ball.vy = - self.f2_power * math.sin(self.an)
            projectile.append(new_ball)
            self.f2_on = 0
            self.f2_power = 10
        elif self.bullet_type == face:
            bullet += 1
            new_ball = Face(self.screen, y=self.y)
            new_ball.r += 5
            self.an = math.atan2((event.pos[1] - new_ball.y), (event.pos[0] - new_ball.x))
            new_ball.vx = self.f2_power * math.cos(self.an)
            new_ball.vy = - self.f2_power * math.sin(self.an)
            projectile.append(new_ball)
            self.f2_on = 0
            self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if event.pos[0]-20 != 0:
                self.an = math.atan((event.pos[1] - self.y) / (event.pos[0] - 20))
            else:
                self.an = 0
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        '''
        draws a gun
        '''
        if self.f2_on:
            pygame.draw.line(screen, YELLOW, (20, self.y), (20+1*(self.f2_power+20)*math.cos(self.an), self.y+1*(self.f2_power+20)*math.sin(self.an)), 10)
        else:
            pygame.draw.line(screen, GREY, (20, self.y), (20+30*math.cos(self.an), self.y+30*math.sin(self.an)), 10)
        # FIXIT don't know how to do it

    def gunmovement(self):
        '''
        moves a gun if you push w or s keys
        :return:
        '''
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if self.y >= 100:
                self.y -= 3
        elif keys[pygame.K_s]:
            if self.y <= 500:
                self.y += 3

    def bullet_changer(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            self.bullet_type = projectiles[0]
        elif keys[pygame.K_2]:
            self.bullet_type = projectiles[1]

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self):
        self.screen = screen
        self.points = 0
        self.live = 1
        # FIXME: don't work!!! How to call this functions when object is created?
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = randint(600, 780)
        y = self.y = randint(50, 550)
        r = self.r = randint(20, 50)
        self.vy = randint(-20, 20)
        color = self.color = RED

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def move(self):
        '''
        moves a target, but only horizontally
        '''
        if self.y >= 500 - self.r:
            self.vy = -self.vy
            self.y = 500 - self.r
        if self.y <= self.r:
            self.vy = -self.vy
            self.y = self.r
        self.y -= self.vy

    def draw(self):
        '''
        draws a target
        '''
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)
        pygame.draw.circle(self.screen, BLACK, (self.x, self.y), self.r+2, 2)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
projectile = []

clock = pygame.time.Clock()
gun = Gun(screen)
target1 = Target()
target2 = Target()
Targets = [target1, target2]
counter = Counter()
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    gun.gunmovement()
    gun.bullet_changer()
    for target in Targets:
        target.draw()
    for b in projectile:
        if b.live > 0:
            b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in projectile:
        if b.live > 0:
            b.move()
            for target in Targets:
                if b.hittest(target):
                    counter.penetration(b, target)
                    target.hit()
                    target.new_target()
                    b.ball_killer()
    for target in Targets:
        target.move()
    gun.power_up()

pygame.quit()

print(counter.getter())
# А ещё ожидание на использование Мега снаряда
# Можно добавить выведение счета и типа снаряда на экран
