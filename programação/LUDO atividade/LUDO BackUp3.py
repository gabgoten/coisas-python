# JOGNA1 –Entrega N1.C– Gabriel Rodrigues, Vanessa Byork, Jonatas Cirino e Lucas Freitas

import pygame
pygame.init()

Largura = 750
Altura = 750
tela = pygame.display.set_mode((Largura, Altura))

# fazendo os valores
branco = (255, 255, 255)
preto = (0, 0, 0)
verde = (0, 255, 0)
amarelo = (255, 255, 0)
vermelho = (255, 0, 0)
azul = (0, 0, 255)
cinza = (128, 128, 128)

caminho_verde = (50, 200, 50, 200)
caminho_verde1 = (50, 350, 250, 50)
caminho_amarelo = (350, 50, 50, 250)
caminho_amarelo1 = (350, 50, 250, 50)
caminho_vermelho = (350, 400, 50, 250)
caminho_vermelho1 = (300, 650, 100, 50)
caminho_azul = (650, 400, 50, 50)
caminho_azul1 = (450, 350, 250, 50)

bolinha1 = 100
bolinha2 = 200
bolinha3 = 550
bolinha4 = 650

# fazendo o fundo
pygame.draw.rect(tela, (branco), (0, 0, Largura, Altura), 0)

# fazendo o caminho de todas as cores
pygame.draw.rect(tela, (verde), (caminho_verde), 0)
pygame.draw.rect(tela, (verde), (caminho_verde1), 0)

pygame.draw.rect(tela, (amarelo), (caminho_amarelo), 0)
pygame.draw.rect(tela, (amarelo), (caminho_amarelo1), 0)

pygame.draw.rect(tela, (vermelho), (caminho_vermelho), 0)
pygame.draw.rect(tela, (vermelho), (caminho_vermelho1), 0)

pygame.draw.rect(tela, (azul), (caminho_azul), 0)
pygame.draw.rect(tela, (azul), (caminho_azul1), 0)

# fazendo as linhas
linha_x = 50
for i in range(14):
    pygame.draw.line(tela, (cinza), (linha_x, 750), (linha_x, 0), 2)
    linha_x += 50

linha_y = 50
for i in range(14):
    pygame.draw.line(tela, (cinza), (750, linha_y), (0, linha_y), 2)
    linha_y += 50

# fazendo os quadrados grandes
pygame.draw.rect(tela, (verde), (0, 0, 300, 300), 0)
pygame.draw.rect(tela, (amarelo), (450, 0, 300, 300), 0)
pygame.draw.rect(tela, (vermelho), (0, 450, 300, 300), 0)
pygame.draw.rect(tela, (azul), (450, 450, 300, 300), 0)

# fazendo os quadrados pequenos
pygame.draw.rect(tela, (branco), (50, 50, 200, 200), 0)
pygame.draw.rect(tela, (branco), (500, 50, 200, 200), 0)
pygame.draw.rect(tela, (branco), (50, 500, 200, 200), 0)
pygame.draw.rect(tela, (branco), (500, 500, 200, 200), 0)

# fazendo o quadrado no meio (junto com os triangulos)
pygame.draw.rect(tela, (branco), ((Largura // 2) - 74, (Altura // 2) - 74, 150, 150), 0)
pygame.draw.polygon(tela, (verde), ((300, 300), (375, 375), (300, 450)))
pygame.draw.polygon(tela, (vermelho), ((450, 450), (375, 375), (300, 450)))
pygame.draw.polygon(tela, (azul), ((450, 450), (375, 375), (450, 300)))
pygame.draw.polygon(tela, (amarelo), ((300, 300), (375, 375), (450, 300)))

# fazendo as setinhas
pygame.draw.rect(tela, (verde), (5, (Altura // 2) - 5, 25, 10), 0)
pygame.draw.polygon(tela, (verde), ((20, (Altura // 2) - 10), (20, (Altura // 2) + 10), (40, (Altura // 2))))

pygame.draw.rect(tela, (azul), (Largura - 30, (Altura // 2) - 5, 25, 10), 0)
pygame.draw.polygon(tela, (azul), ((Largura - 23, (Altura // 2) - 10), (Largura - 23, (Altura // 2) + 10), (Largura - 43, (Altura // 2))))

pygame.draw.rect(tela, (vermelho), ((Largura // 2) - 3, Altura - 30, 10, 25), 0)
pygame.draw.polygon(tela, (vermelho), (((Largura // 2) - 10, (Altura - 20)), ((Largura // 2) + 1, Altura - 40), ((Largura // 2) + 13, (Altura - 20))))

pygame.draw.rect(tela, (amarelo), ((Largura // 2) - 4, 7, 10, 25), 0)
pygame.draw.polygon(tela, (amarelo), (((Largura // 2) - 10, 20), (Largura // 2, 44), ((Largura // 2) + 13, 20)))


# fazendo os circulos (players)
pygame.draw.circle(tela, (verde), (bolinha1, bolinha1), 20, 0)
pygame.draw.circle(tela, (preto), (bolinha1, bolinha1), 20, 3)
pygame.draw.circle(tela, (verde), (bolinha2, bolinha1), 20, 0)
pygame.draw.circle(tela, (preto), (bolinha2, bolinha1), 20, 3)
pygame.draw.circle(tela, (verde), (bolinha1, bolinha2), 20, 0)
pygame.draw.circle(tela, (preto), (bolinha1, bolinha2), 20, 3)
pygame.draw.circle(tela, (verde), (bolinha2, bolinha2), 20, 0)
pygame.draw.circle(tela, (preto), (bolinha2, bolinha2), 20, 3)

pygame.draw.circle(tela, (amarelo), (bolinha3, bolinha1), 20, 0)
pygame.draw.circle(tela, (preto), (bolinha3, bolinha1), 20, 3)
pygame.draw.circle(tela, (amarelo), (bolinha4, bolinha1), 20, 0)
pygame.draw.circle(tela, (preto), (bolinha4, bolinha1), 20, 3)
pygame.draw.circle(tela, (amarelo), (bolinha3, bolinha2), 20, 0)
pygame.draw.circle(tela, (preto), (bolinha3, bolinha2), 20, 3)
pygame.draw.circle(tela, (amarelo), (bolinha4, bolinha2), 20, 0)
pygame.draw.circle(tela, (preto), (bolinha4, bolinha2), 20, 3)

pygame.draw.circle(tela, (vermelho), (bolinha1, bolinha3), 20, 0)
pygame.draw.circle(tela, (preto), (bolinha1, bolinha3), 20, 3)
pygame.draw.circle(tela, (vermelho), (bolinha2, bolinha3), 20, 0)
pygame.draw.circle(tela, (preto), (bolinha2, bolinha3), 20, 3)
pygame.draw.circle(tela, (vermelho), (bolinha1, bolinha4), 20, 0)
pygame.draw.circle(tela, (preto), (bolinha1, bolinha4), 20, 3)
pygame.draw.circle(tela, (vermelho), (bolinha2, bolinha4), 20, 0)
pygame.draw.circle(tela, (preto), (bolinha2, bolinha4), 20, 3)

pygame.draw.circle(tela, (azul), (bolinha3, bolinha3), 20, 0)
pygame.draw.circle(tela, (preto), (bolinha3, bolinha3), 20, 3)
pygame.draw.circle(tela, (azul), (bolinha4, bolinha3), 20, 0)
pygame.draw.circle(tela, (preto), (bolinha4, bolinha3), 20, 3)
pygame.draw.circle(tela, (azul), (bolinha3, bolinha4), 20, 0)
pygame.draw.circle(tela, (preto), (bolinha3, bolinha4), 20, 3)
pygame.draw.circle(tela, (azul), (bolinha4, bolinha4), 20, 0)
pygame.draw.circle(tela, (preto), (bolinha4, bolinha4), 20, 3)

#escrevendo o título
pygame.display.set_caption("LUDO")

rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    pygame.display.update()

pygame.quit()


