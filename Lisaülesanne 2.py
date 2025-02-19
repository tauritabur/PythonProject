import pygame
import math

# Initsialiseeri Pygame
pygame.init()

# Ekraani seaded (640x480)
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Ülesanne 2")

# Laadin pildid
background = pygame.image.load("bg_shop.jpg")
seller = pygame.image.load("seller.png")
chat_bubble = pygame.image.load("chat.png")
logo = pygame.image.load("VIKK_logo.png")
sword = pygame.image.load("Mõõk.png")
cake = pygame.image.load("tort.png")  # Tort, mille pead ise valima

# Muudan piltide suurust
seller = pygame.transform.scale(seller, (250, 305))
chat_bubble = pygame.transform.scale(chat_bubble, (260, 200))
logo = pygame.transform.scale(logo, (250, 30))
sword = pygame.transform.scale(sword, (80, 200))
cake = pygame.transform.scale(cake, (120, 100))

# Teksti seaded (font ja suurus)
font = pygame.font.SysFont("Arial", 24)  # Sobiv suurus jutumulli jaoks
name_text = font.render("Tere, olen Tauri", True, (255, 255, 255))

# Kaarega teksti loomiseks
arc_font = pygame.font.SysFont("Arial", 20, bold=True)
text = "TULEVIK 2050"
arc_positions = []
radius = 170
center_x, center_y = 130, 167  # Logo keskpunkt
angle_step = math.pi / (len(text) + 12)

for i, char in enumerate(text):
    angle = -math.pi / 2 + (i - len(text) / 2) * angle_step
    x = center_x + int(math.cos(angle) * radius)
    y = center_y + int(math.sin(angle) * radius)
    arc_positions.append((char, (x, y)))

# Positsioonid
seller_x = 105  # Poemüüja vasakul serval
seller_y = 485 - seller.get_height() - 20  # Alumine serv
chat_x = seller_x + 140
chat_y = seller_y - chat_bubble.get_height() + 108  # jutumulli Kohandatud kõrgus
logo_x, logo_y = 30, 50  # Logo vasakusse nurka
sword_x, sword_y = 540, 50  # Mõõk seinale
cake_x, cake_y = 380, 205  # Tort lauale

# Teksti keskele
text_rect = name_text.get_rect(
    center=(chat_x + chat_bubble.get_width() // 2, chat_y + chat_bubble.get_height() // 3 + 10))

# Mängutsükkel
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Joonistan elemendid
    screen.blit(background, (0, 0))
    screen.blit(seller, (seller_x, seller_y))
    screen.blit(chat_bubble, (chat_x, chat_y))
    screen.blit(name_text, text_rect.topleft)
    screen.blit(logo, (logo_x, logo_y))
    screen.blit(sword, (sword_x, sword_y))
    screen.blit(cake, (cake_x, cake_y))

    for char, pos in arc_positions:
        char_render = arc_font.render(char, True, (255, 255, 255))
        screen.blit(char_render, pos)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
