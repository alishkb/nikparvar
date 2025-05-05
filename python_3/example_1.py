import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("تمرین - تغییر رنگ پویا")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
COLORS = [WHITE, RED, BLUE, GREEN]


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.base_color = WHITE  # رنگ عادی
        self.color = self.base_color
        self.speed_x = 0
        self.speed_y = 0
        self.items = 0  # تعداد آیتم‌های لمس‌شده

    def update(self):
        if self.x + self.speed_x > 25 and self.x + self.speed_x < 775:
            self.x += self.speed_x
        if self.y + self.speed_y > 25 and self.y + self.speed_y < 575:
            self.y += self.speed_y

    def move(self, direction, is_pressed):
        speed = 5 if is_pressed else 0
        if direction == "left":
            self.speed_x = -speed
        elif direction == "right":
            self.speed_x = speed
        elif direction == "up":
            self.speed_y = -speed
        elif direction == "down":
            self.speed_y = speed

    def set_color(self, background_color):
        # اگه پس‌زمینه سفید باشه، بازیکن مشکی می‌شه
        self.color = BLACK if background_color == WHITE else self.base_color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 25)


class Item:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.base_color = RED  # رنگ عادی
        self.color = self.base_color
        self.active = True

    def check_collision(self, player):
        if self.active:
            distance = ((self.x - player.x) ** 2 + (self.y - player.y) ** 2) ** 0.5
            if distance < 50:
                self.active = False
                player.items += 1
                return random.choice(COLORS)  # رنگ جدید برای پس‌زمینه
        return None

    def set_color(self, background_color):
        # اگه پس‌زمینه قرمز باشه، آیتم آبی می‌شه
        self.color = BLUE if background_color == RED else self.base_color

    def draw(self, screen):
        if self.active:
            pygame.draw.circle(screen, self.color, (self.x, self.y), 15)


def create_item():
    x = random.randint(50, 750)
    y = random.randint(50, 550)
    return Item(x, y)


player = Player(400, 300)
items = [create_item()]  # آیتم اولیه
font = pygame.font.Font(None, 40)
background_color = BLACK  # رنگ اولیه پس‌زمینه

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move("left", True)
            elif event.key == pygame.K_RIGHT:
                player.move("right", True)
            elif event.key == pygame.K_UP:
                player.move("up", True)
            elif event.key == pygame.K_DOWN:
                player.move("down", True)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.move("left", False)
            elif event.key == pygame.K_RIGHT:
                player.move("right", False)
            elif event.key == pygame.K_UP:
                player.move("up", False)
            elif event.key == pygame.K_DOWN:
                player.move("down", False)

    player.update()
    new_items = []
    for item in items:
        new_color = item.check_collision(player)
        if new_color:
            background_color = new_color
            new_items.append(create_item())
        else:
            new_items.append(item)
    items = new_items

    # آپدیت رنگ‌ها بر اساس پس‌زمینه
    player.set_color(background_color)
    for item in items:
        item.set_color(background_color)

    screen.fill(background_color)
    player.draw(screen)
    for item in items:
        item.draw(screen)
    score_text = font.render(f"آیتم‌ها: {player.items}", True, WHITE)
    screen.blit(score_text, (10, 10))
    pygame.display.flip()

pygame.quit()