import pygame

pygame.init()
tela = pygame.display.set_mode((640,480))
pygame.display.set_caption("Minha Primeira Janela Pygame")

fundo = (30, 30, 30)
running = True

while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False


    tela.fill((0,0,0))
    pygame.draw.rect(tela,(255,0,0),(50,50,100,80)) # Superfície, cor , (posx, posy, sizex, sizey)
    pygame.draw.circle(tela,(0,255,0),(320,240),40) #Superfície, cor, raio
    pygame.draw.line(tela,(0,0,255),(0,0),(640,480),3) #superfície,cor,(inx,iny),(fimx,fimy), espessura



    #Teclas pressionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel

    if keys[pygame.K_RIGHT]:
        x += vel
    if keys [pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    pygame.display.flip()

    tela.fill(fundo)


pygame.quit()