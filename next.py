import pygame
import sys

W = 800
H = 600
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
rect_pos = (W // 2, )

pygame.init()
pygame.display.set_caption('Задание на урок')
pygame.mouse.set_visible(True)
screen = pygame.display.set_mode((W, H))
screen.fill(BLUE)

pygame.draw.rect(screen, RED, (20, 20, ))



run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                run = False