# JOGNA1 –Entrega N1.C– Gabriel Rodrigues, Vanessa Byork, Jonatas Cirino e Lucas Freitas

# Explicando o que eu fiz aqui: de inicio eu só montei o mapa do jogo, não dava pra
# interagir nem algo do genero, porém eu vi que tinha que fazer alguma animação ou coisa do tipo, então eu
# decidi fazer com que quando você clicar o "WASD" o personagem se movesse, isso só depois de clicar "ESPAÇO"
# pro jogo começar. Da pra comepletar e fazer isso para cada peça, porém apenas fiz pro verde
# (por preguiça... eu sei). Então você meio que tem que jogar o dado na vida real e mover justamente.

import pygame
pygame.init()

Largura = int(input("Digite o tamanho da Largura do tabuleiro: "))
Altura = int(input("Digite o tamanho da Altura do tabuleiro: "))


tela = pygame.display.set_mode((Largura, Altura))

# fazendo os valores
branco = (255, 255, 255)
preto = (0, 0, 0)
verde = (0, 255, 0)
amarelo = (255, 255, 0)
vermelho = (255, 0, 0)
azul = (0, 0, 255)
cinza = (128, 128, 128)

#50
porcentagem1 = (6.666666666666667 / 100) * Largura
porcentagem2 = (6.666666666666667 / 100) * Altura
#300
porcentagem3 = (40 / 100) * Largura
porcentagem4 = (40 / 100) * Altura
#450
porcentagem5 = (60 / 100) * Largura
porcentagem6 = (60 / 100) * Altura
#500
porcentagem7 = (66.666666666666666666666666666667 / 100) * Largura
porcentagem8 = (66.666666666666666666666666666667 / 100) * Altura
#200
porcentagem9 = (26.6666666667 / 100) * Largura
porcentagem10 = (26.6666666667 / 100) * Altura
#5
porcentagem11 = (0.666666666667 / 100) * Largura
porcentagem12 = (0.666666666667 / 100) * Altura
#10
porcentagem13 = (1.333333333333 / 100) * Largura
porcentagem14 = (1.333333333333 / 100) * Altura
#25
porcentagem15 = (3.33333333333 / 100) * Largura
porcentagem16 = (3.33333333333 / 100) * Altura
#20
porcentagem17 = (2.66666666667 / 100) * Largura
porcentagem18 = (2.66666666667 / 100) * Altura
#40
porcentagem19 = (5.33333333333 / 100) * Largura
porcentagem20 = (5.33333333333 / 100) * Altura
#4
porcentagem21 = (0.533333333333 / 100) * Largura
porcentagem22 = (0.533333333333 / 100) * Altura
#30
porcentagem23 = (4 / 100) * Largura
porcentagem24 = (4 / 100) * Altura
#23
porcentagem25 = (3.06666666667 / 100) * Largura
porcentagem26 = (3.06666666667 / 100) * Altura
#43
porcentagem27 = (5.73333333333 / 100) * Largura
porcentagem28 = (5.73333333333 / 100) * Altura
#6
porcentagem29 = (0.8 / 100) * Largura
porcentagem30 = (0.8 / 100) * Altura
#7
porcentagem31 = (0.933333333333 / 100) * Largura
porcentagem32 = (0.933333333333 / 100) * Altura
#3
porcentagem33 = (0.4 / 100) * Largura
porcentagem34 = (0.4 / 100) * Altura
#1
porcentagem35 = (0.1333333333333 / 100) * Largura
porcentagem36 = (0.1333333333333 / 100) * Altura
#13
porcentagem37 = (1.73333333333 / 100) * Largura
porcentagem38 = (1.73333333333 / 100) * Altura
#44
porcentagem39 = (5.86666666667 / 100) * Largura
porcentagem40 = (5.86666666667 / 100) * Altura
#74
porcentagem41 = (9.86666666667 / 100) * Largura
porcentagem42 = (9.86666666667 / 100) * Altura
#150
porcentagem43 = (20 / 100) * Largura
porcentagem44 = (20 / 100) * Altura
#375
porcentagem45 = (50 / 100) * Largura
porcentagem46 = (50 / 100) * Altura
#350
porcentagem47 = (46.6666666667 / 100) * Largura
porcentagem48 = (46.6666666667 / 100) * Altura
#250
porcentagem49 = (33.3333333333 / 100) * Largura
porcentagem50 = (33.3333333333 / 100) * Altura
#251
porcentagem51 = (33.46666666666 / 100) * Largura
porcentagem52 = (33.46666666666 / 100) * Altura
#400
porcentagem53 = (53.3333333333 / 100) * Largura
porcentagem54 = (53.3333333333 / 100) * Altura
#650
porcentagem55 = (86.6666666667 / 100) * Largura
porcentagem56 = (86.6666666667 / 100) * Altura
#100
porcentagem57 = (13.33333333333 / 100) * Largura
porcentagem58 = (13.33333333333 / 100) * Altura
#52
porcentagem59 = (6.93333333333 / 100) * Largura
porcentagem60 = (6.93333333333 / 100) * Altura
#252
porcentagem61 = (33.6 / 100) * Largura
porcentagem62 = (33.6 / 100) * Altura
#53
porcentagem63 = (7.06666666667 / 100) * Largura
porcentagem64 = (7.06666666667 / 100) * Altura
#102
porcentagem65 = (13.6 / 100) * Largura
porcentagem66 = (13.6 / 100) * Altura

caminho_verde = (porcentagem1, porcentagem10, porcentagem2, porcentagem10)
caminho_verde1 = (porcentagem1, porcentagem48, porcentagem51, porcentagem2)
caminho_amarelo = (porcentagem47, porcentagem2, porcentagem1, porcentagem62)
caminho_amarelo1 = (porcentagem47, porcentagem2, porcentagem49, porcentagem2)
caminho_vermelho = (porcentagem47, porcentagem54, porcentagem1, porcentagem62)
caminho_vermelho1 = (porcentagem3, porcentagem56, porcentagem65, porcentagem2)
caminho_azul = (porcentagem55, porcentagem54, porcentagem1, porcentagem64)
caminho_azul1 = (porcentagem5, porcentagem48, porcentagem61, porcentagem2)

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
    # fazendo o fundo (funciona em qualquer escala da tela)
    pygame.draw.rect(tela, (branco), (0, 0, Largura, Altura), 0)

    # fazendo o caminho de todas as cores (funciona em qualquer escala da tela)
    pygame.draw.rect(tela, (verde), (caminho_verde), 0)
    pygame.draw.rect(tela, (verde), (caminho_verde1), 0)

    pygame.draw.rect(tela, (amarelo), (caminho_amarelo), 0)
    pygame.draw.rect(tela, (amarelo), (caminho_amarelo1), 0)

    pygame.draw.rect(tela, (vermelho), (caminho_vermelho), 0)
    pygame.draw.rect(tela, (vermelho), (caminho_vermelho1), 0)

    pygame.draw.rect(tela, (azul), (caminho_azul), 0)
    pygame.draw.rect(tela, (azul), (caminho_azul1), 0)

    # fazendo as linhas (funciona em qualquer escala da tela)
    linha_x = (Largura - Largura) + porcentagem1
    for i in range(14):
        pygame.draw.line(tela, (cinza), (linha_x, Altura), (linha_x, 0), 2)
        linha_x += porcentagem1

    linha_y = (Altura - Altura) + porcentagem2
    for i in range(14):
        pygame.draw.line(tela, (cinza), (Largura, linha_y), (0, linha_y), 2)
        linha_y += porcentagem2

    # fazendo os quadrados grandes (funciona em qualquer escala da tela)
    pygame.draw.rect(tela, (verde), (0, 0, porcentagem3, porcentagem4), 0)
    pygame.draw.rect(tela, (amarelo), (porcentagem5, 0, porcentagem3, porcentagem4), 0)
    pygame.draw.rect(tela, (vermelho), (0, porcentagem6, porcentagem3, porcentagem4), 0)
    pygame.draw.rect(tela, (azul), (porcentagem5, porcentagem6, porcentagem3, porcentagem4), 0)

    # fazendo os quadrados pequenos (funciona em qualquer escala da tela)
    pygame.draw.rect(tela, (branco), (porcentagem1, porcentagem2, porcentagem9, porcentagem10), 0)
    pygame.draw.rect(tela, (branco), (porcentagem7, porcentagem2, porcentagem9, porcentagem10), 0)
    pygame.draw.rect(tela, (branco), (porcentagem1, porcentagem8, porcentagem9, porcentagem10), 0)
    pygame.draw.rect(tela, (branco), (porcentagem7, porcentagem8, porcentagem9, porcentagem10), 0)

    # fazendo o quadrado no meio (junto com os triangulos) (funciona em qualquer escala da tela)
    pygame.draw.rect(tela, (branco), ((Largura // 2) - porcentagem41, (Altura // 2) - porcentagem42, porcentagem43, porcentagem44), 0)
    pygame.draw.polygon(tela, (verde), ((porcentagem3, porcentagem4), (porcentagem45, porcentagem46), (porcentagem3, porcentagem6)))
    pygame.draw.polygon(tela, (vermelho), ((porcentagem5, porcentagem6), (porcentagem45, porcentagem46), (porcentagem3, porcentagem6)))
    pygame.draw.polygon(tela, (azul), ((porcentagem5, porcentagem6), (porcentagem45, porcentagem46), (porcentagem5, porcentagem4)))
    pygame.draw.polygon(tela, (amarelo), ((porcentagem3, porcentagem4), (porcentagem45, porcentagem46), (porcentagem5, porcentagem4)))

    # fazendo as setinhas (funciona em qualquer escala da tela)
    pygame.draw.rect(tela, (verde), (porcentagem21, (Altura // 2) - porcentagem22, porcentagem15, porcentagem14), 0)
    pygame.draw.polygon(tela, (verde), ((porcentagem17, (Altura // 2) - porcentagem14), (porcentagem17, (Altura // 2) + porcentagem14), (porcentagem19, (Altura // 2))))

    pygame.draw.rect(tela, (azul), (Largura - porcentagem23, (Altura // 2) - porcentagem22, porcentagem15, porcentagem14), 0)
    pygame.draw.polygon(tela, (azul), ((Largura - porcentagem25, (Altura // 2) - porcentagem14), (Largura - porcentagem25, (Altura // 2) + porcentagem14), (Largura - porcentagem28, (Altura // 2))))

    pygame.draw.rect(tela, (vermelho), ((Largura // 2) - porcentagem33, Altura - porcentagem24, porcentagem13, porcentagem16), 0)
    pygame.draw.polygon(tela, (vermelho), (((Largura // 2) - porcentagem13, (Altura - porcentagem18)), ((Largura // 2) + porcentagem35, Altura - porcentagem20), ((Largura // 2) + porcentagem38, (Altura - porcentagem18))))

    pygame.draw.rect(tela, (amarelo), ((Largura // 2) - porcentagem21, porcentagem32, porcentagem13, porcentagem16), 0)
    pygame.draw.polygon(tela, (amarelo), (((Largura // 2) - porcentagem13, porcentagem18), (Largura // 2, porcentagem40), ((Largura // 2) + porcentagem37, porcentagem18)))


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


