import pygame
import random
import tkinter as tk
from tkinter import messagebox
from Cube import Cube
from Snake import Snake


def drawGrid(width, rows, surface):
    sizeBtwn = width // rows
    x, y = 0, 0
    for _ in range(rows):
        x += sizeBtwn
        y += sizeBtwn

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, width))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (width, y))


def redrawWindow(surface):
    global rows, width, snake, snack
    surface.fill((0, 0, 0))
    snake.draw(surface)
    snack.draw(surface)
    drawGrid(width, rows, surface)
    pygame.display.update()


def randomSnack(rows, item):
    positions = item.body
    while True:
        # generate random position
        x = random.randrange(rows)
        y = random.randrange(rows)
        # prevent snack appearing on the snake
        if len(list(filter(lambda z: z.position == (x, y), positions))) > 0:
            continue
        else:
            break
    return (x, y)


def message_box(subject, content):
    # Message box on on top of everything else
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


def main():
    global width, rows, snake, snack
    width = Cube.width
    rows = Cube.rows
    win = pygame.display.set_mode((width, width))
    snake = Snake((255, 0, 0), (10, 10))
    snack = Cube(randomSnack(rows, snake), color=(0, 255, 0))

    clock = pygame.time.Clock()

    while True:
        pygame.time.delay(50)
        clock.tick(10)
        snake.move()
        if snake.body[0].position == snack.position:
            snake.addCube()
            snack = Cube(randomSnack(rows, snake), color=(0, 255, 0))

        for x in range(len(snake.body)):
            if snake.body[x].position in list(map(lambda z: z.position, snake.body[x+1:])):
                message_box(
                    'You Lost!', 'Score: {}. Play again!'.format(len(snake.body)))
                snake.reset((10, 10))
                break

        redrawWindow(win)


main()
