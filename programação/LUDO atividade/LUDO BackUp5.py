# JOGNA1 –Entrega N1.C– Gabriel Rodrigues, Vanessa Byork, Jonatas Cirino e Lucas Freitas

# Explicando o que eu fiz aqui: de inicio eu só montei o mapa do jogo, não dava pra
# interagir nem algo do genero, porém eu vi que tinha que fazer alguma animação ou coisa do tipo, então eu
# decidi fazer com que quando você clicar o "WASD" o personagem se movesse, isso só depois de clicar "ESPAÇO"
# pro jogo começar. Da pra comepletar e fazer isso para cada peça, porém apenas fiz pro verde
# (por preguiça... eu sei). Então você meio que tem que jogar o dado na vida real e mover justamente.

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

bolinha1_x = 100
bolinha1_y = 100

bolinha2 = 200
bolinha3 = 550
bolinha4 = 650

começar1 = False
okay = False
okay2 = False
okay3 = False
okay4 = False

# o programa já estava pronto sem esse "def", porém eu não estava conseguindo fazer os players
# se mexerem, então eu tive que fazer isso para conseguir fazer o que eu queria com os players 
def reiniciar():
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
    pygame.draw.circle(tela, (verde), (bolinha1_x, bolinha1_y), 20, 0)
    pygame.draw.circle(tela, (preto), (bolinha1_x, bolinha1_y), 20, 3)
    pygame.draw.circle(tela, (verde), (200, 100), 20, 0)
    pygame.draw.circle(tela, (preto), (200, 100), 20, 3)
    pygame.draw.circle(tela, (verde), (100, 200), 20, 0)
    pygame.draw.circle(tela, (preto), (100, 200), 20, 3)
    pygame.draw.circle(tela, (verde), (200, 200), 20, 0)
    pygame.draw.circle(tela, (preto), (200, 200), 20, 3)

    pygame.draw.circle(tela, (amarelo), (550, 100), 20, 0)
    pygame.draw.circle(tela, (preto), (550, 100), 20, 3)
    pygame.draw.circle(tela, (amarelo), (650, 100), 20, 0)
    pygame.draw.circle(tela, (preto), (650, 100), 20, 3)
    pygame.draw.circle(tela, (amarelo), (550, 200), 20, 0)
    pygame.draw.circle(tela, (preto), (550, 200), 20, 3)
    pygame.draw.circle(tela, (amarelo), (650, 200), 20, 0)
    pygame.draw.circle(tela, (preto), (650, 200), 20, 3)

    pygame.draw.circle(tela, (vermelho), (100, 550), 20, 0)
    pygame.draw.circle(tela, (preto), (100, 550), 20, 3)
    pygame.draw.circle(tela, (vermelho), (200, 550), 20, 0)
    pygame.draw.circle(tela, (preto), (200, 550), 20, 3)
    pygame.draw.circle(tela, (vermelho), (100, 650), 20, 0)
    pygame.draw.circle(tela, (preto), (100, 650), 20, 3)
    pygame.draw.circle(tela, (vermelho), (200, 650), 20, 0)
    pygame.draw.circle(tela, (preto), (200, 650), 20, 3)

    pygame.draw.circle(tela, (azul), (550, 550), 20, 0)
    pygame.draw.circle(tela, (preto), (550, 550), 20, 3)
    pygame.draw.circle(tela, (azul), (650, 550), 20, 0)
    pygame.draw.circle(tela, (preto), (650, 550), 20, 3)
    pygame.draw.circle(tela, (azul), (550, 650), 20, 0)
    pygame.draw.circle(tela, (preto), (550, 650), 20, 3)
    pygame.draw.circle(tela, (azul), (650, 650), 20, 0)
    pygame.draw.circle(tela, (preto), (650, 650), 20, 3)

reiniciar()

#escrevendo o título
pygame.display.set_caption("LUDO")

rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        bolinha1_x = 75
        bolinha1_y = 325
        começar1 = True
        reiniciar()

    if keys[pygame.K_a] and okay == False and começar1 == True:
        bolinha1_x -= 50
        okay = True
        reiniciar()

    if keys[pygame.K_d] and okay2 == False and começar1 == True:
        bolinha1_x += 50
        okay2 = True
        reiniciar()

    if keys[pygame.K_s] and okay3 == False and começar1 == True:
        bolinha1_y += 50
        okay3 = True
        reiniciar()

    if keys[pygame.K_w] and okay4 == False and começar1 == True:
        bolinha1_y -= 50
        okay4 = True
        reiniciar()

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_a:
            okay = False
        if event.key == pygame.K_d:
            okay2 = False
        if event.key == pygame.K_s:
            okay3 = False
        if event.key == pygame.K_w:
            okay4 = False

    pygame.display.update()

pygame.quit()


