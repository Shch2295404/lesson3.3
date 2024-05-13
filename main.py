import pygame
import random


pygame.init()
SCREEN_W = 800
SCREEN_H = 600
screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))

pygame.display.set_caption("Игра ТИР")
icon = pygame.image.load("img/stock.jpg")
pygame.display.set_icon(icon)
target_img = pygame.image.load("img/target.png")
# target_img = pygame.transform.scale(target_img, (50, 50))
target_width = 50
target_height = 50

target_x = random.randint(0, SCREEN_W - target_width)
target_y = random.randint(0, SCREEN_H - target_height)

running = True
while running:
    pass

pygame.quit()
