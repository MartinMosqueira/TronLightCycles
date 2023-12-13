import pygame
import sys
from pygame.locals import *

# Initialize pygame
pygame.init()

ancho = 1000
alto = 600

# window
window = pygame.display.set_mode((1000, 600))

# title and icon
pygame.display.set_caption("Hello World")
icon = pygame.image.load("images/tron-icon.jpg")
pygame.display.set_icon(icon)

# load sprite cycle orange
playerOrange = pygame.image.load("images/cycle-orange.png")

# load sprite cycle blue
playerBlue = pygame.image.load("images/cycle-blue.png")

color = (8, 4, 36)
edges = (112, 140, 148)

# clock
clock = pygame.time.Clock()

running = True
player_pos = pygame.Vector2(window.get_width() / 2, window.get_height() / 2)
dt = 0
direction = pygame.Vector2(0, 0)  # Inicialmente sin movimiento
angle = 0  # Inicialmente sin rotación
lines = []

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    window.fill(color)

    grosor_borde = 10
    pygame.draw.rect(window, edges, (0, 0, ancho, grosor_borde))  # Borde superior
    pygame.draw.rect(window, edges, (0, alto - grosor_borde, ancho, grosor_borde))  # Borde inferior
    pygame.draw.rect(window, edges, (0, 0, grosor_borde, alto))  # Borde izquierdo
    pygame.draw.rect(window, edges, (ancho - grosor_borde, 0, grosor_borde, alto))  # Borde derecho

    # Dibujar líneas de rastro
    if len(lines) >= 2:
        pygame.draw.lines(window, (252, 212, 4), False, lines, 5)

    # Draw rotated cycle orange
    rotated_player = pygame.transform.rotate(playerOrange, angle)
    player_rect = rotated_player.get_rect(center=player_pos)
    window.blit(rotated_player, player_rect.topleft)

    keys = pygame.key.get_pressed()
    new_direction = pygame.Vector2(0, 0)
    if keys[pygame.K_w]:
        new_direction.y = -1
    if keys[pygame.K_s]:
        new_direction.y = 1
    if keys[pygame.K_a]:
        new_direction.x = -1
    if keys[pygame.K_d]:
        new_direction.x = 1

    # Si se ha pulsado alguna tecla de movimiento, actualizar la dirección
    if new_direction.length() != 0:
        direction = new_direction

    # No permite movimientos en diagonal
    if new_direction.x and new_direction.y != 0:
        direction = pygame.Vector2(0, 0)

    # Actualizar ángulo y posición del jugador
    angle = direction.angle_to(pygame.Vector2(0, -1))  # Calcular ángulo con respecto a arriba
    player_pos += direction * 300 * dt

    # Agregar la posición actual a la lista de rastro
    rounded_position = (round(player_pos.x), round(player_pos.y))
    lines.append(rounded_position)

    # Limites de la pantalla
    player_pos.x = max(30, min(player_pos.x, ancho - 30))
    player_pos.y = max(30, min(player_pos.y, alto - 30))

    pygame.display.update()

    dt = clock.tick(60) / 1000

pygame.quit()
