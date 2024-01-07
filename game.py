import pygame
from pygame.locals import *
import sys

# initialize the game engine
pygame.init()

# colour definitions
background = (8, 4, 36)
black = (0, 0, 0)
orange = (252, 212, 4)
blue = (28, 112, 196)

# sets up the window
x = 800
y = 800
size = [x, y]
screen = pygame.display.set_mode(size)

# title and icon
pygame.display.set_caption("Tron")
icon = pygame.image.load("images/tron-icon.jpg")
pygame.display.set_icon(icon)

# sprite
playerBlue = pygame.image.load("images/cycle-blue.png")

p1x = x // 4
p1y = y // 4
p1alive = True
p1colour = blue
p1score = 0
trail = []

# Rotating the sprite
direction = pygame.Vector2(0, 0)
angle = 0

grid = [[False for _ in range(x // 20)] for _ in range(y // 20)]

p1direction = "right"

clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == KEYDOWN:
            if event.key == K_a:
                if p1direction != "right":
                    p1direction = "left"
            elif event.key == K_d:
                if p1direction != "left":
                    p1direction = "right"
            elif event.key == K_w:
                if p1direction != "down":
                    p1direction = "up"
            elif event.key == K_s:
                if p1direction != "up":
                    p1direction = "down"

        elif event.type == pygame.K_SPACE:
            pass

    if p1alive:
        trail.append((p1x, p1y))

        # sets the initial map
        screen.fill(background)
        for i in range(0, x, 20):
            pygame.draw.line(screen, black, [i, 0], [i, x], 1)
            pygame.draw.line(screen, black, [0, i], [y, i], 1)

        for coord in trail:
            pygame.draw.rect(screen, p1colour, [coord[0] + 1, coord[1] + 1, (x // 40), (x // 40)])

        rotated_player = pygame.transform.rotate(playerBlue, angle)
        screen.blit(rotated_player, (p1x, p1y))
        pygame.display.update()

    if p1x >= 800 or p1x < 0 or p1y >= 800 or p1y < 0:
        p1alive = False

    else:
        if grid[p1x // 20 - 1][p1y // 20 - 1]:
            p1alive = False
        grid[p1x // 20 - 1][p1y // 20 - 1] = True

    new_direction = pygame.Vector2(0, 0)
    if p1alive:
        if p1direction == "left":
            p1x -= 20
            new_direction.x = -1
        elif p1direction == "right":
            p1x += 20
            new_direction.x = 1
        elif p1direction == "up":
            p1y -= 20
            new_direction.y = -1
        elif p1direction == "down":
            p1y += 20
            new_direction.y = 1

    if p1alive:
        p1score += 1
        if new_direction.length() != 0:
            direction = new_direction

    angle = direction.angle_to(pygame.Vector2(0, -1))

    clock.tick(15)

    pygame.display.update()

print(p1score)
pygame.quit()
sys.exit()
