import pygame

# Pygame initialisatsioon
pygame.init()

# Ekraani suurus
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ruudustik")

# Ruudustiku joonistamise funktsioon
def joonista_ruudustik(ekraan, ruudu_suurus, read, veerud, varv):
    for rida in range(read):
        for veerg in range(veerud):
            x = veerg * ruudu_suurus
            y = rida * ruudu_suurus
            ruut = pygame.Rect(x, y, ruudu_suurus, ruudu_suurus)
            pygame.draw.rect(ekraan, varv, ruut, 1)

# Mängu tsükkel funktsioonina
def kaivita_mang(ruudu_suurus, read, veerud, varv):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Tausta täitmine mustaga
        joonista_ruudustik(screen, ruudu_suurus, read, veerud, varv)
        pygame.display.flip()  # Ekraani uuendamine

    pygame.quit()

# Käivita mäng muudetavate parameetritega
kaivita_mang(32, 15, 20, (255, 255, 255))
