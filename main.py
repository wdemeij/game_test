import pygame
from sys import exit


pygame.init() # starts pygame bascically. Makes it possible to run other functionalities
screen = pygame.display.set_mode((800, 400)) # Display surfce, tuple[width, heigth]
pygame.display.set_caption('Runner') # Name of the screen window
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('My game', False, 'black')

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_xpos = 600
snail_rect = snail_surf.get_rect(midbottom = (snail_xpos, 300))


player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))

while True:
    for event in pygame.event.get(): # Event loop
        if event.type == pygame.QUIT: # if you press the X button, loop breaks
            pygame.quit() # shuts down pygame, opposite of pygame.init()
            exit() # Quits all code 

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))
    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800
    screen.blit(snail_surf, snail_rect)
    screen.blit(player_surf, player_rect)

    pygame.display.update() # updates the display surface
    clock.tick(60) # says that the while loop should not run faster than 60 times per second (max framerate) 
