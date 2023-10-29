import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
CHARACTER_COLOR = (255, 0, 0)
ITEM_COLOR = (0, 255, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basic Pygame Game")

# Character setup
character_x = WIDTH // 2
character_y = HEIGHT - 50
character_speed = 0.5
character_radius = 20

# Item setup
item_x = random.randint(0, WIDTH)
item_y = random.randint(0, HEIGHT)
item_radius = 10

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_x -= character_speed
    if keys[pygame.K_RIGHT]:
        character_x += character_speed
    if keys[pygame.K_UP]:
        character_y -= character_speed
    if keys[pygame.K_DOWN]:
        character_y += character_speed

    # Collision detection
    distance = ((item_x - character_x) ** 2 + (item_y - character_y) ** 2) ** 0.5
    if distance <= character_radius + (item_radius / 2):
        item_x = random.randint(0, WIDTH)
        item_y = random.randint(0, HEIGHT)
        score += 1

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Draw character
    pygame.draw.circle(
        screen, CHARACTER_COLOR, (character_x, character_y), character_radius
    )

    # Draw item
    pygame.draw.circle(screen, ITEM_COLOR, (item_x, item_y), item_radius)

    # Display score
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

# Clean up
pygame.quit()
