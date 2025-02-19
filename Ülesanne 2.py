import pygame

# Initsialiseeri Pygame
pygame.init()

# Ekraani seaded (640x480)
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Ülesanne 2")

# Laadin pildid
background = pygame.image.load("bg_shop.jpg")
seller = pygame.image.load("seller.png")
chat_bubble = pygame.image.load("chat.png")

seller = pygame.transform.scale(seller, (250, 305))
chat_bubble = pygame.transform.scale(chat_bubble, (260, 200))

# Teksti seaded (font ja suurus)
font = pygame.font.SysFont("Arial", 24)  # Sobiv suurus jutumulli jaoks
name_text = font.render("Tere, olen Tauri", True, (255, 255, 255))

# Positsioneerin elemendid täpselt nagu näidispildil
seller_x = 105  # Poemüüja vasakul serval
seller_y = 485 - seller.get_height() - 20  # Alumine serv
chat_x = seller_x + 140
chat_y = seller_y - chat_bubble.get_height() + 108  # jutumulli Kohandatud kõrgus

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

    pygame.display.flip()
    clock.tick(30)

pygame.quit()