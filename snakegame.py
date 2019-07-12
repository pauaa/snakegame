import pygame
import math
import random
import tkinter as tk
from tkinter import messagebox


class Cube(object):
    rows = 20
    w = 500

    def __init__(self, start, dirnx=1, dirny=0, color=(231, 59, 43)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]
        pygame.draw.rect(surface, self.color, (i*dis+1, j*dis+1, dis-2, dis-2))

        if eyes:
            center = dis//2
            radius = 2
            circleMiddle = (i*dis+center-radius, j*dis+8)
            circleMiddle2 = (i*dis+dis-radius*3, j*dis+8)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radius)


class Snake(object):
    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = Cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        for i, cube in enumerate(self.body):
            position = cube.pos[:]
            if position in self.turns:
                turn = self.turns[position]
                cube.move(turn[0], turn[1])
                if i == len(self.body)-1:  # last qube
                    self.turns.pop(position)
            else:  # hitting the edges of the screen, move to the opposite side of the screem
                # moving left
                if cube.dirnx == -1 and cube.pos[0] <= 0:
                    cube.pos = (cube.rows-1, cube.pos[1])
                # moving right
                elif cube.dirnx == 1 and cube.pos[0] >= cube.rows-1:
                    cube.pos = (0, cube.pos[1])
                # moving down
                elif cube.dirny == 1 and cube.pos[1] >= cube.rows-1:
                    cube.pos = (cube.pos[0], 0)
                # moving up
                elif cube.dirny == -1 and cube.pos[1] <= 0:
                    cube.pos = (cube.pos[0], cube.rows-1)
                else:
                    cube.move(cube.dirnx, cube.dirny)  # keep moving

    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:  # head of the snake > draw eyes
                c.draw(surface, True)
            else:
                c.draw(surface)


def drawGrid(w, rows, surface):
    sizeBtwn = w // rows
    x = 0
    y = 0
    for l in range(rows):
        x += sizeBtwn
        y += sizeBtwn

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))


def redrawWindow(surface):
    global rows, width
    surface.fill((0, 0, 0))
    snake.draw(surface)
    drawGrid(width, rows, surface)
    pygame.display.update()


def randomSnack(rows, items):
    pass


def message_mov(subject, content):
    pass


def main():
    global width, rows, snake
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    snake = Snake((255, 0, 0), (10, 10))

    flag = True
    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        snake.move()
        redrawWindow(win)


main()
