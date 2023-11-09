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

#posições
personagem_x = 290
personagem_y = 220

#variáveis pros bagulho funfa
parou_cima = False

cima = False
baixo = False
esquerda = False
direita = False

olhando = 0

liberado = True
aumentar = False

pode_andar = True

Aumento = 0

tempo_1 = pygame.time.get_ticks()

BarraVermelha = 15, 10, 250, 50
BarraVerde = 15, 10, Aumento, 50

#colocando o FPS
clock = pygame.time.Clock()
fps = 60

#escrevendo o título
pygame.display.set_caption("Jogo Corrida")

#definindo o lugar
def lugar():
    #fazendo as variaveis e colocando algumas pra agir globalmente
    global parou_cima, cima, esquerda, direita, BarraVermelha, BarraVerde, hitbox_jogador
    keys = pygame.key.get_pressed()

    #fazendo o fundo
    tela.blit(fundo, (0, 0))
    
    #fazendo a hitbox
    hitbox_cima = pygame.Rect(0, 0, 640, 220)
    
    hitbox_jogador = pygame.Rect((personagem_x) - 3, (personagem_y) + 50, 70, 20)
    pygame.draw.rect(tela, (255, 0, 0), hitbox_jogador)

    #fazendo o sprite desenhar
    if baixo == True and cima == False and esquerda == False and direita == False or olhando == 0:
        tela.blit(personagem_baixo, (personagem_x, personagem_y))

    if cima == True and esquerda == False and direita == False and baixo == False or olhando == 3:
        tela.blit(personagem_cima, (personagem_x, personagem_y))

    if esquerda == True and direita == False and baixo == False and cima == False or olhando == 1:
        tela.blit(personagem_esquerda, (personagem_x, personagem_y))

    if direita == True and baixo == False and cima == False or olhando == 2:
        tela.blit(personagem_direita, (personagem_x, personagem_y))

    #fazendo a colisão
    if hitbox_jogador.colliderect(hitbox_cima):
        parou_cima = True
    else:
        parou_cima = False

    pygame.draw.rect(tela, (255, 0, 0), (BarraVermelha), 0)
    pygame.draw.rect(tela, (0, 255, 0), (BarraVerde), 0)

while True:
    #fazendo o jogo funcionar e desligar quando clicar no X
    clock.tick(fps) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #fazendo as salas
    lugar()
    

    #definindo as teclas
    keys = pygame.key.get_pressed()

    #teclas para andar
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
        tempo_1 = pygame.time.get_ticks()
        olhando = 3

    if keys[pygame.K_x] and not keys[pygame.K_z] and liberado == False:
        aumentar = True
        liberado = True
        tempo_1 = pygame.time.get_ticks()
        olhando = 3

    #fazendo o aumento da velocidade
    if aumentar == True:
        if parou_cima == False:
            personagem_y -= Aumento
        if Aumento <= 250:
            Aumento += 1
            BarraVerde = 15, 10, Aumento, 50
        tempo_1 = pygame.time.get_ticks()
        aumentar = False
        pode_andar = False

    if (not keys[pygame.K_z] or (not keys[pygame.K_x])) and pygame.time.get_ticks() > tempo_1 + 1000:
        if Aumento > 0:
            Aumento -= 1
        BarraVerde = 15, 10, Aumento, 50

    if Aumento == 0:
        pode_andar = True

    pygame.display.update()
    
