from pygame.locals import *
import pygame


class Player:
    def __init__(self, x, y, colour, direction, board, image):
        self.x = x
        self.y = y
        self.colour = colour
        self.direction = direction
        self.board = board
        self.image = pygame.image.load(image)
        self.score = 0
        self.trail = []
        self.alive = True
        self.angle = 0

    def event(self, event):

        if event.type == KEYDOWN:
            if event.key == K_a:
                if self.direction != "right":
                    self.direction = "left"
            elif event.key == K_d:
                if self.direction != "left":
                    self.direction = "right"
            elif event.key == K_w:
                if self.direction != "down":
                    self.direction = "up"
            elif event.key == K_s:
                if self.direction != "up":
                    self.direction = "down"

        elif event.type == pygame.K_SPACE:
            pass

    def draw_player(self):
        if self.alive:
            self.trail.append((self.x, self.y))

            self.board.screen.fill(self.board.backgroundColour)

            for coord in self.trail:
                pygame.draw.rect(self.board.screen, self.colour, [coord[0] + 1, coord[1] + 1,
                                                                  (self.board.width // 40), (self.board.width // 40)])

            rotated_player = pygame.transform.rotate(self.image, self.angle)
            self.board.screen.blit(rotated_player, (self.x, self.y))
            pygame.display.update()

    def move_player(self):
        new_direction = pygame.Vector2(0, 0)
        if self.alive:
            if self.direction == "left":
                self.x -= 20
                new_direction.x = -1
            elif self.direction == "right":
                self.x += 20
                new_direction.x = 1
            elif self.direction == "up":
                self.y -= 20
                new_direction.y = -1
            elif self.direction == "down":
                self.y += 20
                new_direction.y = 1

        if new_direction.length() != 0:
            self.direction = new_direction

        self.angle = self.direction.angle_to(pygame.Vector2(0, -1))

    def score_player(self):
        if self.alive:
            self.score += 1
