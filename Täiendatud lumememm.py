import math

import pygame

pygame.init()

# Akna suurus ja seadistused
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lumemees – Tauri Tabur")

# Värvid
SKY_BLUE = (135, 206, 235)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BROWN = (139, 69, 19)
YELLOW = (255, 255, 0)
GRAY = (200, 200, 200)
ORANGE = (255, 165, 0)

# Mängutsükkel
running = True
while running:
    screen.fill(SKY_BLUE)  # Taust helesiniseks

    # Päike
    pygame.draw.circle(screen, YELLOW, (350, 50), 30)
    for i in range(0, 360, 30):
        angle = math.radians(i)
        x = 350 + 45 * math.cos(angle)
        y = 50 + 45 * math.sin(angle)
        pygame.draw.line(screen, YELLOW, (350, 50), (x, y), 3)

    # Pilved
    pygame.draw.ellipse(screen, WHITE, (50, 50, 80, 40))
    pygame.draw.ellipse(screen, WHITE, (10, 100, 80, 40))
    pygame.draw.ellipse(screen, WHITE, (100, 40, 90, 50))
    pygame.draw.ellipse(screen, WHITE, (250, 60, 100, 50))

    # Lumememme keha
    pygame.draw.circle(screen, WHITE, (200, 280), 60)  # Alumine osa
    pygame.draw.circle(screen, WHITE, (200, 190), 45)  # Keskmine osa
    pygame.draw.circle(screen, WHITE, (200, 120), 35)  # Pea

    # Käed (pruunid oksad)
    pygame.draw.line(screen, BROWN, (155, 190), (100, 140), 5)
    pygame.draw.line(screen, BROWN, (245, 190), (300, 140), 5)

    # Hari (paremas käes, suunatud alla)
    pygame.draw.line(screen, BROWN, (300, 120), (310, 200), 5)
    pygame.draw.rect(screen, ORANGE, (305, 200, 12, 20))

    # Nööbid
    pygame.draw.circle(screen, BLACK, (200, 190), 5)
    pygame.draw.circle(screen, BLACK, (200, 215), 5)
    pygame.draw.circle(screen, BLACK, (200, 240), 5)

    # Silmad
    pygame.draw.circle(screen, BLACK, (190, 110), 4)
    pygame.draw.circle(screen, BLACK, (210, 110), 4)

    # Nina 
    pygame.draw.polygon(screen, RED, [(195, 120), (205, 120), (200, 135)])

    # Kübar
    pygame.draw.rect(screen, BLACK, (175, 90, 50, 10))  # Kübara alumine osa
    pygame.draw.rect(screen, BLACK, (185, 60, 30, 30))  # Kübara pealisosa

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
