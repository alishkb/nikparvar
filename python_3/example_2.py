import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("تمرین ساده - جمع‌آوری قلب‌ها با فریم")

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = BLUE
        self.speed_x = 0
        self.speed_y = 0
        self.hearts = 0

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

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 25)


class Heart:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = YELLOW
        self.active = True

    def check_collision(self, player):
        if self.active:
            distance = ((self.x - player.x) ** 2 + (self.y - player.y) ** 2) ** 0.5
            if distance < 50:
                self.active = False
                player.hearts += 1
                return True
        return False

    def draw(self, screen):
        if self.active:
            pygame.draw.circle(screen, self.color, (self.x, self.y), 15)


def create_heart():
    x = random.randint(50, 750)
    y = random.randint(50, 550)
    return Heart(x, y)


player = Player(400, 300)
hearts = [create_heart()]
font = pygame.font.Font(None, 50)
clock = pygame.time.Clock()
frame_count = 0
frame_limit = 1800
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

    if not game_over:
        player.update()
        new_hearts = []
        for heart in hearts:
            if heart.check_collision(player):
                new_hearts.append(create_heart())
            else:
                new_hearts.append(heart)
        hearts = new_hearts

        frame_count += 1
        if player.hearts >= 5:
            game_over = True
            win = True
        elif frame_count >= frame_limit:
            game_over = True
            win = False

    screen.fill(BLACK)
    player.draw(screen)
    for heart in hearts:
        heart.draw(screen)
    if game_over:
        text = font.render("بردی!" if win else "باختی!", True, WHITE)
        text_width = text.get_width()
        screen.blit(text, (400 - text_width // 2, 300))
    frames_left = max(0, (frame_limit - frame_count) // 60)
    score_text = font.render(f"قلب‌ها: {player.hearts} زمان: {frames_left}", True, WHITE)
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
