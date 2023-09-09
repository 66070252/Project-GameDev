import pygame, sys

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50,50))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect(center = (screen_width/2,screen_height/2))
    
    def update(self):
        self.rect.center = pygame.mouse.get_pos()

pygame.init()
clock = pygame.time.Clock()
screen_width, screen_height = 400,400
screen = pygame.display.set_mode((screen_width,screen_height))

player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill((30,30,30))
    player_group.draw(screen)
    player_group.update()
    pygame.display.flip()
    clock.tick(30)
