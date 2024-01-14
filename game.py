import pygame
from pygame.locals import *
import sys
from GameBoard import GameBoard
from Player import Player

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

# sets the initial map
board = GameBoard(x, y)
board.draw()

# sets the players 1 initial variables
p1x = x // 4
p1y = y // 4
# sets the initial direction
p1direction = "right"

# sets the players 2 initial variables
p2x = (x * 3) // 4
p2y = (y * 3) // 4
# sets the initial direction
p2direction = "left"

# Rotating the sprite 1
direction = pygame.Vector2(0, 0)

# Rotating the sprite 2
direction2 = pygame.Vector2(0, 0)

players = [Player(p1x, p1y, blue, p1direction, "images/cycle-blue.png"),
           Player(p2x, p2y, orange, p2direction, "images/cycle-orange.png")]

grid = [[False for _ in range(x // 20)] for _ in range(y // 20)]

clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == KEYDOWN:
            for player in players:
                if event.key == K_a:
                    if player.direction != "right":
                        player.direction = "left"
                elif event.key == K_d:
                    if player.direction != "left":
                        player.direction = "right"
                elif event.key == K_w:
                    if player.direction != "down":
                        player.direction = "up"
                elif event.key == K_s:
                    if player.direction != "up":
                        player.direction = "down"

        elif event.type == pygame.K_SPACE:
            pass

    board.screen.fill(background)
    board.draw()

    for player in players:
        player.draw(board)

    pygame.display.update()

    # check for collisions
    for player in players:
        player.check_boundary()
        player.check_for_match(grid)

    # update positions
    if players[0].alive and players[1].alive:
        for player in players:
            player.update_position()

    # update scores
    for player in players:
        if player.alive:
            player.update_score()

    clock.tick(15)
    pygame.display.update()

print('p1 score: ' + str(players[0].score))
print('p2 score: ' + str(players[1].score))

pygame.quit()
sys.exit()
