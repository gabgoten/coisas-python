import pygame
import random

# Definindo algumas constantes
WIDTH = 600
HEIGHT = 600
PLAYER_SIZE = 50
ENEMY_SIZE = 20
PLAYER_SPEED = 5
ENEMY_SPEED = 3
FPS = 60

# Definindo as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Inicializando o pygame
pygame.init()

# Criando a janela do jogo
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo da nave")

# Criando o jogador
player = pygame.Rect(WIDTH / 2 - PLAYER_SIZE / 2, HEIGHT - PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE)
player_color = BLUE

# Criando a bala do jogador
bullet = None
bullet_color = RED

# Criando uma lista de inimigos
enemies = []

# Função para criar inimigos
def create_enemy():
    enemy_x = random.randint(0, WIDTH - ENEMY_SIZE)
    enemy_y = random.randint(-HEIGHT, 0)
    enemy_type = random.choice(['red', 'blue'])
    if enemy_type == 'red':
        enemy_color = RED
    else:
        enemy_color = BLUE
    enemy = {'rect': pygame.Rect(enemy_x, enemy_y, ENEMY_SIZE, ENEMY_SIZE),
             'type': enemy_type,
             'color': enemy_color}
    return enemy

# Adicionando os primeiros inimigos à lista
for i in range(5):
    enemy = create_enemy()
    enemies.append(enemy)

# Iniciando o relógio do jogo
clock = pygame.time.Clock()

# Loop principal do jogo
while True:
    # Lidando com os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and bullet is None:
                bullet = pygame.Rect(player.centerx - 5, player.top - 10, 10, 10)
                bullet_color = RED
            elif event.button == 3 and bullet is None:
                bullet = pygame.Rect(player.centerx - 5, player.top - 10, 10, 10)
                bullet_color = BLUE

    # Movimentando o jogador
    mouse_pos = pygame.mouse.get_pos()
    player.centerx = mouse_pos[0]
    player.bottom = 550

    # Movimentando a bala do jogador
    if bullet is not None:
        bullet.y -= 10
        if bullet.y < 0:
            bullet = None

    # Movimentando os inimigos
    for enemy in enemies:
        enemy_rect = enemy['rect']
        enemy_type = enemy['type']
        enemy_color = enemy['color']
        enemy_rect.y += ENEMY_SPEED
        if enemy_rect.y > HEIGHT:
            enemies.remove(enemy)
            new_enemy = create_enemy()
            enemies.append(new_enemy)

    # Verificando colisão entre a bala e os inimigos
    if bullet is not None:
        for enemy in enemies:
            if bullet.colliderect(enemy['rect']) and bullet_color == enemy['color']:
                enemies.remove(enemy)
                bullet = None
                break


    # Desenhando os elementos na tela
    screen.fill(WHITE)
    pygame.draw.rect(screen, player_color, player)
    if bullet is not None:
        pygame.draw.ellipse(screen, bullet_color, bullet)
    for enemy in enemies:
        enemy_rect = enemy['rect']
        enemy_color = enemy['color']
        pygame.draw.rect(screen, enemy_color, enemy_rect)

    # Atualizando a tela
    pygame.display.update()

    # Limitando o FPS
    clock.tick(FPS)

# Encerrando o Pygame
pygame.quit()