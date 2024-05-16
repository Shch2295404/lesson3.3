import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set screen dimensions
SCREEN_W = 800
SCREEN_H = 600

# Create the game window
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

# Set window title
pygame.display.set_caption("Игра ТИР")  # Translation: "Shooting Game"

# Set window icon
icon = pygame.image.load("img/stock4.jpg")
pygame.display.set_icon(icon)

# Load and resize target image
target_img = pygame.image.load("img/target.png")
target_img = pygame.transform.scale(target_img, (50, 50))
target_width = 50
target_height = 50

# Initialize target position and color
target_x = random.randint(0, SCREEN_W - target_width)
target_y = random.randint(0, SCREEN_H - target_height)
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Set font for text rendering
font = pygame.font.Font(None, 36)

# Record start time and initialize score
start_time = time.time()
score = 0

# Initialize target speed
target_speed_x = random.choice([-1, 1]) * random.randint(2, 5)
target_speed_y = random.choice([-1, 1]) * random.randint(2, 5)

# Flag to control game loop
running = True

# Main game loop
while running:
    # Calculate elapsed time
    elapsed_time = int(time.time() - start_time)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse click hits the target
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x <= mouse_x <= target_x + target_width and target_y <= mouse_y <= target_y + target_height:
                score += 1
                # Change target properties
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                target_x = random.randint(0, SCREEN_W - target_width)
                target_y = random.randint(0, SCREEN_H - target_height)
                target_speed_x = random.choice([-1, 1]) * random.randint(2, 5)
                target_speed_y = random.choice([-1, 1]) * random.randint(2, 5)

    # Update target position based on speed
    target_x += target_speed_x
    target_y += target_speed_y

    # Bounce target on screen edges
    if target_x <= 0 or target_x >= SCREEN_W - target_width:
        target_speed_x = -target_speed_x
    if target_y <= 0 or target_y >= SCREEN_H - target_height:
        target_speed_y = -target_speed_y

    # Render the screen
    screen.fill(color)
    screen.blit(target_img, (target_x, target_y))

    # Render text for score and time
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    time_text = font.render(f'Time: {elapsed_time}', True, (255, 255, 255))
    screen.blit(score_text, (10, SCREEN_H - 40))
    screen.blit(time_text, (10, SCREEN_H - 80))

    # Update display
    pygame.display.update()

# Quit Pygame when the game loop ends
pygame.quit()