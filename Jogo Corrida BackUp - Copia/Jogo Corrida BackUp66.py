import pygame
import random
import sys
pygame.init()

#tamanhos
Largura = 640
Altura = 480
tela = pygame.display.set_mode((Largura, Altura))
superficie = pygame.Surface((Largura, Altura), pygame.SRCALPHA)

#importando as imagens
fundo = pygame.image.load("fundo.png")
fundo2 = pygame.image.load("fundo2.png")

saguão = pygame.image.load("saguão.png")

personagem_baixo = pygame.image.load("personagem.png")
personagem_cima = pygame.image.load("personagem_cima.png")
personagem_esquerda = pygame.image.load("personagem_esquerda.png")
personagem_direita = pygame.image.load("personagem_direita.png")

npcs = pygame.image.load("personagem.png")
guarda = pygame.image.load("guarda.png")

way = pygame.image.load("npc_cima.png")

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

monstro = pygame.image.load("monstro.png")

fundo_menu = pygame.image.load("menu.jpg")
opçõessim = pygame.image.load("opçõessim.png")
opçõesnao = pygame.image.load("opçõesnao.png")

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
quadrado_y = 265
quadrado_x = 153
quadrado_l = 335
quadrado_a = 50

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

saguão_x = -300
saguão_y = -500

aleatorio_npcs = 0
dimensão_x = -640

monstro_y1 = 200
hit = False
divisão = 10
bug1 = False
bug2 = False
parede_baixo = False
parede_esquerda = False
parede_cima = False
parede_direita = False
seleção = 1

opçãosim = True
jogo_iniciar = False

opções = False
parou_esquerda = False
parou_baixo = False
parou_direita = False
parou_cima01 = False

luz = False

fundo_1 = True
fundo_2 = False
fundo2_x = -560
fundo2_y = -2080
guarda_andar = False

xis1 = 1200
xis2 = 1025
xis3 = 1060
xis4 = 931
xis5 = 1027
xis6 = 1210
xis7 = 800
xis8 = 700
xis9 = 526
xis10 = 716
xis11 = 670
xis12 = 616
xis13 = 865
xis14 = 520
xis15 = 600
xis16 = 1200

yps1 = 181
yps2 = 350
yps3 = 460
yps4 = 526
yps5 = 608
yps6 = 780
yps7 = 710
yps8 = 700
yps9 = 525
yps10 = 453
yps11 = 370
yps12 = 250
yps13 = 380
yps14 = 150
yps15 = 800
yps16 = 460

guardax1 = 521
guardax2 = 521
guardax3 = 1210
guardax4 = 1210
guardax5 = 718
guardax6 = 1010
guardax7 = 690
guardax8 = 1090

guarday1 = 685
guarday2 = 270
guarday3 = 685
guarday4 = 270
guarday5 = 95
guarday6 = 95
guarday7 = 820
guarday8 = 820

falando = False

parou_texto_guarda1 = False
continuar_texto_guarda1 = False
tempo_texto_guarda1 = 0

parou_texto_guarda2 = False
continuar_texto_guarda2 = False
tempo_texto_guarda2 = 0

parou_texto_guarda3 = False
continuar_texto_guarda3 = False
tempo_texto_guarda3 = 0

parou_texto_guarda4 = False
continuar_texto_guarda4 = False
tempo_texto_guarda4 = 0

parou_texto_guarda5 = False
continuar_texto_guarda5 = False
tempo_texto_guarda5 = 0

parou_texto_guarda6 = False
continuar_texto_guarda6 = False
tempo_texto_guarda6 = 0

inicio_jogo_saguão = 0

wayx = 1010
wayy = 743

falaway = False
tempo_fala_way = 0

hitboxway = pygame.Rect(saguão_x + wayx, saguão_y + wayy, 64, 64)

começou_tempo = 0

#colocar no resetar jogo
falaway2 = False
tempo_fala_way2 = 0

#colocando o FPS
clock = pygame.time.Clock()
fps = 60

#escrevendo o título
pygame.display.set_caption("Maratona Da Ascensão")    

#definindo o resetar_jogo (trazendo tudo de volta resetando tudo, qualquer variável nova é bom adicionar aqui)
def resetar_jogo():
    global personagem_x, personagem_y, dimensão_x, hit, divisão, começou_tempo, guardax7, guardax8, guarday7, guarday8, wayx, wayy, falaway, tempo_fala_way, luz, superficie, falando, parou_texto_guarda1, parou_texto_guarda2, parou_texto_guarda3, parou_texto_guarda4, parou_texto_guarda5, parou_texto_guarda6, continuar_texto_guarda1, continuar_texto_guarda2, continuar_texto_guarda3, continuar_texto_guarda4, continuar_texto_guarda5, continuar_texto_guarda6, tempo_texto_guarda1, tempo_texto_guarda2, tempo_texto_guarda3, tempo_texto_guarda4, tempo_texto_guarda5, tempo_texto_guarda6, opções, bug1, bug2, parede_baixo, opções, fundo_1, fundo_2, fundo2_x, fundo2_y, guarda_andar, xis1, xis2, xis3, xis4, xis5, xis6, xis7, xis8, xis9, xis10, xis11, xis12, xis13, xis14, xis15, xis16, yps1, yps2, yps3, yps4, yps5, yps6, yps7, yps8, yps9, yps10, yps11, yps12, yps13, yps14, yps15, yps16, guardax1,  guardax2, guardax3, guardax4, guardax5, guardax6, guarday1, guarday2, guarday3, guarday4, guarday5, guarday6, parou_esquerda, parou_baixo, parou_direita, parou_cima01, jogo_iniciar, parede_esquerda, parede_cima, parede_direita, seleção, tempo_npc1, tempo_npc2, tempo_npc3, liberado_npc1, liberado_npc2, liberado_npc3, aleatorio_npcs, quadrado_y, menu, saguão_menu, saguão_x, saguão_y, posição_momentox, posição_momentoy, tempo_texto, continuar_texto, parar_texto2, continuar_texto2, continuar_texto3, tempo_texto2, tempo_texto3, parar_texto, npc_x, npc_y, npc_x2, npc_y2, npc_x3, npc_y3, X, Y, Y3, Y4, Y5, parou_cima, parou_cima1, parou_cima2, parou_cima3, cima, baixo, esquerda, direita, olhando, liberado, aumentar, pode_andar, Cansou, Aumento, Aumento2, Aumento_Contrario, inicio_jogo, final_jogo, BarraVermelha, BarraVerde, BarraVermelha2, BarraAzul2, tempo_diminuir1, tempo_diminuir2, Ganhar, Pular, Pulo, Pulo2, aleatorio_pedra, aleatorio_pedraX, Y2, hitbox_pedra, tomou_hit, mostrar_pedra, aleatorio_pedra_tamanhoL, aleatorio_pedra_tamanhoR, pedra_hitbox_largura, liberado2, pronto, mostrar_relogio, tempo_segundos
    personagem_x = 290
    personagem_y = 410
    X = -550
    Y = -1408
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
    saguão_x = -1150
    saguão_y = -115
    aleatorio_npcs = 0
    quadrado_y = 265
    dimensão_x = -640
    monstro_y1 = 200
    hit = False
    divisão = 10
    bug1 = False
    bug2 = False
    parede_baixo = False
    parede_esquerda = False
    parede_cima = False
    parede_direita = False
    seleção = 1
    opções = False
    jogo_iniciar = False
    superficie = pygame.Surface((Largura, Altura), pygame.SRCALPHA)
    opções = False
    parou_esquerda = False
    parou_baixo = False
    parou_direita = False
    parou_cima01 = False
    luz = False
    fundo_1 = True
    fundo_2 = False
    fundo2_x = -560
    fundo2_y = -2080
    guarda_andar = False
    xis1 = 1200
    xis2 = 1025
    xis3 = 1060
    xis4 = 931
    xis5 = 1027
    xis6 = 1210
    xis7 = 800
    xis8 = 700
    xis9 = 526
    xis10 = 716
    xis11 = 670
    xis12 = 616
    xis13 = 865
    xis14 = 520
    xis15 = 600
    xis16 = 1200
    yps1 = 181
    yps2 = 350
    yps3 = 460
    yps4 = 526
    yps5 = 608
    yps6 = 780
    yps7 = 710
    yps8 = 700
    yps9 = 525
    yps10 = 453
    yps11 = 370
    yps12 = 250
    yps13 = 380
    yps14 = 150
    yps15 = 800
    yps16 = 460
    guardax1 = 521
    guardax2 = 521
    guardax3 = 1210
    guardax4 = 1210
    guardax5 = 718
    guardax6 = 1010
    guardax7 = 690
    guardax8 = 1090
    guarday1 = 685
    guarday2 = 270
    guarday3 = 685
    guarday4 = 270
    guarday5 = 95
    guarday6 = 95
    guarday7 = 820
    guarday8 = 820
    falando = False
    parou_texto_guarda1 = False
    continuar_texto_guarda1 = False
    tempo_texto_guarda1 = 0
    parou_texto_guarda2 = False
    continuar_texto_guarda2 = False
    tempo_texto_guarda2 = 0
    parou_texto_guarda3 = False
    continuar_texto_guarda3 = False
    tempo_texto_guarda3 = 0
    parou_texto_guarda4 = False
    continuar_texto_guarda4 = False
    tempo_texto_guarda4 = 0
    parou_texto_guarda5 = False
    continuar_texto_guarda5 = False
    tempo_texto_guarda5 = 0
    parou_texto_guarda6 = False
    continuar_texto_guarda6 = False
    tempo_texto_guarda6 = 0
    inicio_jogo_saguão = 0
    wayx = 1010
    wayy = 743
    falaway = False
    tempo_fala_way = 0
    começou_tempo = 0

while True:
    #fazendo o jogo funcionar e desligar quando clicar no X
    clock.tick(fps) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #fazendo o menu do jogo
    while menu == True:
        clock.tick(fps)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (keys[pygame.K_z] and seleção == 4):
                pygame.quit()
                sys.exit()
        teste = pygame.Rect((quadrado_x, quadrado_y), (quadrado_l, quadrado_a))
        tela.blit(fundo_menu, (0, 0))
        pygame.draw.rect(tela, (255, 0, 0), teste, 3)
        if event.type == pygame.KEYUP:
            if keys[pygame.K_UP] and seleção == 2:
                seleção = 1
            elif keys[pygame.K_DOWN] and seleção == 1 :
                seleção = 2
            elif keys[pygame.K_UP] and seleção == 3:
                seleção = 2
            elif keys[pygame.K_DOWN] and seleção == 2:
                seleção = 3
            elif keys[pygame.K_UP] and seleção == 4:
                seleção = 3
            elif keys[pygame.K_DOWN] and seleção == 3:
                seleção = 4
        if seleção == 1:
            quadrado_y = 265
            quadrado_x = 153
            quadrado_l = 335
            quadrado_a = 50
        if seleção == 2:
            quadrado_y = 315
            quadrado_x = 100
            quadrado_l = 440
            quadrado_a = 50
        if seleção == 3:
            quadrado_y = 365
            quadrado_x = 225
            quadrado_l = 195
            quadrado_a = 50
        if seleção == 4:
            quadrado_y = 415
            quadrado_x = 153
            quadrado_l = 335
            quadrado_a = 50
        pygame.display.update()
        if event.type == pygame.KEYUP:
            if keys[pygame.K_z] and seleção == 1:
                resetar_jogo()
                saguão_menu = True
                personagem_x = Largura - 80 
                personagem_y = Altura/2 - 30
                aleatorio_npcs = random.choice((1, 2, 3, 4, 5, 6))
                olhando = 1
                menu = False
            if keys[pygame.K_z] and seleção == 3:
                opções = True
                menu = False

    #fazendo as opções
    while opções == True:
        clock.tick(fps)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if opçãosim == True:
            tela.blit(opçõessim, (0, 0))
        if opçãosim == False:
            tela.blit(opçõesnao, (0, 0))

        if event.type == pygame.KEYUP:
            if opçãosim == True and keys[pygame.K_z]:
                opçãosim = False

            elif opçãosim == False and keys[pygame.K_z]:
                opçãosim = True

        if keys[pygame.K_x]:
            menu = True
            opções = False
        pygame.display.update()

    #fazendo o saguão do jogo
    while saguão_menu == True:    
        clock.tick(fps) 
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        tela.blit(saguão, (saguão_x, saguão_y))

        #fazendo os npcs randoms
        tela.blit(npcs, (saguão_x + 1200, saguão_y + 181))
        hitboxnpc1 = pygame.Rect(saguão_x + xis1, saguão_y + yps1, 64, 64)

        tela.blit(npcs, (saguão_x + 1025, saguão_y + 350))
        hitboxnpc2 = pygame.Rect(saguão_x + xis2, saguão_y + yps2, 64, 64)

        tela.blit(npcs, (saguão_x + 1060, saguão_y + 460))
        hitboxnpc3 = pygame.Rect(saguão_x + xis3, saguão_y + yps3, 64, 64)

        tela.blit(npcs, (saguão_x + 931, saguão_y + 526))
        hitboxnpc4 = pygame.Rect(saguão_x + xis4, saguão_y + yps4, 64, 64)

        tela.blit(npcs, (saguão_x + 1027, saguão_y + 608))
        hitboxnpc5 = pygame.Rect(saguão_x + xis5, saguão_y + yps5, 64, 64)

        tela.blit(npcs, (saguão_x + 1210, saguão_y + 780))
        hitboxnpc6 = pygame.Rect(saguão_x + xis6, saguão_y + yps6, 64, 64)

        tela.blit(npcs, (saguão_x + 800, saguão_y + 710))
        hitboxnpc7 = pygame.Rect(saguão_x + xis7, saguão_y + yps7, 64, 64)

        tela.blit(npcs, (saguão_x + 700, saguão_y + 700))
        hitboxnpc8 = pygame.Rect(saguão_x + xis8, saguão_y + yps8, 64, 64)

        tela.blit(npcs, (saguão_x + 526, saguão_y + 525))
        hitboxnpc9 = pygame.Rect(saguão_x + xis9, saguão_y + yps9, 64, 64)

        tela.blit(npcs, (saguão_x + 716, saguão_y + 453))
        hitboxnpc10 = pygame.Rect(saguão_x + xis10, saguão_y + yps10, 64, 64)

        tela.blit(npcs, (saguão_x + 670, saguão_y + 370))
        hitboxnpc11 = pygame.Rect(saguão_x + xis11, saguão_y + yps11, 64, 64)

        tela.blit(npcs, (saguão_x + 616, saguão_y + 250))
        hitboxnpc12 = pygame.Rect(saguão_x + xis12, saguão_y + yps12, 64, 64)

        tela.blit(npcs, (saguão_x + 865, saguão_y + 380))
        hitboxnpc13 = pygame.Rect(saguão_x + xis13, saguão_y + yps13, 64, 64)

        #fazendo os guardas
        tela.blit(guarda, (saguão_x + guardax1, saguão_y + guarday1))
        hitboxguarda1 = pygame.Rect(saguão_x + guardax1, saguão_y + guarday1, 64, 64)

        tela.blit(guarda, (saguão_x + guardax2, saguão_y + guarday2))
        hitboxguarda2 = pygame.Rect(saguão_x + guardax2, saguão_y + guarday2, 64, 64)

        tela.blit(guarda, (saguão_x + guardax3, saguão_y + guarday3))
        hitboxguarda3 = pygame.Rect(saguão_x + guardax3, saguão_y + guarday3, 64, 64)

        tela.blit(guarda, (saguão_x + guardax4, saguão_y + guarday4))
        hitboxguarda4 = pygame.Rect(saguão_x + guardax4, saguão_y + guarday4, 64, 64)

        tela.blit(guarda, (saguão_x + guardax5, saguão_y + guarday5))
        hitboxguarda5 = pygame.Rect(saguão_x + guardax5, saguão_y + guarday5, 64, 64)

        tela.blit(guarda, (saguão_x + guardax6, saguão_y + guarday6))
        hitboxguarda6 = pygame.Rect(saguão_x + guardax6, saguão_y + guarday6, 64, 64)

        tela.blit(guarda, (saguão_x + guardax7, saguão_y + guarday7))
        hitboxguarda7 = pygame.Rect(saguão_x + guardax7, saguão_y + guarday7, 64, 64)
        
        tela.blit(guarda, (saguão_x + guardax8, saguão_y + guarday8))
        hitboxguarda8 = pygame.Rect(saguão_x + guardax8, saguão_y + guarday8, 64, 64)

        #fazendo os npcs especiais
        if aleatorio_npcs == 1:
            tela.blit(npc_cima, (saguão_x + xis14, saguão_y + yps14))
            npc_x = saguão_x + xis14
            npc_y = saguão_y + yps14
            tela.blit(npc_cima2, (saguão_x + xis15, saguão_y + yps15))
            npc_x2 = saguão_x + xis15
            npc_y2 = saguão_y + yps15
            tela.blit(npc_cima3, (saguão_x + xis16, saguão_y + yps16))
            npc_x3 = saguão_x + xis16
            npc_y3 = saguão_y + yps16
        if aleatorio_npcs == 2:
            tela.blit(npc_cima2, (saguão_x + xis14, saguão_y + yps14))
            npc_x2 = saguão_x + xis14
            npc_y2 = saguão_y + yps14
            tela.blit(npc_cima3, (saguão_x + xis15, saguão_y + yps15))
            npc_x3 = saguão_x + xis15
            npc_y3 = saguão_y + yps15
            tela.blit(npc_cima, (saguão_x + xis16, saguão_y + yps16))
            npc_x = saguão_x + xis16
            npc_y = saguão_y + yps16
        if aleatorio_npcs == 3:
            tela.blit(npc_cima3, (saguão_x + xis14, saguão_y + yps14))
            npc_x3 = saguão_x + xis14
            npc_y3 = saguão_y + yps14
            tela.blit(npc_cima, (saguão_x + xis15, saguão_y + yps15))
            npc_x = saguão_x + xis15
            npc_y = saguão_y + yps15
            tela.blit(npc_cima2, (saguão_x + xis16, saguão_y + yps16))
            npc_x2 = saguão_x + xis16
            npc_y2 = saguão_y + yps16
        if aleatorio_npcs == 4:
            tela.blit(npc_cima, (saguão_x + xis14, saguão_y + yps14))
            npc_x = saguão_x + xis14
            npc_y = saguão_y + yps14
            tela.blit(npc_cima3, (saguão_x + xis15, saguão_y + yps15))
            npc_x3 = saguão_x + xis15
            npc_y3 = saguão_y + yps15
            tela.blit(npc_cima2, (saguão_x + xis16, saguão_y + yps16))
            npc_x2 = saguão_x + xis16
            npc_y2 = saguão_y + yps16
        if aleatorio_npcs == 5:
            tela.blit(npc_cima2, (saguão_x + xis14, saguão_y + yps14))
            npc_x2 = saguão_x + xis14
            npc_y2 = saguão_y + yps14
            tela.blit(npc_cima, (saguão_x + xis15, saguão_y + yps15))
            npc_x = saguão_x + xis15
            npc_y = saguão_y + yps15
            tela.blit(npc_cima3, (saguão_x + xis16, saguão_y + yps16))
            npc_x3 = saguão_x + xis16
            npc_y3 = saguão_y + yps16
        if aleatorio_npcs == 6:
            tela.blit(npc_cima3, (saguão_x + xis14, saguão_y + yps14))
            npc_x3 = saguão_x + xis14
            npc_y3 = saguão_y + yps14
            tela.blit(npc_cima2, (saguão_x + xis15, saguão_y + yps15))
            npc_x2 = saguão_x + xis15
            npc_y2 = saguão_y + yps15
            tela.blit(npc_cima, (saguão_x + xis16, saguão_y + yps16))
            npc_x = saguão_x + xis16
            npc_y = saguão_y + yps16
            
        if inicio_jogo_saguão >= 1500:
            tela.blit(way, (saguão_x + wayx, saguão_y + wayy))
            hitboxway = pygame.Rect(saguão_x + wayx, saguão_y + wayy, 64, 64)

        if inicio_jogo_saguão >= 1590 and wayx <= 1129 and inicio_jogo_saguão <= 1800:
            wayx += 1.5

        if wayx >= 1129 and wayy >= 181:
            wayy -= 1.5

        if wayy <= 181 and wayx >= 867:
            wayx -= 1.5

        if wayx <= 867 and wayy >= 138:
            wayy -= 1.5

        hitbox_jogador_esquerda = pygame.Rect((personagem_x) - 10, (personagem_y) + 55, 10, 10)
        hitbox_jogador_direita = pygame.Rect((personagem_x) + 61, (personagem_y) + 55, 10, 10)
        hitbox_jogador_baixo = pygame.Rect((personagem_x) - 1, (personagem_y) + 67, 67, 3)
        hitbox_jogador_cima = pygame.Rect((personagem_x) - 1, (personagem_y) + 50, 67, 3)

        hitbox_jogador = pygame.Rect((personagem_x) - 3, (personagem_y) + 50, 70, 20)

        hitboxnpc14 = pygame.Rect(npc_x, npc_y, 64, 64)
        hitboxnpc15 = pygame.Rect(npc_x2, npc_y2, 64, 64)
        hitboxnpc16 = pygame.Rect(npc_x3, npc_y3, 64, 64)
        
        hitbox_npc1 = pygame.Rect(npc_x - 40, npc_y - 20, 150, 100)
        hitbox_npc2 = pygame.Rect(npc_x2 - 40, npc_y2 - 20, 150, 100)
        hitbox_npc3 = pygame.Rect(npc_x3 - 40, npc_y3 - 20, 150, 100)

        hitbox_guarda1 = pygame.Rect(saguão_x + guardax1 - 40, saguão_y + guarday1 - 20, 150, 100)
        hitbox_guarda2 = pygame.Rect(saguão_x + guardax2 - 40, saguão_y + guarday2 - 20, 150, 100)
        hitbox_guarda3 = pygame.Rect(saguão_x + guardax3 - 40, saguão_y + guarday3 - 20, 150, 100)
        hitbox_guarda4 = pygame.Rect(saguão_x + guardax4 - 40, saguão_y + guarday4 - 20, 150, 100)
        hitbox_guarda5 = pygame.Rect(saguão_x + guardax5 - 40, saguão_y + guarday5 - 20, 150, 100)
        hitbox_guarda6 = pygame.Rect(saguão_x + guardax6 - 40, saguão_y + guarday6 - 20, 150, 100)

        hitbox_parede1 = pygame.Rect(saguão_x, saguão_y, 515, 1039)
        hitbox_parede2 = pygame.Rect(saguão_x, saguão_y, 768, 128)
        hitbox_parede22 = pygame.Rect(saguão_x + 1023, saguão_y, 768, 128)
        hitbox_parede3 = pygame.Rect(saguão_x + 1280, saguão_y, 448, 350)
        hitbox_parede322 = pygame.Rect(saguão_x + 1285, saguão_y, 448, 352)
        hitbox_parede32 = pygame.Rect(saguão_x + 1280, saguão_y + 420, 448, 1039)
        hitbox_parede3222 = pygame.Rect(saguão_x + 1285, saguão_y + 418, 448, 1039)
        hitbox_parede4 = pygame.Rect(saguão_x, saguão_y + 897, 1330, 142)

        hitbox_parede_passar = pygame.Rect(saguão_x + 767, saguão_y, 257, 108)

        if guarda_andar == False:
            hitbox_guarda_andar1 = pygame.Rect(saguão_x + 1071, saguão_y + 280, 124, 60)
            hitbox_guarda_andar2 = pygame.Rect(saguão_x + 1110, saguão_y + 530, 102, 36)
            hitbox_guarda_andar3 = pygame.Rect(saguão_x + 588, saguão_y + 442, 116, 392)
            hitbox_guarda_andar4 = pygame.Rect(saguão_x + 651, saguão_y + 317, 55, 76)
            
        if guarda_andar == True and guarday4 < 350:
            guarday1 -= 1
            guarday2 += 1
            guarday3 -= 1
            guarday4 += 1
            
            hitbox_guarda_andar1 = pygame.Rect(saguão_x - 1000, saguão_y - 1000, 0, 0)
            hitbox_guarda_andar2 = pygame.Rect(saguão_x - 1000, saguão_y - 1000, 0, 0)
            hitbox_guarda_andar3 = pygame.Rect(saguão_x - 1000, saguão_y - 1000, 0, 0)
            hitbox_guarda_andar4 = pygame.Rect(saguão_x - 1000, saguão_y - 1000, 0, 0)

        if hitbox_jogador.colliderect(hitbox_guarda_andar1) or hitbox_jogador.colliderect(hitbox_guarda_andar2) or hitbox_jogador.colliderect(hitbox_guarda_andar3) or hitbox_jogador.colliderect(hitbox_guarda_andar4):
            guarda_andar = True

        if hitbox_jogador.colliderect(hitbox_parede1) or hitbox_jogador_esquerda.colliderect(hitboxnpc1) or hitbox_jogador_esquerda.colliderect(hitboxnpc2) or hitbox_jogador_esquerda.colliderect(hitboxnpc3) or hitbox_jogador_esquerda.colliderect(hitboxnpc4) or hitbox_jogador_esquerda.colliderect(hitboxnpc5) or hitbox_jogador_esquerda.colliderect(hitboxnpc6) or hitbox_jogador_esquerda.colliderect(hitboxnpc7) or hitbox_jogador_esquerda.colliderect(hitboxnpc8) or hitbox_jogador_esquerda.colliderect(hitboxnpc9) or hitbox_jogador_esquerda.colliderect(hitboxnpc10) or hitbox_jogador_esquerda.colliderect(hitboxnpc11) or hitbox_jogador_esquerda.colliderect(hitboxnpc12) or hitbox_jogador_esquerda.colliderect(hitboxnpc13) or hitbox_jogador_esquerda.colliderect(hitboxnpc14) or hitbox_jogador_esquerda.colliderect(hitboxnpc15) or hitbox_jogador_esquerda.colliderect(hitboxnpc16) or hitbox_jogador_esquerda.colliderect(hitboxguarda1) or hitbox_jogador_esquerda.colliderect(hitboxguarda2) or hitbox_jogador_esquerda.colliderect(hitboxguarda3) or hitbox_jogador_esquerda.colliderect(hitboxguarda4) or hitbox_jogador_esquerda.colliderect(hitboxguarda5) or hitbox_jogador_esquerda.colliderect(hitboxguarda6) or hitbox_jogador_esquerda.colliderect(hitboxguarda7) or hitbox_jogador_esquerda.colliderect(hitboxguarda8) or hitbox_jogador_esquerda.colliderect(hitboxway):
            parede_esquerda = True
        else:
            parede_esquerda = False

        if hitbox_jogador.colliderect(hitbox_parede2) or hitbox_jogador.colliderect(hitbox_parede322) or hitbox_jogador.colliderect(hitbox_parede22) or hitbox_jogador_cima.colliderect(hitboxnpc1) or hitbox_jogador_cima.colliderect(hitboxnpc2) or hitbox_jogador_cima.colliderect(hitboxnpc3) or hitbox_jogador_cima.colliderect(hitboxnpc4) or hitbox_jogador_cima.colliderect(hitboxnpc5) or hitbox_jogador_cima.colliderect(hitboxnpc6) or hitbox_jogador_cima.colliderect(hitboxnpc7) or hitbox_jogador_cima.colliderect(hitboxnpc8) or hitbox_jogador_cima.colliderect(hitboxnpc9) or hitbox_jogador_cima.colliderect(hitboxnpc10) or hitbox_jogador_cima.colliderect(hitboxnpc11) or hitbox_jogador_cima.colliderect(hitboxnpc12) or hitbox_jogador_cima.colliderect(hitboxnpc13) or hitbox_jogador_cima.colliderect(hitboxnpc14) or hitbox_jogador_cima.colliderect(hitboxnpc15) or hitbox_jogador_cima.colliderect(hitboxnpc16) or hitbox_jogador_cima.colliderect(hitboxguarda1) or hitbox_jogador_cima.colliderect(hitboxguarda2) or hitbox_jogador_cima.colliderect(hitboxguarda3) or hitbox_jogador_cima.colliderect(hitboxguarda4) or hitbox_jogador_cima.colliderect(hitboxguarda5) or hitbox_jogador_cima.colliderect(hitboxguarda6) or hitbox_jogador_cima.colliderect(hitboxguarda7) or hitbox_jogador_cima.colliderect(hitboxguarda8) or hitbox_jogador_cima.colliderect(hitboxway):
            parede_cima = True
        else:
            parede_cima = False

        if hitbox_jogador.colliderect(hitbox_parede3) or hitbox_jogador.colliderect(hitbox_parede32) or hitbox_jogador_direita.colliderect(hitboxnpc1) or hitbox_jogador_direita.colliderect(hitboxnpc2) or hitbox_jogador_direita.colliderect(hitboxnpc3) or hitbox_jogador_direita.colliderect(hitboxnpc4) or hitbox_jogador_direita.colliderect(hitboxnpc5) or hitbox_jogador_direita.colliderect(hitboxnpc6) or hitbox_jogador_direita.colliderect(hitboxnpc7) or hitbox_jogador_direita.colliderect(hitboxnpc8) or hitbox_jogador_direita.colliderect(hitboxnpc9) or hitbox_jogador_direita.colliderect(hitboxnpc10) or hitbox_jogador_direita.colliderect(hitboxnpc11) or hitbox_jogador_direita.colliderect(hitboxnpc12) or hitbox_jogador_direita.colliderect(hitboxnpc13) or hitbox_jogador_direita.colliderect(hitboxnpc14) or hitbox_jogador_direita.colliderect(hitboxnpc15) or hitbox_jogador_direita.colliderect(hitboxnpc16) or hitbox_jogador_direita.colliderect(hitboxguarda1) or hitbox_jogador_direita.colliderect(hitboxguarda2) or hitbox_jogador_direita.colliderect(hitboxguarda3) or hitbox_jogador_direita.colliderect(hitboxguarda4) or hitbox_jogador_direita.colliderect(hitboxguarda5) or hitbox_jogador_direita.colliderect(hitboxguarda6) or hitbox_jogador_direita.colliderect(hitboxguarda7) or hitbox_jogador_direita.colliderect(hitboxguarda8) or hitbox_jogador_direita.colliderect(hitboxway):
            parede_direita = True
        else:
            parede_direita = False

        if hitbox_jogador.colliderect(hitbox_parede4) or hitbox_jogador.colliderect(hitbox_parede3222) or hitbox_jogador_baixo.colliderect(hitboxnpc1) or hitbox_jogador_baixo.colliderect(hitboxnpc2) or hitbox_jogador_baixo.colliderect(hitboxnpc3) or hitbox_jogador_baixo.colliderect(hitboxnpc4) or hitbox_jogador_baixo.colliderect(hitboxnpc5) or hitbox_jogador_baixo.colliderect(hitboxnpc6) or hitbox_jogador_baixo.colliderect(hitboxnpc7) or hitbox_jogador_baixo.colliderect(hitboxnpc8) or hitbox_jogador_baixo.colliderect(hitboxnpc9) or hitbox_jogador_baixo.colliderect(hitboxnpc10) or hitbox_jogador_baixo.colliderect(hitboxnpc11) or hitbox_jogador_baixo.colliderect(hitboxnpc12) or hitbox_jogador_baixo.colliderect(hitboxnpc13) or hitbox_jogador_baixo.colliderect(hitboxnpc14) or hitbox_jogador_baixo.colliderect(hitboxnpc15) or hitbox_jogador_baixo.colliderect(hitboxnpc16) or hitbox_jogador_baixo.colliderect(hitboxguarda1) or hitbox_jogador_baixo.colliderect(hitboxguarda2) or hitbox_jogador_baixo.colliderect(hitboxguarda3) or hitbox_jogador_baixo.colliderect(hitboxguarda4) or hitbox_jogador_baixo.colliderect(hitboxguarda5) or hitbox_jogador_baixo.colliderect(hitboxguarda6) or hitbox_jogador_baixo.colliderect(hitboxguarda7) or hitbox_jogador_baixo.colliderect(hitboxguarda8) or hitbox_jogador_baixo.colliderect(hitboxway):
            parede_baixo = True
        else:
            parede_baixo = False
        
        if olhando == 0:
            tela.blit(personagem_baixo, (personagem_x, personagem_y))

        if olhando == 3:
            tela.blit(personagem_cima, (personagem_x, personagem_y))

        if olhando == 1:
            tela.blit(personagem_esquerda, (personagem_x, personagem_y))

        if olhando == 2:
            tela.blit(personagem_direita, (personagem_x, personagem_y))

        if keys[pygame.K_LEFT] and saguão_x <= 0 and personagem_x == Largura/2 - 30 and parede_esquerda == False:
            saguão_x += 2
            olhando = 1
        if keys[pygame.K_RIGHT] and saguão_x >= -1152 and personagem_x == Largura/2 - 30 and parede_direita == False:
            saguão_x -= 2
            olhando = 2
        if keys[pygame.K_UP] and saguão_y <= 0 and personagem_y == Altura/2 - 30 and parede_cima == False:
            saguão_y += 2
            olhando = 3
        if keys[pygame.K_DOWN] and saguão_y >= -515 and personagem_y == Altura/2 - 30 and parede_baixo == False:
            saguão_y -= 2
            olhando = 0
                
        if saguão_x >= 0 or saguão_x <= -1150:
            if keys[pygame.K_LEFT] and personagem_x > 15 and parede_esquerda == False:
                personagem_x -= 1.5
                olhando = 1
            if keys[pygame.K_RIGHT] and personagem_x < 555 and parede_direita == False:
                personagem_x += 1.5
                olhando = 2
        if saguão_y >= 0 or saguão_y <= -515:
            if keys[pygame.K_UP] and personagem_y > -15 and parede_cima == False:
                personagem_y -= 1.5
                olhando = 3
            if keys[pygame.K_DOWN] and personagem_y < 395 and parede_baixo == False:
                personagem_y += 1.5
                olhando = 0

        if hitbox_jogador.colliderect(hitbox_npc1) and continuar_texto == False and relogio_ativado == False and falando == False:
            tela.blit(espaço, (npc_x - 10, npc_y - 40))
            if keys[pygame.K_SPACE]:
                continuar_texto = True
        if continuar_texto == True:
            falando = True
            balão = pygame.transform.scale(balão, (250, 180))
            tela.blit(balão, (npc_x - 10, npc_y - 80))
            texto_fala = fonte2.render("Ce quer um relógio? Eu", True, (0, 0, 0))
            texto_fala2 = fonte2.render("tenho um de sobra aqui", True, (0, 0, 0))
            tela.blit(texto_fala, (npc_x, npc_y - 70))
            tela.blit(texto_fala2, (npc_x, npc_y - 40))
            tempo_texto += 1
            if tempo_texto >= 150:
                relogio_ativado = True
                falando = False
                continuar_texto = False

        if hitbox_jogador.colliderect(hitbox_guarda1) and continuar_texto_guarda1 == False and parou_texto_guarda1 == False and falando == False:
            tela.blit(espaço, (saguão_x + guardax1 - 10, saguão_y + guarday1 - 40))
            if keys[pygame.K_SPACE]:
                continuar_texto_guarda1 = True
        if continuar_texto_guarda1 == True:
            falando = True
            balão = pygame.transform.scale(balão, (190, 180))
            tela.blit(balão, (saguão_x + guardax1 - 10, saguão_y + guarday1 - 80))
            texto_fala = fonte2.render("Por aqui tu não", True, (0, 0, 0))
            texto_fala2 = fonte2.render("encontrará nada.", True, (0, 0, 0))
            tela.blit(texto_fala, (saguão_x + guardax1, saguão_y + guarday1 - 70))
            tela.blit(texto_fala2, (saguão_x + guardax1, saguão_y + guarday1 - 40))
            tempo_texto_guarda1 += 1
            if tempo_texto_guarda1 >= 200:
                parou_texto_guarda1 = True
                falando = False
                continuar_texto_guarda1 = False

        if hitbox_jogador.colliderect(hitbox_guarda2) and continuar_texto_guarda2 == False and parou_texto_guarda2 == False and falando == False:
            tela.blit(espaço, (saguão_x + guardax2 - 10, saguão_y + guarday2 - 40))
            if keys[pygame.K_SPACE]:
                continuar_texto_guarda2 = True
        if continuar_texto_guarda2 == True:
            falando = True
            balão = pygame.transform.scale(balão, (175, 180))
            tela.blit(balão, (saguão_x + guardax2 - 10, saguão_y + guarday2 - 80))
            texto_fala = fonte2.render("Essa passagem", True, (0, 0, 0))
            texto_fala2 = fonte2.render("Está fechada.", True, (0, 0, 0))
            tela.blit(texto_fala, (saguão_x + guardax2, saguão_y + guarday2 - 70))
            tela.blit(texto_fala2, (saguão_x + guardax2, saguão_y + guarday2 - 40))
            tempo_texto_guarda2 += 1
            if tempo_texto_guarda2 >= 200:
                parou_texto_guarda2 = True
                falando = False
                continuar_texto_guarda2 = False

        if hitbox_jogador.colliderect(hitbox_guarda3) and continuar_texto_guarda3 == False and parou_texto_guarda3 == False and falando == False:
            tela.blit(espaço, (saguão_x + guardax3 - 10, saguão_y + guarday3 - 40))
            if keys[pygame.K_SPACE]:
                continuar_texto_guarda3 = True
        if continuar_texto_guarda3 == True:
            falando = True
            balão = pygame.transform.scale(balão, (220, 180))
            tela.blit(balão, (saguão_x + guardax3 - 10, saguão_y + guarday3 - 80))
            texto_fala = fonte2.render("Por aqui não, volte", True, (0, 0, 0))
            texto_fala2 = fonte2.render("e espere instruções", True, (0, 0, 0))
            tela.blit(texto_fala, (saguão_x + guardax3, saguão_y + guarday3 - 70))
            tela.blit(texto_fala2, (saguão_x + guardax3, saguão_y + guarday3 - 40))
            tempo_texto_guarda3 += 1
            if tempo_texto_guarda3 >= 200:
                parou_texto_guarda3 = True
                falando = False
                continuar_texto_guarda3 = False

        if hitbox_jogador.colliderect(hitbox_guarda4) and continuar_texto_guarda4 == False and parou_texto_guarda4 == False and falando == False:
            tela.blit(espaço, (saguão_x + guardax4 - 10, saguão_y + guarday4 - 40))
            if keys[pygame.K_SPACE]:
                continuar_texto_guarda4 = True
        if continuar_texto_guarda4 == True:
            falando = True
            balão = pygame.transform.scale(balão, (260, 180))
            tela.blit(balão, (saguão_x + guardax4 - 10, saguão_y + guarday4 - 80))
            texto_fala = fonte2.render("Você não pode voltar", True, (0, 0, 0))
            texto_fala2 = fonte2.render("por aqui, há outra saída.", True, (0, 0, 0))
            tela.blit(texto_fala, (saguão_x + guardax4, saguão_y + guarday4 - 70))
            tela.blit(texto_fala2, (saguão_x + guardax4, saguão_y + guarday4 - 40))
            tempo_texto_guarda4 += 1
            if tempo_texto_guarda4 >= 240:
                parou_texto_guarda4 = True
                falando = False
                continuar_texto_guarda4 = False

        if hitbox_jogador.colliderect(hitboxway):
            falaway = True

        if falaway == True and tempo_fala_way <= 120:
            balão = pygame.transform.scale(balão, (150, 120))
            tela.blit(balão, (saguão_x + wayx - 10, saguão_y + wayy - 80))
            texto_fala_way = fonte2.render("Com licença.", True, (0, 0, 0))
            tela.blit(texto_fala_way, (saguão_x + wayx, saguão_y + wayy - 70))
            tempo_fala_way += 1

        if inicio_jogo_saguão >= 2280:
            falaway2 = True

        if falaway2 == True and tempo_fala_way2 <= 120:
            balão = pygame.transform.scale(balão, (130, 120))
            tela.blit(balão, (saguão_x + wayx - 10, saguão_y + wayy - 60))
            texto_fala_way = fonte2.render("Atenção.", True, (0, 0, 0))
            tela.blit(texto_fala_way, (saguão_x + wayx, saguão_y + wayy - 50))
            tempo_fala_way2 += 1

        if luz == False:
            preto = pygame.Rect((0, 0), (640, 480))
            pygame.draw.rect(superficie, (0, 0, 0, 200), preto)
            tela.blit(superficie, (0, 0))

        inicio_jogo_saguão += 1

        if inicio_jogo_saguão >= 1260 and começou_tempo <= 120:
            balão = pygame.transform.scale(balão, (130, 100))
            tela.blit(balão, (saguão_x + guardax1 - 10, saguão_y + guarday1 - 60))
            tela.blit(balão, (saguão_x + guardax2 - 10, saguão_y + guarday2 - 60))
            tela.blit(balão, (saguão_x + guardax3 - 10, saguão_y + guarday3 - 60))
            tela.blit(balão, (saguão_x + guardax4 - 10, saguão_y + guarday4 - 60))
            tela.blit(balão, (saguão_x + guardax5 - 10, saguão_y + guarday5 - 60))
            tela.blit(balão, (saguão_x + guardax6 - 10, saguão_y + guarday6 - 60))
            tela.blit(balão, (saguão_x + guardax7 - 10, saguão_y + guarday7 - 60))
            tela.blit(balão, (saguão_x + guardax8 - 10, saguão_y + guarday8 - 60))
            começou_texto = fonte2.render("Começou.", True, (0, 0, 0))
            tela.blit(começou_texto, (saguão_x + guardax1, saguão_y + guarday1 - 50))
            tela.blit(começou_texto, (saguão_x + guardax2, saguão_y + guarday2 - 50))
            tela.blit(começou_texto, (saguão_x + guardax3, saguão_y + guarday3 - 50))
            tela.blit(começou_texto, (saguão_x + guardax4, saguão_y + guarday4 - 50))
            tela.blit(começou_texto, (saguão_x + guardax5, saguão_y + guarday5 - 50))
            tela.blit(começou_texto, (saguão_x + guardax6, saguão_y + guarday6 - 50))
            tela.blit(começou_texto, (saguão_x + guardax7, saguão_y + guarday7 - 50))
            tela.blit(começou_texto, (saguão_x + guardax8, saguão_y + guarday8 - 50))
            começou_tempo += 1
            luz = True

        pygame.display.update()
        #mudar pra o certo pra trocar de tela
        if hitbox_jogador.colliderect(hitbox_parede_passar):
            resetar_jogo()
            olhando = 3
            menu = False
            opções = False
            jogo_iniciar = True
            saguão_menu = False

    #jogo iniciando de verdade
    while jogo_iniciar == True:
        clock.tick(fps)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        #fazendo o fim do tempo (perder)
        while inicio_jogo > final_jogo:
            clock.tick(fps)
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            texto = fonte.render("ACABOU O TEMPO", True, (255, 255, 255))
            tela.blit(texto, (150, 200))
            
            botão_reiniciar = pygame.Rect((235, 400), (150, 30))
            pygame.draw.rect(tela, (255, 0, 0), botão_reiniciar)
            pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                posicao_mouse = pygame.mouse.get_pos()
                if botão_reiniciar.collidepoint(posicao_mouse):
                    relogio_ativado = False
                    resetar_jogo()
        inicio_jogo += 1

        #fazendo a chegada final (ganhar)
        while Ganhar >= 200:
            clock.tick(fps)
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            texto = fonte.render("FINAL DA CORRIDA", True, (255, 255, 255))
            tela.blit(texto, (150, 200))

            botão_reiniciar = pygame.Rect((235, 400), (150, 30))
            pygame.draw.rect(tela, (255, 0, 0), botão_reiniciar)
            pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                posicao_mouse = pygame.mouse.get_pos()
                if botão_reiniciar.collidepoint(posicao_mouse):
                    relogio_ativado = False
                    resetar_jogo()
    
        #fazendo o fundo
        if fundo_1 == True:
            tela.blit(fundo, (X, Y))
            hitbox_paredefundo1 = pygame.Rect(X + 503, Y, 154, 1791)
            hitbox_paredefundo2 = pygame.Rect(X + 632, Y + 1792, 130, 255)
            hitbox_paredefundo22 = pygame.Rect(X + 632, Y + 1800, 135, 247)
            hitbox_paredefundo3 = pygame.Rect(X + 1024, Y, 119, 253)
            hitbox_paredefundo32 = pygame.Rect(X + 1028, Y + 232, 119, 23)
        else:
            hitbox_paredefundo1 = pygame.Rect(X, Y, 0, 0)
            hitbox_paredefundo2 = pygame.Rect(X, Y, 0, 0)
            hitbox_paredefundo22 = pygame.Rect(X, Y, 0, 0)
            hitbox_paredefundo3 = pygame.Rect(X, Y, 0, 0)
            hitbox_paredefundo32 = pygame.Rect(X, Y, 0, 0)

        if fundo_2 == True:
            tela.blit(fundo2, (fundo2_x, fundo2_y))
        
        if Y3 > 480:
            Y3 = 0
            Ganhar += 1
            
        if Y2 > 540 and Y <= 0:
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
        Y3 += Aumento / divisão
        Y2 += Aumento / divisão
        if Y <= 0 and fundo_1 == True:
            Y += Aumento / divisão
        if fundo2_y <= 0 and fundo_2 == True:
            fundo2_y += Aumento / divisão

        #fazendo a hitbox
        hitbox_cima = pygame.Rect(0, 0, 640, 280)

        hitbox_cima1 = pygame.Rect(0, 0, 640, 240)

        hitbox_cima2 = pygame.Rect(0, 0, 640, 190)

        hitbox_cima3 = pygame.Rect(0, 0, 640, 120)
        
        hitbox_jogador = pygame.Rect((personagem_x) - 3, (personagem_y) + 50, 70, 20)
        hitbox_jogador_inimigos2 = pygame.Rect(personagem_x, personagem_y, 64, 64)

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
            if Y <= 0:
                npc_y += Aumento / divisão

            npc_y2 -= 5
            if Y <= 0:
                npc_y2 += Aumento / divisão

            npc_y3 -= 1
            if Y <= 0:
                npc_y3 += Aumento / divisão

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
        if hitbox_jogador.colliderect(hitbox_cima) and Y <= 0:
            parou_cima = True
        else:
            parou_cima = False

        if hitbox_jogador.colliderect(hitbox_cima1) and Y <= 0:
            parou_cima1 = True
        else:
            parou_cima1 = False

        if hitbox_jogador.colliderect(hitbox_cima2) and Y <= 0:
            parou_cima2 = True
        else:
            parou_cima2 = False

        if hitbox_jogador.colliderect(hitbox_cima3) and Y <= 0:
            parou_cima3 = True
        else:
            parou_cima3 = False

        if hitbox_jogador.colliderect(hitbox_paredefundo1) or hitbox_jogador.colliderect(hitbox_paredefundo22):
            parou_esquerda = True
        else:
            parou_esquerda = False

        if hitbox_jogador.colliderect(hitbox_paredefundo2):
            parou_baixo = True
        else:
            parou_baixo = False

        if hitbox_jogador.colliderect(hitbox_paredefundo3):
            parou_direita = True
        else:
            parou_direita = False

        if personagem_y + 50 <= 0:
            fundo_1 = False
            fundo_2 = True
            npc_y = 300
            npc_y2 = 300
            npc_y3 = 300
            personagem_y = 410
            Aumento = 0
            Y = -10

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
            texto_tempo = fonte.render("Tempo: " + str(int(tempo_segundos/60)), True, (255, 255, 255))
            tela.blit(texto_tempo, (200, 50))
            tempo_texto = 0

    #    fazendo a barra de velocidade
    #    pygame.draw.rect(tela, (255, 0, 0), (BarraVermelha), 0)
    #    pygame.draw.rect(tela, (0, 255, 0), (BarraVerde), 0)

        #fazendo a outra dimensão ou sla oq e os monstros
        hitbox_monstro = pygame.Rect(200, monstro_y1 + 10, 64, 41)
        dimensão = pygame.Rect((dimensão_x, 0), (640, 480))

        monstro_y1 += Aumento / divisão
        if dimensão.contains(hitbox_monstro) and hit == False:
            tela.blit(monstro, (200, monstro_y1))
        if hitbox_jogador_inimigos2.colliderect(hitbox_monstro):
            hit = True
            divisão += 5
            monstro_y1 = Altura + 500

        pygame.draw.rect(superficie, (200, 0, 0, 128), dimensão)
        tela.blit(superficie, (0, 0))

        if dimensão_x < 0:
            dimensão_x += 0.5

    #    fazendo a barra de stamina
    #    pygame.draw.rect(tela, (255, 0, 0), (BarraVermelha2), 0)
    #    pygame.draw.rect(tela, (50, 50, 255), (BarraAzul2), 0)

        #definindo as teclas
        keys = pygame.key.get_pressed()

        #teclas para andar e pular correndo
        if pode_andar == False and Cansou == False:
            if keys[pygame.K_LEFT] and personagem_x > 0 and parou_esquerda == False:
                personagem_x -= 3

            if keys[pygame.K_RIGHT] and personagem_x < 640 - 64 and parou_direita == False:
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
        if Cansou == True and Aumento <= 0:
            bug1 = True
        if Cansou == False:
            bug1 = False
        if pode_andar == True or bug1 == True:
            if keys[pygame.K_LEFT] and personagem_x > 0 and parou_esquerda == False:
                personagem_x -= 1
            if keys[pygame.K_LEFT]:
                esquerda = True
                olhando = 1
            if not keys[pygame.K_LEFT]:
                esquerda = False

            if keys[pygame.K_RIGHT] and personagem_x < 640 - 64 and parou_direita == False:
                personagem_x += 1
            if keys[pygame.K_RIGHT]:
                direita = True
                olhando = 2
            if not keys[pygame.K_RIGHT]:
                direita = False

            bug2 = False
            if keys[pygame.K_UP] and parou_cima == False and parou_cima01 == False:
                personagem_y -= 1
            if keys[pygame.K_UP] and parou_cima == True and inicio_jogo >= 300 and parou_cima01 == False:
                Aumento = 10
                bug2 = True
            if keys[pygame.K_UP]:
                cima = True
                olhando = 3
            if not keys[pygame.K_UP]:
                cima = False

            if keys[pygame.K_DOWN] and personagem_y < 410 and parou_baixo == False:
                personagem_y += 1
            if keys[pygame.K_DOWN]:
                baixo = True
                olhando = 0

            if keys[pygame.K_DOWN] and personagem_y >= 410 and fundo_1 == True and Y > -1408:
                Aumento = -10
            if Aumento < 0 and fundo_1 == True and not(keys[pygame.K_DOWN] and personagem_y >= 410 and fundo_1 == True and Y > -1408):
                Aumento = 0

            if keys[pygame.K_DOWN] and personagem_y >= 410 and fundo_2 == True and fundo2_y > -2080:
                Aumento = -10
            if Aumento < 0 and fundo_2 == True and not(keys[pygame.K_DOWN] and personagem_y >= 410 and fundo_2 == True and fundo2_y > -2080):
                Aumento = 0

            if not keys[pygame.K_DOWN]:
                baixo = False

        #fazendo o personagem correr
        if inicio_jogo >= 300:
            if Cansou == False:
                if keys[pygame.K_z] and not keys[pygame.K_x] and liberado == True and parou_cima01 == False:
                    aumentar = True
                    liberado = False
                    liberado2 = False
                    tempo_2 = pygame.time.get_ticks()
                    tempo_4 = pygame.time.get_ticks()
                    if pular == 0:
                        olhando = 4

                if keys[pygame.K_x] and not keys[pygame.K_z] and liberado == False and parou_cima01 == False:
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
                if parou_cima == False and Y <= 0:
                    personagem_y -= Aumento2//2

                if parou_cima1 == False and Aumento > 50 and Y <= 0:
                    personagem_y -= Aumento2//2

                if parou_cima2 == False and Aumento > 100 and Y <= 0:
                    personagem_y -= Aumento2//2

                if parou_cima3 == False and Aumento > 150 and Y <= 0:
                    personagem_y -= Aumento2//2
                if Y >= 0:
                    personagem_y -= Aumento2
                
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
            if Aumento > 0 and personagem_y <= 230 and Y <= 0:
                personagem_y += 2
            if Aumento > 0 and personagem_y > 230 and personagem_y < 410 and Y <= 0:
                personagem_y += 1
            BarraVerde = 15, 10, Aumento, 50
            if Aumento == 0:
                Aumento2 = 0

        if Cansou == False:
            if Aumento == 0:
                pode_andar = True

        #fazendo a barra de stamina regenerar
        if Aumento_Contrario < 176 and (Aumento <= 0 or bug2 == True):
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
    
