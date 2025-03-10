import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("کنترل با دکمه")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
bg_color = WHITE

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                bg_color = RED
            elif event.key == pygame.K_b:
                bg_color = BLUE

    screen.fill(bg_color)
    pygame.display.flip()

pygame.quit()