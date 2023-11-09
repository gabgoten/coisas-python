#FAZER COM QUE O SPRITE DELA GIRE HORIZONTALMENTE QUANDO CLICAR ESQUERDA OU DIREITA ENQUANTO CORRE
#FAZER O SPRITE DELA CONTINUAR ANDANDO MESMO QUANDO VOCÊ NÃO ESTIVER CLICANDO (PORÉM ISSO ATÉ O AUMENTAR SER 0)

import pygame
import sys
pygame.init()

#tamanhos
Largura = 640
Altura = 480
tela = pygame.display.set_mode((Largura, Altura))

#importando as imagens
fundo = pygame.image.load("fundo.png")
fundo = pygame.transform.scale(fundo, (Largura, Altura))

personagem_baixo = pygame.image.load("personagem.png")
personagem_cima = pygame.image.load("personagem_cima.png")
personagem_esquerda = pygame.image.load("personagem_esquerda.png")
personagem_direita = pygame.image.load("personagem_direita.png")

correr_esquerda = pygame.image.load("correr_esquerda.png")
correr_direita = pygame.image.load("correr_direita.png")

#posições
personagem_x = 290
personagem_y = 220

X = 0
Y = 0

#variáveis pros bagulho funfa
parou_cima = False
parou_cima1 = False
parou_cima2 = False
parou_cima3 = False

cima = False
baixo = False
esquerda = False
direita = False

olhando = 0

liberado = True
aumentar = False

pode_andar = True

Aumento = 0
Aumento2 = 0
Aumento_Contrario = 175
Aumento_ContrarioX = 15

tempo_1 = pygame.time.get_ticks()
tempo_2 = pygame.time.get_ticks()
tempo_3 = pygame.time.get_ticks()

BarraVermelha = 15, 10, 175, 50
BarraVerde = 15, 10, Aumento, 50

BarraVermelha2 = 15, 75, 175, 50
BarraAzul2 = 15, 75, Aumento_Contrario, 50

#colocando o FPS
clock = pygame.time.Clock()
fps = 60

#escrevendo o título
pygame.display.set_caption("Jogo Corrida")    

while True:
    #fazendo o jogo funcionar e desligar quando clicar no X
    clock.tick(fps) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #fazendo o fundo
    tela.blit(fundo, (X, Y))
    tela.blit(fundo, (X, Y - 480))
    if Y > 480:
        Y = 0
    Y += Aumento / 10
    
    #fazendo a barra de velocidade
    pygame.draw.rect(tela, (255, 0, 0), (BarraVermelha), 0)
    pygame.draw.rect(tela, (0, 255, 0), (BarraVerde), 0)

    #fazendo a barra de stamina
    pygame.draw.rect(tela, (255, 0, 0), (BarraVermelha2), 0)
    pygame.draw.rect(tela, (50, 50, 255), (BarraAzul2), 0)

    #fazendo a hitbox
    hitbox_cima = pygame.Rect(0, 0, 640, 280)

    hitbox_cima1 = pygame.Rect(0, 0, 640, 240)

    hitbox_cima2 = pygame.Rect(0, 0, 640, 190)

    hitbox_cima3 = pygame.Rect(0, 0, 640, 120)
    
    hitbox_jogador = pygame.Rect((personagem_x) - 3, (personagem_y) + 50, 70, 20)

    #fazendo o sprite desenhar
    if baixo == True and cima == False and esquerda == False and direita == False or olhando == 0:
        tela.blit(personagem_baixo, (personagem_x, personagem_y))

    if cima == True and esquerda == False and direita == False and baixo == False or olhando == 3:
        tela.blit(personagem_cima, (personagem_x, personagem_y))
    
    if esquerda == True and direita == False and baixo == False and cima == False or olhando == 1:
        tela.blit(personagem_esquerda, (personagem_x, personagem_y))

    if direita == True and baixo == False and cima == False or olhando == 2:
        tela.blit(personagem_direita, (personagem_x, personagem_y))

    if olhando == 4:
        if liberado == True:
                tela.blit(correr_esquerda, (personagem_x, personagem_y))

        if liberado == False:
            tela.blit(correr_direita, (personagem_x, personagem_y))

        if Aumento == 0:
            olhando = 3

    #fazendo a colisão
    if hitbox_jogador.colliderect(hitbox_cima):
        parou_cima = True
    else:
        parou_cima = False

    if hitbox_jogador.colliderect(hitbox_cima1):
        parou_cima1 = True
    else:
        parou_cima1 = False

    if hitbox_jogador.colliderect(hitbox_cima2):
        parou_cima2 = True
    else:
        parou_cima2 = False

    if hitbox_jogador.colliderect(hitbox_cima3):
        parou_cima3 = True
    else:
        parou_cima3 = False

    #definindo as teclas
    keys = pygame.key.get_pressed()

    #teclas para andar
    if pode_andar == False:
        if keys[pygame.K_LEFT]:
            personagem_x -= 1

        if keys[pygame.K_RIGHT]:
            personagem_x += 1

    if pode_andar == True:
        if keys[pygame.K_LEFT]:
            personagem_x -= 1
        if keys[pygame.K_LEFT]:
            esquerda = True
            olhando = 1
        if not keys[pygame.K_LEFT]:
            esquerda = False

        if keys[pygame.K_RIGHT]:
            personagem_x += 1
        if keys[pygame.K_RIGHT]:
            direita = True
            olhando = 2
        if not keys[pygame.K_RIGHT]:
            direita = False

        if keys[pygame.K_UP] and parou_cima == False:
            personagem_y -= 1
        if keys[pygame.K_UP]:
            cima = True
            olhando = 3
        if not keys[pygame.K_UP]:
            cima = False

        if keys[pygame.K_DOWN]:
            personagem_y += 1
        if keys[pygame.K_DOWN]:
            baixo = True
            olhando = 0
        if not keys[pygame.K_DOWN]:
            baixo = False

    #fazendo o personagem correr
    if keys[pygame.K_z] and not keys[pygame.K_x] and liberado == True:
        aumentar = True
        liberado = False
        tempo_2 = pygame.time.get_ticks()
        olhando = 4

    if keys[pygame.K_x] and not keys[pygame.K_z] and liberado == False:
        aumentar = True
        liberado = True
        tempo_3 = pygame.time.get_ticks()
        olhando = 4

    #fazendo o aumento da velocidade
    if aumentar == True:
        if parou_cima == False:
            personagem_y -= Aumento2//2

        if parou_cima1 == False and Aumento > 50:
            personagem_y -= Aumento2//2

        if parou_cima2 == False and Aumento > 100:
            personagem_y -= Aumento2//2

        if parou_cima3 == False and Aumento > 150:
            personagem_y -= Aumento2//2
        
        if Aumento <= 175:
            Aumento += 1
            BarraVerde = 15, 10, Aumento, 50
        if Aumento <= 20:
            Aumento2 += 0.4
        Aumento_Contrario -= 0.2
        BarraAzul2 = 15, 75, Aumento_Contrario, 50
        tempo_1 = pygame.time.get_ticks()      
        aumentar = False
        pode_andar = False
        cima = False
        baixo = False
        esquerda = False
        direita = False

    #fazendo a diminuição da velocidade
    if (not keys[pygame.K_z] or (not keys[pygame.K_x])) and pygame.time.get_ticks() > tempo_1 + 500 and cima == False:
        if Aumento > 0:
            Aumento -= 1
        if Aumento > 0 and Aumento <= 20:
            Aumento2 -= 0.4
        if Aumento > 0 and personagem_y < 230:
            personagem_y += 2
        BarraVerde = 15, 10, Aumento, 50

    if Aumento == 0:
        pode_andar = True

    #fazendo a barra de stamina regenerar
    if Aumento_Contrario < 176 and Aumento == 0:
        Aumento_Contrario += 0.05
        BarraAzul2 = 15, 75, Aumento_Contrario, 50
    if Aumento_Contrario == 0:
        Cansou = True

    pygame.display.update()
    
