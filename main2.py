import pygame
import random
import time
import math

# Initialize pygame
pygame.init()

# Set screen dimensions
SCREEN_W = 800
SCREEN_H = 600

# Create the game window
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

# Set window caption
pygame.display.set_caption("Игра ТИР")  # Translation: "Shooting Game"

# Load and set window icon
icon = pygame.image.load("img/stock4.jpg")
pygame.display.set_icon(icon)

# Load target image and set dimensions
target_img = pygame.image.load("img/target.png")
target_img = pygame.transform.scale(target_img, (50, 50))
target_width = 50
target_height = 50

# Initialize target coordinates
target_x = random.randint(0, SCREEN_W - target_width)
target_y = random.randint(0, SCREEN_H - target_height)

# Initialize color
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Load font and set initial game variables
font = pygame.font.Font(None, 36)
start_time = time.time()
last_change_time = start_time
score = 0

# Initialize target speed in x and y directions
target_speed_x = random.choice([-1, 1]) * random.randint(2, 5)
target_speed_y = random.choice([-1, 1]) * random.randint(2, 5)

# Set initial movement type
movement_type = 'linear'

# Flag to control game loop
running = True

# Game loop
while running:
    elapsed_time = int(time.time() - start_time)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x <= mouse_x <= target_x + target_width and target_y <= mouse_y <= target_y + target_height:
                score += 1
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                target_x = random.randint(0, SCREEN_W - target_width)
                target_y = random.randint(0, SCREEN_H - target_height)
                target_speed_x = random.choice([-1, 1]) * random.randint(2, 5)
                target_speed_y = random.choice([-1, 1]) * random.randint(2, 5)

    if elapsed_time % 10 == 0 and elapsed_time != last_change_time:
        last_change_time = elapsed_time
        movement_type = random.choice(['linear', 'sinusoidal', 'circular'])

    if movement_type == 'linear':
        target_x += target_speed_x
        target_y += target_speed_y
    elif movement_type == 'sinusoidal':
        target_x += target_speed_x
        target_y = (SCREEN_H // 2) + int(100 * math.sin(target_x * 0.05))
    elif movement_type == 'circular':
        angle = (elapsed_time % 360) * (math.pi / 180)
        target_x = (SCREEN_W // 2) + int(100 * math.cos(angle))
        target_y = (SCREEN_H // 2) + int(100 * math.sin(angle))

    # Bounce off the walls
    if target_x <= 0 or target_x >= SCREEN_W - target_width:
        target_speed_x = -target_speed_x
    if target_y <= 0 or target_y >= SCREEN_H - target_height:
        target_speed_y = -target_speed_y

    # Update screen
    screen.fill(color)
    screen.blit(target_img, (target_x, target_y))

    # Display score and elapsed time
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    time_text = font.render(f'Time: {elapsed_time}', True, (255, 255, 255))
    screen.blit(score_text, (10, SCREEN_H - 40))
    screen.blit(time_text, (10, SCREEN_H - 80))

    pygame.display.update()

# Quit pygame
pygame.quit()