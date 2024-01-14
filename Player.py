import pygame


class Player:
    def __init__(self, x, y, colour, direction, image):
        self.x = x
        self.y = y
        self.colour = colour
        self.direction = direction
        self.direction_vector = pygame.Vector2(0, 0)
        self.image = pygame.image.load(image)
        self.score = 0
        self.trail = []
        self.alive = True
        self.angle = 0

    def draw(self, board):
        if self.alive:
            self.trail.append((self.x, self.y))
            for coord in self.trail:
                pygame.draw.rect(board.screen, self.colour, [coord[0] + 1, coord[1] + 1,
                                                             (board.width // 40), (board.height // 40)])

            rotated_player = pygame.transform.rotate(self.image, self.angle)
            board.screen.blit(rotated_player, (self.x, self.y))

    def check_boundary(self):
        if self.x >= 800 or self.x < 0 or self.y >= 800 or self.y < 0:
            self.alive = False

    def check_for_match(self, grid):
        if grid[self.x // 20 - 1][self.y // 20 - 1]:
            self.alive = False
        grid[self.x // 20 - 1][self.y // 20 - 1] = True

    def update_angle(self, direction):
        self.angle = direction.angle_to(pygame.Vector2(0, -1))

    def update_direction(self, direction):
        if self.alive:
            self.direction_vector = direction

    def update_position(self):
        if self.alive:
            if self.direction == "left":
                self.x -= 20
                self.update_direction(pygame.Vector2(-1, 0))
            elif self.direction == "right":
                self.x += 20
                self.update_direction(pygame.Vector2(1, 0))
            elif self.direction == "up":
                self.y -= 20
                self.update_direction(pygame.Vector2(0, -1))
            elif self.direction == "down":
                self.y += 20
                self.update_direction(pygame.Vector2(0, 1))

        self.update_angle(self.direction_vector)

    def update_score(self):
        self.score += 1
