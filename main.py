import pygame
from sys import exit

pygame.init()
pygame.display.set_caption('First One')
clock = pygame.time.Clock()
font = pygame.font.Font('font\Pixeltype.ttf', 50)
screen = pygame.display.set_mode((800, 400))

sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
text_surface = font.render('to escrevendo', False, 'Gray')

snail_surface = pygame.image.load('graphics/snail/snail1.png')
snail_x_pos = 600


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        screen.blit(text_surface, (300, 50))

        snail_x_pos -= 5
        screen.blit(snail_surface, (snail_x_pos, 250))

        if snail_x_pos < -100:
            snail_x_pos = 800
    pygame.display.update()
    clock.tick(600)
