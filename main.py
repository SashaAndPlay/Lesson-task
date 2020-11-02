import pygame

W = 800
H = 600
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
block = 0
a = "Всем привет"
b = "Задание на урок"



pygame.init()
pygame.display.set_caption('Задание на урок')
pygame.mouse.set_visible(True)
screen = pygame.display.set_mode((W, H))
screen.fill(BLUE)

red = pygame.Surface((100, 100))
red_rect = red.get_rect(center=(400, 150))

font1 = pygame.font.SysFont('Arial', 40, True, False)
font2 = pygame.font.SysFont('Arial', 25, False, False)


run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                run = False

    if block == 0:            
        screen.blit(red, red_rect)
        red.fill(RED)
        screen.blit(font1.render(a, True, RED), (300, 300))
        screen.blit(font2.render(b, True, WHITE), (320, 400))
        pygame.display.update()
