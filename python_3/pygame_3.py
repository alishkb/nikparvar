import pygame

class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.x_dir = 'add'
        self.y_dir = 'add'

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self, dx, dy):
        if self.x + dx <= 790 and self.x_dir == 'add':
            self.x += dx
        elif self.x - dx >= 0:
            self.x -= dx
            self.x_dir = None
        else:
            self.x_dir = 'add'

        if self.y + dy <= 790 and self.y_dir == 'add':
            self.y += dy
        elif self.y - dy >= 0:
            self.y -= dy
            self.y_dir = None
        else:
            self.y_dir = 'add'


        self.y = self.y + dy if self.y + dy <= 590 else self.y - dy

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("توپ متحرک")

ball = Ball(100, 100, 20, (0, 0, 255))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball.move(2, 2)

    screen.fill((255, 255, 255))
    ball.draw(screen)
    pygame.display.flip()

pygame.quit()