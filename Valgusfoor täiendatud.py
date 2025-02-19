import pygame

pygame.init()

# Akna suurus ja seadistused
WIDTH, HEIGHT = 350, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Foor – Tauri Tabur")

# Värvid
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
GRAY = (100, 100, 100)
DARK_GRAY = (50, 50, 50)
BLUE = (0, 0, 255)

# Mängutsükkel
running = True
while running:
    screen.fill(BLACK)  # Taust mustaks

    # Foori post
    pygame.draw.rect(screen, DARK_GRAY, (150, 230, 20, 170))

    # Foori kast
    pygame.draw.rect(screen, GRAY, (105, 30, 110, 200), 2)

    # Valgusfoori tuled
    pygame.draw.circle(screen, RED, (160, 70), 30)    # Punane tuli
    pygame.draw.circle(screen, YELLOW, (160, 130), 30)  # Kollane tuli
    pygame.draw.circle(screen, GREEN, (160, 190), 30)  # Roheline tuli

    # 1. Joonista trapetsikujuline alus (45° nurgad)
    base_points = [(120, 400), (200, 400), (180, 350), (140, 350)]
    pygame.draw.polygon(screen, WHITE, base_points)  # Aluse taust

    # 2. Jaga alus kolmeks horisontaalseks ribaks
    ribbon_height = (400 - 350) // 3  # Riba kõrgus ~16.6px
    # Sinine riba (ülemine)
    pygame.draw.rect(screen, BLUE, (140, 350, 40, ribbon_height))
    # Must riba (keskmine)
    pygame.draw.rect(screen, BLACK, (140, 350 + ribbon_height, 40, ribbon_height))
    # Valge riba (alumine)
    pygame.draw.rect(screen, WHITE, (140, 350 + 2 * ribbon_height, 40, ribbon_height))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
