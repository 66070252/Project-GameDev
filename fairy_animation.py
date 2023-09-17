#import function
import pygame
pygame.init()

Width = 100
Height = 100
black = (0, 0, 0)
fps = 60
screen = pygame.display.set_mode([Width, Height])
pygame.display.set_caption('Fairy')
timer = pygame.time.Clock()
frames = ['images/New_fairy_sprite1_1.png', 'images/New_fairy_sprite1_2.png', 'images/New_fairy_sprite1_3.png']

active_frame = 0
mode = 0
count = 0

def update_fairy(mod, counter):
    if counter >=  60:
        counter = 0
    if mod == 0:
        if counter < 20:
            act = 0
        if 20 <= counter < 40:
            act = 1
        if 40 <= counter < 60:
            act = 2
    counter += 1
    return act, counter



running = True
while running:
    timer.tick(fps)
    screen.fill(black)
    active_frame, count = update_fairy(mode, count)
    fairy = pygame.transform.scale(pygame.image.load(frames[active_frame]), (50, 50))
    screen.blit(fairy, (50, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame. display.flip()
pygame.quit()
