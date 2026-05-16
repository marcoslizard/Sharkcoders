import pygame

pygame.init()

LARGURA = 640
ALTURA = 480

tela = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption("Quadrado que move")

fundo = (200,200,200)

x = LARGURA // 2
y = ALTURA // 2

tamanho = 50

velocidade = 1

running = True
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= velocidade
    if keys[pygame.K_RIGHT]:
        x += velocidade
    if keys[pygame.K_UP]:
        y -= velocidade
    if keys[pygame.K_DOWN]:
        y += velocidade

    if x <0:
        x = 0
    if x > LARGURA - tamanho :
        x = LARGURA - tamanho
    if y <0:
        y = 0

    if y > ALTURA - tamanho:
        y= ALTURA - tamanho

    tela.fill(fundo)
    pygame.draw.rect(tela,(255,0,0),(x,y,tamanho,tamanho))
    pygame.display.flip()

pygame.quit()