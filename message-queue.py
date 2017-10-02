import pygame
from pygame.locals import *
from sys import exit

backgroundImageFileName = 'background-02.png'
SCREENSIZE = (640, 480)
message = '    This is a demonstration of the scrolly message script.'

pygame.init()
screen = pygame.display.set_mode(SCREENSIZE, 0, 32)

font = pygame.font.SysFont('arial', 80)
textSurface = font.render(message, True, (0, 0, 255), None)

x = 0
y = (SCREENSIZE[1] - textSurface.get_height()) / 2

background = pygame.image.load(backgroundImageFileName).convert()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    screen.blit(background, (0, 0))

    x -= 2
    if x < -textSurface.get_width():
        x = 0

    screen.blit(textSurface, (x, y))
    screen.blit(textSurface, (x + textSurface.get_width(), y))
    pygame.display.update()