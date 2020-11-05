import pygame
import sys
W, H = 400, 400
BLUE = (0, 0, 250)
RED = (245, 0, 0)
YELLOW = (255, 255, 0)
BG = (128, 128, 128)
collide = 1
k = 0 #СЧЁТЧИК

#квадрат
rect_size = w, h = 70, 70
rect_pos = ((W - w) // 2, (H - h) // 2)
#круг
circle_radius = 35
circle_pos = (0, 0)
#Число столкновений
k_size = a, b = 20, 20
k_pos = (10, 10)

pygame.init()
pygame.display.set_caption('DRAW and COLLIDE')
pygame.mouse.set_visible(True)
screen = pygame.display.set_mode((W, H))

font1 = pygame.font.SysFont('Arial', 40, True, False)
run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit(0)
        elif e.type == pygame.MOUSEMOTION:
            circle_pos = e.pos
    screen.fill(BG)
    rect1 = pygame.draw.circle(screen, YELLOW, circle_pos, circle_radius)
    rect2 = pygame.draw.rect(screen, RED if collide else BLUE, (rect_pos, rect_size))
    screen.blit (font1.render(str(k), True, YELLOW), (k_pos))
    if rect1.colliderect(rect2): #Столкновение
        k += 1
    else:
        collide = False


    pygame.display.update()
        