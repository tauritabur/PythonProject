import pygame

pygame.init()

# Akna suurus ja seadistused
WIDTH, HEIGHT = 302, 301
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Foor – Tauri Tabur")

# Värvid
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
GRAY = (100, 100, 100)

# Mängutsükkel
running = True
while running:
    screen.fill(BLACK)  # Taust mustaks

    # foori kast
    pygame.draw.rect(screen, GRAY, (90, 13, 100, 275), 2)  # Suurem kast ja ainult kontuur

    # kolm valgusfoori tuld
    pygame.draw.circle(screen, RED, (140, 65), 40)    # Punane tuli
    pygame.draw.circle(screen, YELLOW, (140, 150), 40)  # Kollane tuli
    pygame.draw.circle(screen, GREEN, (140, 235), 40)  # Roheline tuli

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
