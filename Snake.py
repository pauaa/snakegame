import pygame
from Cube import Cube


class Snake(object):
    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = Cube(pos, color)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_LEFT]:
                    if self.dirnx == 1 and self.dirny == 0:
                        continue
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.position[:]] = [
                        self.dirnx, self.dirny]

                elif keys[pygame.K_RIGHT]:
                    if self.dirnx == -1 and self.dirny == 0:
                        continue
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.position[:]] = [
                        self.dirnx, self.dirny]

                elif keys[pygame.K_UP]:
                    if self.dirnx == 0 and self.dirny == 1:
                        continue
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.position[:]] = [
                        self.dirnx, self.dirny]

                elif keys[pygame.K_DOWN]:
                    if self.dirnx == 0 and self.dirny == -1:
                        continue
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.position[:]] = [
                        self.dirnx, self.dirny]

        for i, cube in enumerate(self.body):
            position = cube.position[:]
            if position in self.turns:
                turn = self.turns[position]
                cube.move(turn[0], turn[1])
                if i == len(self.body)-1:  # last qube
                    self.turns.pop(position)
            else:  # hitting the edges of the screen, move to the opposite side of the screem
                if cube.moving_left() and cube.position[0] <= 0:
                    cube.position = (cube.rows-1, cube.position[1])
                elif cube.moving_right() and cube.position[0] >= cube.rows-1:
                    cube.position = (0, cube.position[1])
                elif cube.moving_down() and cube.position[1] >= cube.rows-1:
                    cube.position = (cube.position[0], 0)
                elif cube.moving_up() and cube.position[1] <= 0:
                    cube.position = (cube.position[0], cube.rows-1)
                else:
                    cube.move(cube.dirnx, cube.dirny)  # keep moving

    def reset(self, pos):
        self.head = Cube(pos, self.color)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        if dx == 1 and dy == 0:  # right
            newTail = Cube((tail.position[0]-1, tail.position[1]), self.color)
        elif dx == -1 and dy == 0:  # left
            newTail = Cube((tail.position[0]+1, tail.position[1]), self.color)
        elif dx == 0 and dy == 1:  # down
            newTail = Cube((tail.position[0], tail.position[1]-1), self.color)
        elif dx == 0 and dy == -1:  # up
            newTail = Cube((tail.position[0], tail.position[1]+1), self.color)

        newTail.dirnx = dx
        newTail.dirny = dy
        self.body.append(newTail)

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:  # head of the snake > draw eyes
                c.draw(surface, True)
            else:
                c.draw(surface)
