import pygame, sys
from pygame.locals import *

# Initialize pygame
pygame.init()

ancho = 1000
alto = 600

# window
window = pygame.display.set_mode((1000,600))

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

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    window.fill(color)

    # Draw cycle orange
    window.blit(playerOrange, player_pos)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    grosor_borde = 10
    pygame.draw.rect(window, edges, (0, 0, ancho, grosor_borde))  # Borde superior
    pygame.draw.rect(window, edges, (0, alto - grosor_borde, ancho, grosor_borde))  # Borde inferior
    pygame.draw.rect(window, edges, (0, 0, grosor_borde, alto))  # Borde izquierdo
    pygame.draw.rect(window, edges, (ancho - grosor_borde, 0, grosor_borde, alto))  # Borde derecho
    pygame.display.update()
    pygame.display.update()

    dt = clock.tick(60) / 1000

pygame.quit()

'''
    # Rotate image up
    imagen_rotada_arriba = pygame.transform.rotate(playerOrange, 180)
    rect_rotado_arriba = imagen_rotada_arriba.get_rect(center=(500,100))
    window.blit(imagen_rotada_arriba, rect_rotado_arriba.topleft)

    # Rotate image down
    imagen_rotada_abajo = pygame.transform.rotate(playerOrange, 0)
    rect_rotado_abajo = imagen_rotada_abajo.get_rect(center=(500,200))
    window.blit(imagen_rotada_abajo, rect_rotado_abajo.topleft)

    # Rotate image right
    imagen_rotada_derecha = pygame.transform.rotate(playerOrange, 90)
    rect_rotado_derecha = imagen_rotada_derecha.get_rect(center=(500,300))
    window.blit(imagen_rotada_derecha, rect_rotado_derecha.topleft)

    # Rotate image left
    imagen_rotada_izquierda = pygame.transform.rotate(playerOrange, -90)
    rect_rotado_izquierda = imagen_rotada_izquierda.get_rect(center=(500,400))
    window.blit(imagen_rotada_izquierda, rect_rotado_izquierda.topleft)

    # Draw cycle blue

    # Rotate image up
    imagen_rotada_arriba = pygame.transform.rotate(playerBlue, 180)
    rect_rotado_arriba = imagen_rotada_arriba.get_rect(center=(400,100))
    window.blit(imagen_rotada_arriba, rect_rotado_arriba.topleft)

    # Rotate image down
    imagen_rotada_abajo = pygame.transform.rotate(playerBlue, 0)
    rect_rotado_abajo = imagen_rotada_abajo.get_rect(center=(400,200))
    window.blit(imagen_rotada_abajo, rect_rotado_abajo.topleft)

    # Rotate image right
    imagen_rotada_derecha = pygame.transform.rotate(playerBlue, 90)
    rect_rotado_derecha = imagen_rotada_derecha.get_rect(center=(400,300))
    window.blit(imagen_rotada_derecha, rect_rotado_derecha.topleft)

    # Rotate image left
    imagen_rotada_izquierda = pygame.transform.rotate(playerBlue, -90)
    rect_rotado_izquierda = imagen_rotada_izquierda.get_rect(center=(400,400))
    window.blit(imagen_rotada_izquierda, rect_rotado_izquierda.topleft)
    
'''
