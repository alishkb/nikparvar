"""

"""

import pygame

# مقداردهی اولیه Pygame
pygame.init()

# تنظیم اندازه پنجره
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("مستطیل متحرک")

# تنظیم رنگ مستطیل
rect_color = (255, 0, 0)

# تنظیم موقعیت و اندازه مستطیل
rect_x = 100
rect_y = 100
rect_width = 50
rect_height = 50

# تنظیم سرعت حرکت مستطیل
speed = 5

# حلقه اصلی بازی
running = True
while running:
    # مدیریت رویدادها
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # دریافت وضعیت کلیدها
    keys = pygame.key.get_pressed()

    # حرکت مستطیل با کلیدهای جهت‌دار
    if keys[pygame.K_LEFT]:
        rect_x -= speed
    if keys[pygame.K_RIGHT]:
        rect_x += speed
    if keys[pygame.K_UP]:
        rect_y -= speed
    if keys[pygame.K_DOWN]:
        rect_y += speed

    # بررسی برخورد با لبه‌های پنجره
    if rect_x < 0:
        rect_x = 0
    elif rect_x > width - rect_width:
        rect_x = width - rect_width

    if rect_y < 0:
        rect_y = 0
    elif rect_y > height - rect_height:
        rect_y = height - rect_height

    # پاکسازی صفحه نمایش
    screen.fill((255, 255, 255))

    # رسم مستطیل
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))

    # به‌روزرسانی صفحه نمایش
    pygame.display.flip()

# خروج از Pygame
pygame.quit()