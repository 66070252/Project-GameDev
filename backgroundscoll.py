import pygame
import math

pygame.init()

clock = pygame.time.Clock()
FPS = 60

Width = 750
Height = 750

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Endless Scroll")

bg = pygame.image.load('Images/background.png').convert()
bg_height = bg.get_height()
bg = pygame.transform.scale (bg, (Width, bg_height))
bg_rect = bg.get_rect()

scroll = 0
tiles = math.ceil(Height / bg_height) + 2

run = True
while run:
    
    clock.tick(FPS)

    for i in range(tiles):
        screen.blit(bg, (0,i * bg_height + scroll - bg_height))

    scroll += 5

    if abs(scroll) > bg_height:
        scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()