import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Smart Bot')

BLACK = (0, 0, 0)
GREEN = (10, 255, 10)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)


class Robot:
    def __init__(self, x, y):
        self.x = x

        self.y = y
        self.color = GREEN
        self.x_speed = 1
        self.x_s = 0.1

    def update(self, random=False):
        if random:
            self.x -= .1

        if self.x + self.x_speed > 0 and self.x + self.x_speed < 750:
            self.x += self.x_speed

    def zandi(self, direction, is_pressed):
        if direction == 'left':
            self.x_speed = -self.x_s if is_pressed else 0

        elif direction == 'right':
            self.x_speed = self.x_s if is_pressed else 0

    def set_speed(self, mode):
        if mode == 'fast':
            self.x_s += 0.1
        elif mode == 'slow':
            self.x_s -= 0.1 if self.x_s >= 0.1 else 0

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 50, 50))


robot = Robot(400, 300)
robot_2 = Robot(400, 500)
font = pygame.font.Font(None, 40)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            robot_2.update(True)

            if event.key == pygame.K_LEFT:
                robot.zandi('left', True)
            elif event.key == pygame.K_RIGHT:
                robot.zandi('right', True)
            if event.key == pygame.K_2:
                robot.set_speed('fast')
            elif event.key == pygame.K_1:
                robot.set_speed('slow')
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                robot.zandi('left', False)
            elif event.key == pygame.K_RIGHT:
                robot.zandi('right', False)

    robot.update()
    screen.fill(BLACK)
    robot.draw(screen)
    robot_2.draw(screen)

    text = font.render('bot is moving', True, WHITE)
    text_speed = font.render(str(robot.x_s), True, WHITE)
    screen.blit(text, (10, 10))
    screen.blit(text_speed, (10, 30))
    pygame.display.flip()

pygame.quit()


