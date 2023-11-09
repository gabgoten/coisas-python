# JOGNA1 –Entrega N1.C– Gabriel Rodrigues, Vanessa Byork, Jonatas Cirino e Lucas Freitas

import pygame
pygame.init()

Largura = 750
Altura = 750
tela = pygame.display.set_mode((Largura, Altura))

# fazendo o fundo
pygame.draw.rect(tela, (255, 255, 255), (0, 0, Largura, Altura), 0)

# fazendo o caminho de todas as cores
pygame.draw.rect(tela, (0, 255, 0), (50, 200, 50, 200), 0)
pygame.draw.rect(tela, (0, 255, 0), (50, 350, 250, 50), 0)

pygame.draw.rect(tela, (255, 255, 0), (350, 50, 50, 250), 0)
pygame.draw.rect(tela, (255, 255, 0), (350, 50, 250, 50), 0)

pygame.draw.rect(tela, (255, 0, 0), (350, 400, 50, 250), 0)
pygame.draw.rect(tela, (255, 0, 0), (300, 650, 100, 50), 0)

pygame.draw.rect(tela, (0, 0, 255), (650, 400, 50, 50), 0)
pygame.draw.rect(tela, (0, 0, 255), (450, 350, 250, 50), 0)

# fazendo as linhas
linha_x = 50
for i in range(14):
    pygame.draw.line(tela, (128, 128, 128), (linha_x, 750), (linha_x, 0), 2)
    linha_x += 50

linha_y = 50
for i in range(14):
    pygame.draw.line(tela, (128, 128, 128), (750, linha_y), (0, linha_y), 2)
    linha_y += 50

# fazendo os quadrados grandes
pygame.draw.rect(tela, (0, 240, 0), (0, 0, 300, 300), 0)
pygame.draw.rect(tela, (240, 240, 0), (450, 0, 300, 300), 0)
pygame.draw.rect(tela, (240, 0, 0), (0, 450, 300, 300), 0)
pygame.draw.rect(tela, (0, 0, 240), (450, 450, 300, 300), 0)

# fazendo os quadrados pequenos
pygame.draw.rect(tela, (255, 255, 255), (50, 50, 200, 200), 0)
pygame.draw.rect(tela, (255, 255, 255), (500, 50, 200, 200), 0)
pygame.draw.rect(tela, (255, 255, 255), (50, 500, 200, 200), 0)
pygame.draw.rect(tela, (255, 255, 255), (500, 500, 200, 200), 0)

# fazendo o quadrado no meio (junto com os triangulos)
pygame.draw.rect(tela, (255, 255, 255), ((Largura // 2) - 74, (Altura // 2) - 74, 150, 150), 0)
pygame.draw.polygon(tela, (0, 255, 0), ((300, 300), (375, 375), (300, 450)))
pygame.draw.polygon(tela, (255, 0, 0), ((450, 450), (375, 375), (300, 450)))
pygame.draw.polygon(tela, (0, 0, 255), ((450, 450), (375, 375), (450, 300)))
pygame.draw.polygon(tela, (255, 255, 0), ((300, 300), (375, 375), (450, 300)))

# fazendo os circulos (players)
pygame.draw.circle(tela, (0, 255, 0), (100, 100), 20, 0)
pygame.draw.circle(tela, (0, 0, 0), (100, 100), 20, 3)
pygame.draw.circle(tela, (0, 255, 0), (200, 100), 20, 0)
pygame.draw.circle(tela, (0, 0, 0), (200, 100), 20, 3)
pygame.draw.circle(tela, (0, 255, 0), (100, 200), 20, 0)
pygame.draw.circle(tela, (0, 0, 0), (100, 200), 20, 3)
pygame.draw.circle(tela, (0, 255, 0), (200, 200), 20, 0)
pygame.draw.circle(tela, (0, 0, 0), (200, 200), 20, 3)

pygame.draw.circle(tela, (255, 255, 0), (550, 100), 20, 0)
pygame.draw.circle(tela, (0, 0, 0), (550, 100), 20, 3)
pygame.draw.circle(tela, (255, 255, 0), (650, 100), 20, 0)
pygame.draw.circle(tela, (0, 0, 0), (650, 100), 20, 3)
pygame.draw.circle(tela, (255, 255, 0), (550, 200), 20, 0)
pygame.draw.circle(tela, (0, 0, 0), (550, 200), 20, 3)
pygame.draw.circle(tela, (255, 255, 0), (650, 200), 20, 0)
pygame.draw.circle(tela, (0, 0, 0), (650, 200), 20, 3)

pygame.draw.circle(tela, (255, 0, 0), (100, 550), 20, 0)
pygame.draw.circle(tela, (0, 0, 0), (100, 550), 20, 3)
pygame.draw.circle(tela, (255, 0, 0), (200, 550), 20, 0)
pygame.draw.circle(tela, (0, 0, 0), (200, 550), 20, 3)
pygame.draw.circle(tela, (255, 0, 0), (100, 650), 20, 0)
pygame.draw.circle(tela, (0, 0, 0), (100, 650), 20, 3)
pygame.draw.circle(tela, (255, 0, 0), (200, 650), 20, 0)
pygame.draw.circle(tela, (0, 0, 0), (200, 650), 20, 3)

pygame.draw.circle(tela, (0, 0, 255), (550, 550), 20, 0)
pygame.draw.circle(tela, (0, 0, 0), (550, 550), 20, 3)
pygame.draw.circle(tela, (0, 0, 255), (650, 550), 20, 0)
pygame.draw.circle(tela, (0, 0, 0), (650, 550), 20, 3)
pygame.draw.circle(tela, (0, 0, 255), (550, 650), 20, 0)
pygame.draw.circle(tela, (0, 0, 0), (550, 650), 20, 3)
pygame.draw.circle(tela, (0, 0, 255), (650, 650), 20, 0)
pygame.draw.circle(tela, (0, 0, 0), (650, 650), 20, 3)

#escrevendo o título
pygame.display.set_caption("LUDO")

rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    pygame.display.update()

pygame.quit()


