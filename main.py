import pygame
import random
# inicia um jogo
pygame.init()
# cria o a tela  800 é o eixo x e 600 o eixo y
tela = pygame.display.set_mode((800, 600))

# titulo
pygame.display.set_caption("Space Invaders!")
# icone
icon = pygame.image.load("space-ship (1).png")
pygame.display.set_icon(icon)
#background
background = pygame.image.load("Prancheta 1.png")
# imagem do jogador
jogador_imagem = pygame.image.load("spaceship.png")
# definindo os eixos que a imagem irá aparecer
eixox = 370
eixoy = 450
variacao = 0

inimigo_imagem = pygame.image.load("alien.png")
inimigox = random.randint(0,800)
inimigoy = random.randint(50,150)
variacao_inimigox = 2.5
variacao_inimigoy = 30
def jogador(x, y):
    # define a imagem e seus eixos
    tela.blit(jogador_imagem, (x, y))

def inimigo(x,y):
    tela.blit(inimigo_imagem, (x,y))
# game loop
running = True
while running:
    # Red, Green, Blue cores em respectivas posições que vao ate 255.A tela deve ser colorida antes para nãosobescrever as outras imagens
    tela.fill((0, 30, 30))
    tela.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                variacao = - 5
            if event.key  == pygame.K_RIGHT:
                variacao = 5
        if event.type == pygame.KEYUP:
            variacao = 0
        #verifica o evento de uma tecla ser pressionada ou não, depois verifica se sao as setas. caso sim, move a nave
        if event.type == pygame.QUIT:
            running = False
    eixox += variacao
    if eixox <= 0:
        eixox = 0
    if eixox >= 734:
        eixox = 734

    inimigox += variacao_inimigox
    if inimigox <= 0:
        variacao_inimigox = 4
        inimigoy += variacao_inimigoy
    if inimigox >= 734:
        variacao_inimigox = -4
        inimigoy += variacao_inimigoy

    jogador(eixox, eixoy)
    inimigo(inimigox,inimigoy)

    # é necessário dar uptade
    pygame.display.update()
