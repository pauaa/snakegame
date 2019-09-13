import pygame


class Cube(object):
    rows = 20
    width = 500

    def __init__(self, start, color, dirnx=1, dirny=0):
        self.position = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.position = (
            self.position[0] + self.dirnx, self.position[1] + self.dirny)

    def draw(self, surface, eyes=False):
        dis = self.width // self.rows
        i = self.position[0]
        j = self.position[1]
        pygame.draw.rect(surface, self.color, (i*dis+1, j*dis+1, dis-2, dis-2))

        if eyes:
            center = dis//2
            radius = 2
            circleMiddle = (i*dis+center-radius+1, j*dis+8)
            circleMiddle2 = (i*dis+dis-radius*3, j*dis+8)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radius)

    def moving_left(self):
        return self.dirnx == -1 and self.dirny == 0

    def moving_right(self):
        return self.dirnx == 1 and self.dirny == 0

    def moving_down(self):
        return self.dirny == 1 and self.dirnx == 0

    def moving_up(self):
        return self.dirny == -1 and self.dirnx == 0
