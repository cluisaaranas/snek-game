import pygame

pygame.init()

window = pygame.display.set_mode((2500,1000))
window.fill((0,0,0))
pygame.display.set_caption("something")

player = pygame.surface.Surface((50, 50))
player.fill((0,255,10))
player_x = 100
player_y = 100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player_x -= 50
            if event.key == pygame.K_d:
                player_x += 50
            if event.key == pygame.K_w:
                player_y -= 50
            if event.key == pygame.K_s:
                player_y += 50
    window.fill((0,0,0))
    window.blit(player, (player_x, player_y))
    pygame.display.flip()