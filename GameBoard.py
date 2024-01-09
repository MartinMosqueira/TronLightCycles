import pygame


class GameBoard:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.lineColor = (0, 0, 0)
        self.backgroundColor = (8, 4, 36)
        self.screen = pygame.display.set_mode((width, height))

    def draw(self):
        self.screen.fill(self.backgroundColor)
        for i in range(0, self.width, 20):
            pygame.draw.line(self.screen, self.lineColor, [i, 0], [i, self.width], 1)
            pygame.draw.line(self.screen, self.lineColor, [0, i], [self.height, i], 1)
