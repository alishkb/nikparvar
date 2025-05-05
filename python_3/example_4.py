import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("تمرین پیشرفته - بازی مار")

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)


class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = GREEN
        self.speed_x = 0
        self.speed_y = 0
        self.radius = 25
        self.foods = 0

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x - self.radius < 0 or self.x + self.radius > 800 or self.y - self.radius < 0 or self.y + self.radius > 600:
            return False
        return True

    def move(self, direction):
        speed = 1
        if direction == "left" and self.speed_x != speed:
            self.speed_x = -speed
            self.speed_y = 0
        elif direction == "right" and self.speed_x != -speed:
            self.speed_x = speed
            self.speed_y = 0
        elif direction == "up" and self.speed_y != speed:
            self.speed_y = -speed
            self.speed_x = 0
        elif direction == "down" and self.speed_y != -speed:
            self.speed_y = speed
            self.speed_x = 0

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = YELLOW
        self.active = True

    def check_collision(self, snake):
        if self.active:
            distance = ((self.x - snake.x) ** 2 + (self.y - snake.y) ** 2) ** 0.5
            if distance < snake.radius + 15:
                self.active = False
                snake.foods += 1
                snake.radius += 5
                return True
        return False

    def draw(self, screen):
        if self.active:
            pygame.draw.circle(screen, self.color, (self.x, self.y), 15)


def create_food():
    x = random.randint(50, 750)
    y = random.randint(50, 550)
    return Food(x, y)


snake = Snake(400, 300)
foods = [create_food()]
font = pygame.font.Font(None, 50)
game_over = False
win = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif not game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.move("left")
                elif event.key == pygame.K_RIGHT:
                    snake.move("right")
                elif event.key == pygame.K_UP:
                    snake.move("up")
                elif event.key == pygame.K_DOWN:
                    snake.move("down")

    if not game_over:
        if not snake.update():
            game_over = True
            win = False
        new_foods = []
        for food in foods:
            if food.check_collision(snake):
                new_foods.append(create_food())
            else:
                new_foods.append(food)
        foods = new_foods
        if snake.foods >= 15:
            game_over = True
            win = True

    screen.fill(BLACK)
    snake.draw(screen)
    for food in foods:
        food.draw(screen)
    if game_over:
        text = font.render("You WIN!" if win else "You LOST", True, WHITE)
        text_width = text.get_width()
        screen.blit(text, (400 - text_width // 2, 300))
    score_text = font.render(f"BLOCKS: {snake.foods}", True, WHITE)
    screen.blit(score_text, (10, 10))
    pygame.display.flip()

pygame.quit()