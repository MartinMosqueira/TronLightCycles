import pygame
from pygame.locals import *
import sys
from GameBoard import GameBoard
from Player import Player


class Game:
    def __init__(self):
        # initialize the game engine
        pygame.init()

        self.x = 800
        self.y = 800

        # sets the initial map
        self.board = GameBoard(self.x, self.y)

        # initialize the grid
        self.grid = [[False for _ in range(self.x // 20)] for _ in range(self.y // 20)]

        # initialize the players
        self.players = [Player(self.x // 4, self.y // 4, (28, 112, 196), "right", "images/cycle-blue.png"),
                        Player((self.x * 3) // 4, (self.y * 3) // 4, (252, 212, 4), "left", "images/cycle-orange.png")]

        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

                elif event.type == KEYDOWN:
                    for player in self.players:
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

            # draw board
            self.board.draw()

            # draw players
            for player in self.players:
                player.draw(self.board)

            pygame.display.update()

            # check for collisions
            for player in self.players:
                player.check_boundary()
                player.check_for_match(self.grid)

            # update positions
            if all(player.alive for player in self.players):
                for player in self.players:
                    player.update_position()

            # update scores
            for player in self.players:
                if player.alive:
                    player.update_score()

            self.clock.tick(15)
            pygame.display.update()

        print('p1 score: ' + str(self.players[0].score))
        print('p2 score: ' + str(self.players[1].score))

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()
