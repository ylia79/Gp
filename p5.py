import pygame

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BG_COLOR = (0, 0, 0)
SPEED = 2  # Adjust the scrolling speed

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Infinite Scrolling Background")

# Load the background image
background_image = pygame.image.load("background.jpeg")

# Get the image dimensions
bg_width, bg_height = background_image.get_width(), background_image.get_height()

# Initialize the x-coordinate for scrolling
x = 0

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Scroll the background
    x -= SPEED

    # Reset the x-coordinate to create the infinite effect
    if x < -bg_width:
        x = 0

    # Clear the screen
    screen.fill(BG_COLOR)

    # Draw the background twice for the scrolling effect
    screen.blit(background_image, (x, 0))
    screen.blit(background_image, (x + bg_width, 0))

    # Update the display
    pygame.display.flip()

    # Control game speed
    clock.tick(60)

# Clean up
pygame.quit()
