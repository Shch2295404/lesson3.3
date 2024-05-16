import pygame
import random


pygame.init()
SCREEN_W = 800
SCREEN_H = 600
screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))

pygame.display.set_caption("Игра ТИР")
icon = pygame.image.load("img/stock4.jpg")
pygame.display.set_icon(icon)
target_img = pygame.image.load("img/target.png")
# target_img = pygame.transform.scale(target_img, (50, 50))
target_width = 50
target_height = 50

target_x = random.randint(0, SCREEN_W - target_width)
target_y = random.randint(0, SCREEN_H - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            # print(event.pos)
            # mouse_x, mouse_y = event.pos.get()
            mouse_x, mouse_y = pygame.mouse.get_pos()
            print(mouse_x, mouse_y)
            if mouse_x >= target_x and mouse_x <= target_x + target_width and mouse_y >= target_y and mouse_y <= target_y + target_height:
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                target_x = random.randint(0, SCREEN_W - target_width)
                target_y = random.randint(0, SCREEN_H - target_height)
        # target_x = event.pos[0] - target_width // 2
        # target_y = event.pos[1] - target_height // 2
    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()

pygame.quit()
