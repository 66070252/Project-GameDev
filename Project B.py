#import function
import pygame
import os
import time
import random
pygame.font.init()

#Screen
width, height = 750, 750
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Space Ship War")

#Enemy images
Red_ship = pygame.Surface((20,20))
Red_ship.fill((255,0,0))
Green_ship = pygame.Surface((20,20))
Green_ship.fill((0,255,0))
Blue_ship = pygame.Surface((20,20))
Blue_ship.fill((0,0,255))

#Player images
Player_ship = pygame.Surface((20,20))
Player_ship.fill((255,255,255))

#Bullet
Bullet = pygame.Surface((3,20))
Bullet.fill((255,0,0))

#Player character
class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y, 50, 50))

#Background
BG = pygame.transform.scale \
    (pygame.image.load(os.path.join("BG.jpg")), (width,height))

#Game start
def main():
    run = True
    FPS = 60
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)
    clock = pygame.time.Clock()
    ship = Ship(300, 650)
    ship_speed = 5

    #Screen
    def draw():
        screen.blit(BG, (0,0))
        #text
        live_label = main_font.render(f"lives: {lives}", 1, (255,255,255))
        level_label = main_font.render(f"level: {level}", 1, (255,255,255))
        #draw text
        screen.blit(live_label, (10, 10))
        screen.blit(level_label, (width - level_label.get_width() - 10, 10))

        ship.draw(screen)

        pygame.display.update()

    #Make game run while loop
    while run:
        clock.tick(60)
        draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        #Control
        key = pygame.key.get_pressed()
        if key[pygame.K_a] and ship.x - ship_speed > 0:
            ship.x -= ship_speed
        if key[pygame.K_w] and ship.y - ship_speed > 0:
            ship.y -= ship_speed
        if key[pygame.K_s] and ship.y + ship_speed + 50 < height:
            ship.y += ship_speed
        if key[pygame.K_d] and ship.x + ship_speed + 50 < width:
            ship.x += ship_speed
main()
