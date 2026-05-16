import pygame

pygame.init()

LARGURA = 640
ALTURA = 480

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Quadrado que move")

fundo = (0, 0, 0)

verde = (0, 255, 0)
vermelho = (255, 0, 0)
azul = (0,0,255)

cor = verde

x = LARGURA // 2
y = ALTURA // 2

tamanho = 50
velocidade = 1

running = True

while running:
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            running = False

        # Detecta o clique da tecla SPACE
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:

                # Troca entre verde e vermelho
                if cor == verde:
                    cor = vermelho

                else:
                    cor = verde



    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= velocidade

    if keys[pygame.K_RIGHT]:
        x += velocidade

    if keys[pygame.K_UP]:
        y -= velocidade

    if keys[pygame.K_DOWN]:
        y += velocidade

    # Limites da tela
    if x < 0:
        x = 0

    if x > LARGURA - tamanho:
        x = LARGURA - tamanho

    if y < 0:
        y = 0

    if y > ALTURA - tamanho:
        y = ALTURA - tamanho

    tela.fill(fundo)

    pygame.draw.circle(tela, cor, (x, y), 40)

    pygame.display.flip()

pygame.quit()