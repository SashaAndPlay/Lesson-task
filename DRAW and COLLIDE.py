import pygame
import sys

W, H = 400, 400
# цвета
BLUE = (0, 0, 250)
RED = (245, 0, 0)
YELLOW = (255, 255, 0, 180)
BG = (128, 128, 128)
collide = 1
collide2 = 1

# квадрат
rect_size = w, h = 70, 70
rect_pos = ((W - w) // 2, (H - h) // 2)
# круг
circle_radius = 35
circle_pos = (0, 0)
# Число столкновений с КРУГОМ
k = 0 
k_pos = (10, 10)

# Число столкновений с кругом
j = 0 
j_pos = (70, 10)

speed = [5, 5]

def aaa(x, y)
    if ball_rect.left < 0 or ball_rect.right > W:
        speed[0] = -x
    if ball_rect.top < 0 or ball_rect.bottom > H:
        speed[1] = -y
    return ball_rect.move(speed)

pygame.init()
pygame.display.set_caption('DRAW and COLLIDE')
pygame.mouse.set_visible(True)
screen = pygame.display.set_mode((W, H))

font = pygame.font.SysFont('Arial', 40, True, False)
# создаём поверхность размером в 2 раза больше круга и вкл. альфа-канал
surface = pygame.Surface((circle_radius * 2, circle_radius * 2), pygame.SRCALPHA)
# на созданной поверхности рисуем жёлтый круг
pygame.draw.circle(surface, YELLOW, (circle_radius, circle_radius), circle_radius)
# находим рект у поверхности
rect1 = surface.get_rect()

clock = pygame.time.Clock()
FPS = 300
speed_x, speed_y = 1, 1


ball = pygame.image.load('ball.png')
ball_rect = ball.get_rect()


while True:
    clock.tick(FPS)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit(0)
        elif e.type == pygame.MOUSEMOTION:
            # circle_pos = e.pos
            rect1.center = e.pos

    COLOR = RED if collide or collide2 else BLUE 
    screen.fill(BG)
    

    rect2 = pygame.draw.rect(screen, COLOR, (rect_pos, rect_size))
    screen.blit(ball, ball_rect)
    screen.blit(font.render(str(k), True, YELLOW), (k_pos))
    screen.blit(font.render(str(j), True, YELLOW), (j_pos))
    screen.blit(surface, rect1)

    ball_rect = aaa(speed[0], speed[1])

    if rect1.colliderect(rect2):
        collide = True
        if COLOR == BLUE:
            k += 1
    else:
        collide = False

    if ball_rect.colliderect(rect2):
        collide2 = True
        if COLOR == BLUE:
            j += 1
    else:
        collide2 = False

    pygame.display.update()
    
