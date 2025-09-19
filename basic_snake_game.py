import pygame
import random
import time

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = pygame.Rect(200, 250, 50, 50)
apple = pygame.Rect(600, 250, 50, 50)
clock = pygame.time.Clock()

# Velocity
dx, dy = 0, 0   # start moving right

score = 0

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx, dy = -5, 0
            if event.key == pygame.K_RIGHT:
                dx, dy = 5, 0
            if event.key == pygame.K_UP:
                dx, dy = 0, -5
            if event.key == pygame.K_DOWN:
                dx, dy = 0, 5

    # Apply movement every frame
    player.x += dx
    player.y += dy

    if 0 >= player.x or player.x >= (SCREEN_WIDTH - player.width) or 0 >= player.y or player.y >= (SCREEN_HEIGHT - player.height):
        print(f"You scored: {score}")

        dx = 0
        dy = 0

        run = False

    # Eat apple
    if player.colliderect(apple):
        apple.x = random.randint(0, SCREEN_WIDTH - apple.width)
        apple.y = random.randint(0, SCREEN_HEIGHT - apple.height)

        score += 1

    # Drawing
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), player)
    pygame.draw.rect(screen, (255, 0, 0), apple)

    pygame.display.update()
    clock.tick(60)

# death animation stuff
# Green -> Red -> Green
pygame.draw.rect(screen, (255, 0, 0), player)
pygame.display.update()

time.sleep(0.5)

pygame.draw.rect(screen, (0, 255, 0), player)
pygame.display.update()

time.sleep(0.25)

pygame.quit()
