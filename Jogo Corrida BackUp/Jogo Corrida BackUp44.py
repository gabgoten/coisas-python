#FAZER OS 2 FINAIS MAIS BONITINHOS

import pygame
import random
import sys
pygame.init()

#tamanhos
Largura = 640
Altura = 480
tela = pygame.display.set_mode((Largura, Altura))

#importando as imagens
fundo = pygame.image.load("fundo.png")
fundo = pygame.transform.scale(fundo, (Largura, Altura))

saguão = pygame.image.load("saguão.png")

fundo_caminho_virando = pygame.image.load("fundo_caminho_virando.png")
fundo_caminho_virando = pygame.transform.scale(fundo_caminho_virando, (Largura, Altura))

fundo_caminho_virando2 = pygame.image.load("fundo_caminho_virando2.png")
fundo_caminho_virando2 = pygame.transform.scale(fundo_caminho_virando2, (Largura, Altura + 5))

fundo_caminho_lado = pygame.image.load("fundo_caminho_lado.png")
fundo_caminho_lado = pygame.transform.scale(fundo_caminho_lado, (Largura, Altura))

personagem_baixo = pygame.image.load("personagem.png")
personagem_cima = pygame.image.load("personagem_cima.png")
personagem_esquerda = pygame.image.load("personagem_esquerda.png")
personagem_direita = pygame.image.load("personagem_direita.png")

npc_cima = pygame.image.load("npc_cima.png")
npc_cima2 = pygame.image.load("npc_cima2.png")
npc_cima3 = pygame.image.load("npc_cima3.png")

npc_correr_esquerda = pygame.image.load("npc_correr_esquerda.png")
npc_correr_direita = pygame.image.load("npc_correr_direita.png")
npc_correr_esquerda2 = pygame.image.load("npc_correr_esquerda2.png")
npc_correr_direita2 = pygame.image.load("npc_correr_direita2.png")
npc_correr_esquerda3 = pygame.image.load("npc_correr_esquerda3.png")
npc_correr_direita3 = pygame.image.load("npc_correr_direita3.png")

espaço = pygame.image.load("barra.png")
espaço = pygame.transform.scale(espaço, (150, 150))

balão = pygame.image.load("balão.png")
balão = pygame.transform.scale(balão, (250, 180))

correr_esquerda = pygame.image.load("correr_esquerda.png")
correr_direita = pygame.image.load("correr_direita.png")

pedra = pygame.image.load("pedra.png")

fundo_menu = pygame.image.load("menu.jpg")
fundo_menu = pygame.transform.scale(fundo_menu, (Largura, Altura))

#posições
personagem_x = 290
personagem_y = 320

npc_x = 200
npc_y = 300
npc_x2 = 300
npc_y2 = 300
npc_x3 = 400
npc_y3 = 300

X = 0
Y = 0
Y2= 0
Y3 = 0
Y4 = 0
Y5 = 0

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
liberado2 = True
aumentar = False

pode_andar = True

Cansou = False

Aumento = 0
Aumento2 = 0
Aumento_Contrario = 175

tempo_1 = pygame.time.get_ticks()
tempo_2 = pygame.time.get_ticks()
tempo_3 = pygame.time.get_ticks()
tempo_4 = 0
tempo_5 = 0

inicio_jogo = 0
final_jogo = 10800
Ganhar = 0

BarraVermelha = 15, 10, 175, 50
BarraVerde = 15, 10, Aumento, 50

BarraVermelha2 = 15, 75, 175, 50
BarraAzul2 = 15, 75, Aumento_Contrario, 50

tempo_diminuir1 = 200
tempo_diminuir2 = 200

fonte = pygame.font.Font(None, 60)
fonte2 = pygame.font.Font(None, 30)
fonte3 = pygame.font.Font(None, 20)
fonte4 = pygame.font.Font(None, 25)

pular = 0

pulo = False
pulo2 = False

aleatorio_pedra = 0
aleatorio_pedraX = 0
aleatorio_pedra_tamanhoL = 0
aleatorio_pedra_tamanhoR = 0
pedra_hitbox_largura = 0

hitbox_pedra = pygame.Rect(aleatorio_pedraX, Y2 - 45, 30, 10)
tomou_hit = False
mostrar_pedra = True
mostrar_relogio = True
relogio_ativado = False
tempo_segundos = final_jogo

pronto = True

continuar_texto = False
continuar_texto2 = False
continuar_texto3 = False
tempo_texto = 0
tempo_texto2 = 0
tempo_texto3 = 0
parar_texto = False
parar_texto2 = False

posição_momentox = 0
posição_momentoy = 0

tempo_npc1 = 330
liberado_npc1 = False
tempo_npc2 = 315
liberado_npc2 = False
tempo_npc3 = 345
liberado_npc3 = False

menu = True
saguão_menu = False

saguão_x = -200
saguão_y = -500

#colocando o FPS
clock = pygame.time.Clock()
fps = 60

#escrevendo o título
pygame.display.set_caption("Jogo Corrida")    

#definindo o resetar_jogo (trazendo tudo de volta resetando tudo, qualquer variável nova é bom adicionar aqui)
def resetar_jogo():
    global personagem_x, personagem_y, tempo_npc1, tempo_npc2, tempo_npc3, liberado_npc1, liberado_npc2, liberado_npc3, menu, saguão_menu, posição_momentox, posição_momentoy, tempo_texto, continuar_texto, parar_texto2, continuar_texto2, continuar_texto3, tempo_texto2, tempo_texto3, parar_texto, npc_x, npc_y, npc_x2, npc_y2, npc_x3, npc_y3, X, Y, Y3, Y4, Y5, parou_cima, parou_cima1, parou_cima2, parou_cima3, cima, baixo, esquerda, direita, olhando, liberado, aumentar, pode_andar, Cansou, Aumento, Aumento2, Aumento_Contrario, inicio_jogo, final_jogo, BarraVermelha, BarraVerde, BarraVermelha2, BarraAzul2, tempo_diminuir1, tempo_diminuir2, Ganhar, Pular, Pulo, Pulo2, aleatorio_pedra, aleatorio_pedraX, Y2, hitbox_pedra, tomou_hit, mostrar_pedra, aleatorio_pedra_tamanhoL, aleatorio_pedra_tamanhoR, pedra_hitbox_largura, liberado2, pronto, mostrar_relogio, relogio_ativado, tempo_segundos
    personagem_x = 290
    personagem_y = 320
    X = 0
    Y = 0
    Y2 = 0
    Y3 = 0
    Y4 = 0
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
    liberado2 = True
    aumentar = False
    pode_andar = True
    Cansou = False
    Aumento = 0
    Aumento2 = 0
    Aumento_Contrario = 175
    inicio_jogo = 0
    final_jogo = 10800
    BarraVermelha = 15, 10, 175, 50
    BarraVerde = 15, 10, Aumento, 50
    BarraVermelha2 = 15, 75, 175, 50
    BarraAzul2 = 15, 75, Aumento_Contrario, 50
    tempo_diminuir1 = 200
    tempo_diminuir2 = 200
    Ganhar = 0
    pular = 0
    pulo = False
    pulo2 = False
    aleatorio_pedra = 0
    aleatorio_pedraX = 0
    hitbox_pedra = pygame.Rect(aleatorio_pedraX, Y2 - 45, 30, 10)
    tomou_hit = False
    mostrar_pedra = True
    aleatorio_pedra_tamanhoL = 0
    aleatorio_pedra_tamanhoR = 0
    pedra_hitbox_largura = 0
    pronto = True
    mostrar_relogio = True
    relogio_ativado = False
    tempo_segundos = final_jogo
    npc_x = 200
    npc_y = 300
    npc_x2 = 300
    npc_y2 = 300
    npc_x3 = 400
    npc_y3 = 300
    continuar_texto = False
    continuar_texto2 = False
    tempo_texto = 0
    Y5 = 0
    tempo_texto2 = 0
    parar_texto = False
    continuar_texto3 = False
    tempo_texto3 = 0
    parar_texto2 = False
    posição_momentox = 0
    posição_momentoy = 0
    tempo_npc1 = 330
    liberado_npc1 = False
    tempo_npc2 = 315
    liberado_npc2 = False
    tempo_npc3 = 345
    liberado_npc3 = False
    menu = True
    saguão_menu = False

while True:
    #fazendo o jogo funcionar e desligar quando clicar no X
    clock.tick(fps) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #fazendo o menu do jogo
    while menu == True:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        teste = pygame.Rect((235, 300), (150, 30))
        pygame.draw.rect(tela, (255, 0, 0), teste)
        tela.blit(fundo_menu, (0, 0))
        pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            posicao_mouse = pygame.mouse.get_pos()
            if teste.collidepoint(posicao_mouse):
                resetar_jogo()
                saguão_menu = True
                personagem_x = Largura/2 - 30
                personagem_y = Altura/2 - 30
                menu = False

    #fazendo o saguão do jogo
    while saguão_menu == True:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        tela.blit(saguão, (saguão_x, saguão_y))
        tela.blit(personagem_esquerda, (personagem_x, personagem_y))
        if keys[pygame.K_LEFT] and saguão_x <= 0 and personagem_x == Largura/2 - 30:
            saguão_x += 1
        if keys[pygame.K_RIGHT] and saguão_x >= -355 and personagem_x == Largura/2 - 30:
            saguão_x -= 1
        if keys[pygame.K_UP] and saguão_y <= 0 and personagem_y == Altura/2 - 30:
            saguão_y += 1
        if keys[pygame.K_DOWN] and saguão_y >= -515 and personagem_y == Altura/2 - 30:
            saguão_y -= 1
        if saguão_x >= 0 or saguão_x <= -355:
            if keys[pygame.K_LEFT]:
                personagem_x -= 0.5
            if keys[pygame.K_RIGHT]:
                personagem_x += 0.5
        if saguão_y >= 0 or saguão_y <= -515:
            if keys[pygame.K_UP]:
                personagem_y -= 0.5
            if keys[pygame.K_DOWN]:
                personagem_y += 0.5        

        pygame.display.update()

    #fazendo o fim do tempo (perder)
    while inicio_jogo > final_jogo:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        texto = fonte.render("ACABOU O TEMPO", True, (255, 255, 255))
        tela.blit(texto, (150, 200))
        
        botão_reiniciar = pygame.Rect((235, 300), (150, 30))
        pygame.draw.rect(tela, (255, 0, 0), botão_reiniciar)
        pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            posicao_mouse = pygame.mouse.get_pos()
            if botão_reiniciar.collidepoint(posicao_mouse):
                resetar_jogo()
    inicio_jogo += 1

    #fazendo a chegada final (ganhar)
    while Ganhar >= 200:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        texto = fonte.render("FINAL DA CORRIDA", True, (255, 255, 255))
        tela.blit(texto, (150, 200))

        botão_reiniciar = pygame.Rect((235, 300), (150, 30))
        pygame.draw.rect(tela, (255, 0, 0), botão_reiniciar)
        pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            posicao_mouse = pygame.mouse.get_pos()
            if botão_reiniciar.collidepoint(posicao_mouse):
                resetar_jogo()

    #fazendo o fundo
    if Ganhar <= 20 or Ganhar > 100:
        tela.blit(fundo, (X, Y))
        tela.blit(fundo, (X, Y - 480))
    if Ganhar > 20 and Ganhar < 101:
        tela.blit(fundo_caminho_lado, (X, Y))
        tela.blit(fundo_caminho_lado, (X, Y - 480))
    if Ganhar > 20 and Ganhar < 24:
        tela.blit(fundo, (X, Y4))
        tela.blit(fundo_caminho_virando, (X, Y4 - 480))
    if Ganhar > 100 and Ganhar < 104:
        tela.blit(fundo_caminho_lado, (X, Y5))
        tela.blit(fundo_caminho_virando2, (X, Y5 - 485))
    if Y > 480:
        Y = 0
        if Ganhar < 21:
            Y4 = 0
        if Ganhar < 101:
            Y5 = 0
        Ganhar += 1
        
    if Y2 > 540:
        pedra = pygame.image.load("pedra.png")
        if Ganhar < 20 or Ganhar > 101:
            aleatorio_pedraX = random.randint(200, 380)
        if Ganhar >= 25 and Ganhar < 99:
            aleatorio_pedraX = random.randint(300, 490)
        aleatorio_pedra_tamanhoL = random.choice((32, 48, 64))
        aleatorio_pedra_tamanhoR = aleatorio_pedra_tamanhoL
        if aleatorio_pedra_tamanhoL == 32:
            pedra_hitbox_largura = 30
            pedra_hitbox_altura = 10
        if aleatorio_pedra_tamanhoL == 48:
            pedra_hitbox_largura = 45
            pedra_hitbox_altura = 20
        if aleatorio_pedra_tamanhoL == 64:
            pedra_hitbox_largura = 60
            pedra_hitbox_altura = 30
        aleatorio_pedra = random.randint(1, 7)
        mostrar_pedra = True
        mostrar_relogio = True
        Y2 = 0
    Y5 += Aumento / 10
    Y4 += Aumento / 10
    Y2 += Aumento / 10
    Y += Aumento / 10

    #fazendo a hitbox
    hitbox_cima = pygame.Rect(0, 0, 640, 280)

    hitbox_cima1 = pygame.Rect(0, 0, 640, 240)

    hitbox_cima2 = pygame.Rect(0, 0, 640, 190)

    hitbox_cima3 = pygame.Rect(0, 0, 640, 120)
    
    hitbox_jogador = pygame.Rect((personagem_x) - 3, (personagem_y) + 50, 70, 20)

    hitbox_npc1 = pygame.Rect(npc_x - 40, npc_y - 20, 150, 100)
    hitbox_npc2 = pygame.Rect(npc_x2 - 40, npc_y2 - 20, 150, 100)
    hitbox_npc3 = pygame.Rect(npc_x3 - 40, npc_y3 - 20, 150, 100)

    if pular == 0:
        hitbox_jogador_inimigos = pygame.Rect((personagem_x) - 3, (personagem_y) + 50, 70, 20)
    if pular > 0:
        hitbox_jogador_inimigos = pygame.Rect(-500, -500, 0, 0)

    #fazendo o sprite dos obstáculos
    if aleatorio_pedra == 1 and mostrar_pedra == True:
        pedra = pygame.transform.scale(pedra, (aleatorio_pedra_tamanhoL, aleatorio_pedra_tamanhoR))
        tela.blit(pedra, (aleatorio_pedraX, Y2 - 60))
        hitbox_pedra = pygame.Rect(aleatorio_pedraX, Y2 - 45, pedra_hitbox_largura, pedra_hitbox_altura)
    if mostrar_pedra == False:
        hitbox_pedra = pygame.Rect(-500, -500, 0, 0)

    #fazendo o npc correr
    if inicio_jogo <= 300:
        tela.blit(npc_cima, (npc_x, npc_y))
        tela.blit(npc_cima2, (npc_x2, npc_y2))
        tela.blit(npc_cima3, (npc_x3, npc_y3))
        
    if inicio_jogo >= 300:
        if liberado_npc1 == False:
            tela.blit(npc_correr_esquerda, (npc_x, npc_y))
            if inicio_jogo >= tempo_npc1:
                tempo_npc1 += 30
                liberado_npc1 = True
        if liberado_npc1 == True:
            tela.blit(npc_correr_direita, (npc_x, npc_y))
            if inicio_jogo >= tempo_npc1:
                tempo_npc1 += 30
                liberado_npc1 = False

    if inicio_jogo >= 300:
        if liberado_npc2 == False:
            tela.blit(npc_correr_esquerda2, (npc_x2, npc_y2))
            if inicio_jogo >= tempo_npc2:
                tempo_npc2 += 15
                liberado_npc2 = True
        if liberado_npc2 == True:
            tela.blit(npc_correr_direita2, (npc_x2, npc_y2))
            if inicio_jogo >= tempo_npc2:
                tempo_npc2 += 15
                liberado_npc2 = False

    if inicio_jogo >= 300:
        if liberado_npc3 == False:
            tela.blit(npc_correr_esquerda3, (npc_x3, npc_y3))
            if inicio_jogo >= tempo_npc3:
                tempo_npc3 += 45
                liberado_npc3 = True
        if liberado_npc3 == True:
            tela.blit(npc_correr_direita3, (npc_x3, npc_y3))
            if inicio_jogo >= tempo_npc3:
                tempo_npc3 += 45
                liberado_npc3 = False
        
    if inicio_jogo >= 300:
        npc_y -= 3
        npc_y += Aumento / 10

        npc_y2 -= 5
        npc_y2 += Aumento / 10

        npc_y3 -= 1
        npc_y3 += Aumento / 10

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
        if liberado2 == True:
            tela.blit(correr_esquerda, (personagem_x, personagem_y))
            if ((not keys[pygame.K_x] or not keys[pygame.K_z]) or (keys[pygame.K_x] and keys[pygame.K_z])) and pygame.time.get_ticks() > tempo_3 + tempo_diminuir1:
                tempo_2 = pygame.time.get_ticks()
                tempo_diminuir2 += 50
                liberado2 = False

        if liberado2 == False:
            tela.blit(correr_direita, (personagem_x, personagem_y))
            if ((not keys[pygame.K_z] or not keys[pygame.K_x]) or (keys[pygame.K_z] and keys[pygame.K_x])) and pygame.time.get_ticks() > tempo_2 + tempo_diminuir2:
                tempo_3 = pygame.time.get_ticks()
                tempo_diminuir1 += 50
                liberado2 = True

        if Aumento == 0:
            olhando = 3
            tempo_diminuir1 = 200
            tempo_diminuir2 = 200

    if olhando == 5:
        tela.blit(personagem_cima, (personagem_x, personagem_y))

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

    if hitbox_jogador_inimigos.colliderect(hitbox_pedra) and tomou_hit == False:
        if Aumento >= 5 and Aumento < 40:
            Aumento -= 5
        if Aumento >= 40:
            Aumento -= 40
        Aumento_Contrario -= 20
        tomou_hit = True
        mostrar_pedra = False
        BarraVerde = 15, 10, Aumento, 50
        BarraAzul2 = 15, 75, Aumento_Contrario, 50
    if not hitbox_jogador_inimigos.colliderect(hitbox_pedra):
        tomou_hit = False

    keys = pygame.key.get_pressed()
    if inicio_jogo > 500:
        if hitbox_jogador.colliderect(hitbox_npc1) and continuar_texto == False and relogio_ativado == False:
            tela.blit(espaço, (npc_x - 10, npc_y - 40))
            if keys[pygame.K_SPACE]:
                continuar_texto = True
        if continuar_texto == True:
            balão = pygame.transform.scale(balão, (250, 180))
            tela.blit(balão, (npc_x - 10, npc_y - 80))
            texto_fala = fonte2.render("Ce quer um relógio? Eu", True, (0, 0, 0))
            texto_fala2 = fonte2.render("tenho um de sobra aqui", True, (0, 0, 0))
            tela.blit(texto_fala, (npc_x, npc_y - 70))
            tela.blit(texto_fala2, (npc_x, npc_y - 40))
            tempo_texto += 1
            if tempo_texto >= 120:
                relogio_ativado = True
                continuar_texto = False

    if inicio_jogo > 1000:
        if hitbox_jogador.colliderect (hitbox_npc2) and continuar_texto2 == False:
            tela.blit(espaço, (npc_x2 - 10, npc_y2 - 40))
            if keys[pygame.K_SPACE]:
                continuar_texto2 = True
        if continuar_texto2 == True and parar_texto == False:
            balão = pygame.transform.scale(balão, (290, 180))
            tela.blit(balão, (npc_x2 - 15, npc_y2 - 80))
            texto_fala3 = fonte3.render("Sabia que se você clicar Z e X numa certa", True, (0, 0, 0))
            texto_fala4 = fonte3.render("velocidade você mantém sua aceleração?", True, (0, 0, 0))
            tela.blit(texto_fala3, (npc_x2 - 5, npc_y2 - 70))
            tela.blit(texto_fala4, (npc_x2 - 5, npc_y2 - 40))
            tempo_texto2 += 1
            if tempo_texto2 >= 300:
                parar_texto = True

    if inicio_jogo > 1000:
        if hitbox_jogador.colliderect (hitbox_npc3) and continuar_texto3 == False:
            tela.blit(espaço, (npc_x3 - 10, npc_y3 - 40))
            if keys[pygame.K_SPACE]:
                continuar_texto3 = True
        if continuar_texto3 == True and parar_texto2 == False:
            balão = pygame.transform.scale(balão, (250, 180))
            tela.blit(balão, (npc_x3 - 10, npc_y3 - 80))
            texto_fala5 = fonte4.render("eu ouvi dizer que a segunda", True, (0, 0, 0))
            texto_fala6 = fonte4.render("passagem que é a verdadeira", True, (0, 0, 0))
            tela.blit(texto_fala5, (npc_x3, npc_y3 - 70))
            tela.blit(texto_fala6, (npc_x3 - 5, npc_y3 - 40))
            tempo_texto3 += 1
            if tempo_texto3 >= 420:
                parar_texto2 = True

    tempo_segundos -= 1
    if relogio_ativado == True:
        texto_tempo = fonte.render("00:" + str(int(tempo_segundos/60)), True, (255, 255, 255))
        tela.blit(texto_tempo, (200, 50))
        tempo_texto = 0

    #fazendo a barra de velocidade
#    pygame.draw.rect(tela, (255, 0, 0), (BarraVermelha), 0)
#    pygame.draw.rect(tela, (0, 255, 0), (BarraVerde), 0)

    #fazendo a barra de stamina
    pygame.draw.rect(tela, (255, 0, 0), (BarraVermelha2), 0)
    pygame.draw.rect(tela, (50, 50, 255), (BarraAzul2), 0)

    #definindo as teclas
    keys = pygame.key.get_pressed()

    #teclas para andar e pular correndo
    if pode_andar == False and Cansou == False:
        if keys[pygame.K_LEFT] and personagem_x > 0:
            personagem_x -= 3

        if keys[pygame.K_RIGHT] and personagem_x < 640 - 64:
            personagem_x += 3

        if keys[pygame.K_UP] and not pulo and pular == 0:
            pulo2 = True
            pulo = True

        if pulo2 and pular < 11:
            pular += 1
            personagem_y -= pular
            if pular > 9:
                pulo2 = False
                Aumento_Contrario -= 5

        if not pulo2 and pular > 0:
            pular -= 1
            personagem_y += pular + 1

        if not keys[pygame.K_UP]:
            pulo = False

        if Cansou == True:
            pular = 0
        if pular > 0:
            olhando = 5
        if pular == 0 and Aumento > 0:
            olhando = 4

    #teclas para andar
    if pode_andar == True or (Cansou == True and Aumento <= 0):
        if keys[pygame.K_LEFT] and personagem_x > 0:
            personagem_x -= 1
        if keys[pygame.K_LEFT]:
            esquerda = True
            olhando = 1
        if not keys[pygame.K_LEFT]:
            esquerda = False

        if keys[pygame.K_RIGHT] and personagem_x < 640 - 64:
            personagem_x += 1
        if keys[pygame.K_RIGHT]:
            direita = True
            olhando = 2
        if not keys[pygame.K_RIGHT]:
            direita = False

        if keys[pygame.K_UP] and parou_cima == False:
            personagem_y -= 1
        if keys[pygame.K_UP] and parou_cima == True and inicio_jogo >= 300:
            Aumento = 10
        if keys[pygame.K_UP]:
            cima = True
            olhando = 3
        if not keys[pygame.K_UP]:
            cima = False

        if keys[pygame.K_DOWN] and personagem_y < 410:
            personagem_y += 1
        if keys[pygame.K_DOWN]:
            baixo = True
            olhando = 0
        if not keys[pygame.K_DOWN]:
            baixo = False

    #fazendo o personagem correr
    if inicio_jogo >= 300:
        if Cansou == False:
            if keys[pygame.K_z] and not keys[pygame.K_x] and liberado == True:
                aumentar = True
                liberado = False
                liberado2 = False
                tempo_2 = pygame.time.get_ticks()
                tempo_4 = pygame.time.get_ticks()
                if pular == 0:
                    olhando = 4

            if keys[pygame.K_x] and not keys[pygame.K_z] and liberado == False:
                aumentar = True
                liberado = True
                liberado2 = True
                tempo_3 = pygame.time.get_ticks()
                tempo_5 = pygame.time.get_ticks()
                if pular == 0:
                    olhando = 4

    #fazendo o aumento da velocidade
    if Cansou == False:
        if aumentar == True:
            if parou_cima == False:
                personagem_y -= Aumento2//2

            if parou_cima1 == False and Aumento > 50:
                personagem_y -= Aumento2//2

            if parou_cima2 == False and Aumento > 100:
                personagem_y -= Aumento2//2

            if parou_cima3 == False and Aumento > 150:
                personagem_y -= Aumento2//2
            
            if (not (not (tempo_4 < tempo_5 - 300)) and (not (tempo_4 > tempo_5))) and Aumento > 10:
                pronto = False
            if (not (tempo_4 < tempo_5 - 300)) and (not (tempo_4 > tempo_5)):
                pronto = True

            if Aumento <= 175 and pronto == True:
                Aumento += 1
                BarraVerde = 15, 10, Aumento, 50
            if Aumento <= 20 and Aumento >= 6 and pronto == True:
                Aumento2 += 0.4
            if Aumento > 0 and Aumento < 5 and pronto == True:
                Aumento2 += 5
            if Aumento == 5:
                Aumento2 = 10

            if tempo_diminuir1 > 200:
                tempo_diminuir1 = 200
            if tempo_diminuir2 > 200:
                tempo_diminuir2 = 200

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
    if ((not keys[pygame.K_z] or (not keys[pygame.K_x])) or (keys[pygame.K_z] and (keys[pygame.K_x]))) and pygame.time.get_ticks() > tempo_1 + 500 and cima == False:
        if Aumento > 0:
            Aumento -= 1
        if Aumento > 0 and Aumento <= 20:
            Aumento2 -= 0.4
        if Aumento > 0 and personagem_y <= 230:
            personagem_y += 2
        if Aumento > 0 and personagem_y > 230 and personagem_y < 410:
            personagem_y += 1
        BarraVerde = 15, 10, Aumento, 50
        if Aumento == 0:
            Aumento2 = 0

    if Cansou == False:
        if Aumento == 0:
            pode_andar = True

    #fazendo a barra de stamina regenerar
    if Aumento_Contrario < 176 and Aumento <= 0:
        if Aumento_Contrario < 0:
            Aumento_Contrario = 0
        Aumento_Contrario += 0.05
        BarraAzul2 = 15, 75, Aumento_Contrario, 50
    if Aumento_Contrario < 0:
        Cansou = True
        BarraAzul2 = 15, 75, Aumento_Contrario, 50
    if Aumento_Contrario > 175:
        Cansou = False

    pygame.display.update()
    
