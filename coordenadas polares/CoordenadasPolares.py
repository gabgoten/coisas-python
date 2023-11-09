# Este programa tem o propósito de exemplificar o uso de Coordenadas Polares

import pygame
from pygame.locals import *
import math

def DesenhaFundo():
    tela.fill(CorTela)
    pygame.draw.line(tela, (0, 0, 0), (0, yIni), (TamTela[0]-1, yIni), 1)
    pygame.draw.line(tela, (0, 0, 0), (xIni, 0), (xIni, TamTela[1]-1), 1)

def NovaBola(posFinal):
    raio = 12
    cor = (0, 127, 255)
    xFim = posFinal[0]
    yFim = posFinal[1]
    distFim = ( (xFim - xIni)**2 + (yFim - yIni)**2 ) ** 0.5 # calcula a distância entre o centro da tela o o ponto clicado
    angulo = math.acos((xFim - xIni) / distFim) # calcula o ângulo da reta que passa pelo centro da tela e pelo ponto clicado
    if yFim > yIni:
        angulo = 2*PI - angulo # ajuste do ângulo para a parte inferior do quadro de desenho
    distAtual = 0 # variável a ser usada para o local efetivo do desenho da bolinha - começa no centro e vai até a posFinal
    passo = 0.1 # este passo define a velocidade da bolinha
    #           0         1     2    3        4       5          6      7  
    novabola = [posFinal, raio, cor, distFim, angulo, distAtual, passo, False]
    Bolas.append(novabola)


def DesenhaBolas(B):
    for i in range(len(B)):
        if B[i][5] <= B[i][3]: # distAtual <= distFim      se ainda não chegou ao final aumenta a distância
            B[i][5] += B[i][6] # soma o passo à distAtual
        else:
            B[i][7] = True
        X = xIni + int(B[i][5] * math.cos(B[i][4]))      # calcula coordenada X da nova posição da bolinha
        Y = yIni - int(B[i][5] * math.sin(B[i][4]))      # calcula coordenada Y da nova posição da bolinha
        pygame.draw.circle(tela, B[i][2], (X, Y), B[i][1], 0) # desenha a bolinha na nova posição

def RemoveBolas(B):
    i = 0
    while i < len(B):
        if B[i][7]:
            del(B[i])
        else:
            i = i + 1

# Parte principal do programa

# Parâmetros iniciais
PI = math.acos(-1)  # define o valor de PI
TamTela = (800, 600)
CorTela = (200, 255, 200)
xIni = TamTela[0] // 2
yIni = TamTela[1] // 2
Bolas = []

pygame.init() 
tela = pygame.display.set_mode(TamTela, 0, 32)
pygame.display.set_caption('Geometria – uma bolinha se desloca do centro até o ponto do clique do mouse')

fim = False
while not fim:
    DesenhaFundo()
    DesenhaBolas(Bolas)
    pygame.display.update()
    #RemoveBolas(Bolas)


    for evento in pygame.event.get(): 
        if evento.type == QUIT:        
            fim = True
        elif evento.type == KEYDOWN:
            if evento.key == K_ESCAPE:
                fim = True
        elif evento.type == MOUSEBUTTONDOWN:
            botoesMouse = pygame.mouse.get_pressed()
        elif evento.type == MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if botoesMouse[0]:
                NovaBola(pos)
          

pygame.display.quit() 


print("Fim do programa")

