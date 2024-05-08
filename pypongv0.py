import pygame
import sys
# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH = 800
HEIGHT = 600
BALL_SIZE = 20
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
FPS = 60

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the title of the window
pygame.display.set_caption("Pong")

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define the ball and paddles
ball_x = WIDTH / 2
ball_y = HEIGHT / 2
paddle1_y = HEIGHT / 2 - PADDLE_HEIGHT / 2
paddle2_y = HEIGHT / 2 - PADDLE_HEIGHT / 2

# Set up the game loop
clock = pygame.time.Clock()
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1_y -= 5
    if keys[pygame.K_s]:
        paddle1_y += 5
    if keys[pygame.K_UP]:
        paddle2_y -= 5
    if keys[pygame.K_DOWN]:
        paddle2_y += 5

    # Move the ball
    ball_x += 3
    ball_y += 3

    # Collision detection and response
    if ball_y <= 0 or ball_y >= HEIGHT - BALL_SIZE:
        ball_y = HEIGHT / 2 - BALL_SIZE / 2
    if ball_x <= 0 or ball_x >= WIDTH - BALL_SIZE:
        ball_x = WIDTH / 2 - BALL_SIZE / 2

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (0, paddle1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (WIDTH - PADDLE_WIDTH, paddle2_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_SIZE)

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)