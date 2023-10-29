import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
TARGET_COLOR = (255, 0, 0)
GUN_COLOR = (0, 0, 0)
TARGET_SIZE = 30
GUN_WIDTH = 20
TARGET_SPEED = 3
TARGET_SPAWN_INTERVAL = 60  # Adjust this to control target spawn rate

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Target Shooting Game")

# Gun setup
gun_x = WIDTH // 2 - GUN_WIDTH // 2
gun_y = HEIGHT - 20

# Targets setup
targets = []
score = 0

# Game loop
running = True
clock = pygame.time.Clock()
target_spawn_timer = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and gun_x > 0:
        gun_x -= 5
    if keys[pygame.K_RIGHT] and gun_x < WIDTH - GUN_WIDTH:
        gun_x += 5

    # Spawn new targets
    target_spawn_timer += 1
    if target_spawn_timer >= TARGET_SPAWN_INTERVAL:
        target_x = random.randint(0, WIDTH - TARGET_SIZE)
        target_y = 0
        targets.append([target_x, target_y])
        target_spawn_timer = 0

    # Update targets' positions
    new_targets = []
    for target in targets:
        target[1] += TARGET_SPEED
        if target[1] < HEIGHT:
            new_targets.append(target)
    targets = new_targets

    # Check for target collisions
    for target in targets:
        if (
            gun_x < target[0] < gun_x + GUN_WIDTH
            and gun_y > target[1] > gun_y - GUN_WIDTH
        ):
            score += 1
            targets.remove(target)

    # Clear the screen
    screen.fill(WHITE)

    # Draw the gun
    pygame.draw.rect(screen, GUN_COLOR, (gun_x, gun_y, GUN_WIDTH, 10))

    # Draw the targets
    for target in targets:
        pygame.draw.rect(
            screen, TARGET_COLOR, (target[0], target[1], TARGET_SIZE, TARGET_SIZE)
        )

    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Control game speed
    clock.tick(60)

# Clean up
pygame.quit()
