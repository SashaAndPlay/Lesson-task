import pygame

W = 800
H = 600
BLUE = (0, 0, 255)
RED = (255, 0, 0)
a = "Всем привет"
b = "Задание на урок"

square = pygame.display.set_mode((50, 50))
square.fill(RED)

pygame.init()
pygame.display.set_caption('Задание на урок')
pygame.mouse.set_visible(True)
screen = pygame.display.set_mode((W, H), pygame.FULLSCREEN)
screen.fill(BLUE)

font1 = pygame.font.SysFont('Arial', 40, True, False)
font2 = pygame.font.SysFont('Arial', 25, True, False)
screen.blit(font1.render(a, True, BLUE), (50, 50))



text1 = pygame.Surface((W - 30, font1.get_height()))
text1_rect = text1.get_rect(center=(W // 2, H - 30))


run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                run = False

