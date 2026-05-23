import pygame, random, math, os

pygame.int()
W, H = 800, 600
win = pygame.display.set_mode((W, H))

pygame.display.set_caption("Mini Asteroids Expandido")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)

HIGHSCORE_FILE = "highscore.txt"
if os.path.exists(HIGHSCORE_FILE):
    with open(HIGHSCORE_FILE, "r") as f:
        highscore = int(f.read())
else:
    highscore = 0

running = True
spawn_timer = 0
spawn_interval = 3000
last_powerup = 0
powerup_interval = 10000

while running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if game_state == STATE_MENU and event.key == pygame.K_RETURN:
                reset_game()
                game_state = STATE_GAME
            elif game_state == STATE_GAMEOVER and event.key == pygame.K_RETURN:
                reset_game()
                game_state = STATE_GAME

    keys = pygame.key.get_pressed()
