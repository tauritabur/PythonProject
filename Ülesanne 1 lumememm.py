from turtle import width

import pygame

pygame.init()

# Akna suurus ja seadistused
WIDTH, HEIGHT = 300, 301
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lumemees – Tauri Tabur")

# Värvid
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Mängutsükkel
running = True
while running:
    screen.fill(BLACK)  # Taust mustaks

    # Joonista lumememm
    pygame.draw.circle(screen, WHITE, (150, 210), 50)  # Alumine kehaosa
    pygame.draw.circle(screen, WHITE, (150, 130), 38)  # Keskmine osa
    pygame.draw.circle(screen, WHITE, (150, 67), 30)   # Pea

    # Silmad
    pygame.draw.circle(screen, BLACK, (140, 65), 4)
    pygame.draw.circle(screen, BLACK, (160, 65), 4)

    # Nina
    pygame.draw.polygon(screen, RED, [(145, 75), (155, 75), (150, 90)])

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()