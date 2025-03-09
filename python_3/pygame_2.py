import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("مستطیل متحرک")

x = 100
y = 100
speed = 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))
    pygame.display.flip()

pygame.quit()
