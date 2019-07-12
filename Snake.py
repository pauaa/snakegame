import pygame
from Cube import Cube


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
        self.head = Cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        if dx == 1 and dy == 0:  # right
            newTail = Cube((tail.pos[0]-1, tail.pos[1]))
        elif dx == -1 and dy == 0:  # left
            newTail = Cube((tail.pos[0]+1, tail.pos[1]))
        elif dx == 0 and dy == 1:  # down
            newTail = Cube((tail.pos[0], tail.pos[1]-1))
        elif dx == 0 and dy == -1:  # up
            newTail = Cube((tail.pos[0], tail.pos[1]+1))

        newTail.dirnx = dx
        newTail.dirny = dy
        self.body.append(newTail)

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:  # head of the snake > draw eyes
                c.draw(surface, True)
            else:
                c.draw(surface)
