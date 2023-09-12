import pygame, sys, random
#This create Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30,30))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect(center = (screen_width/2,screen_height/2))
    
    # Control follow cersor mouse
    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def create_bullet(self):
        return Bullet(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])

#This create Bullet
class Bullet(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.image = pygame.Surface((4,30))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(center = (pos_x,pos_y))

    def update(self):
        self.rect.y -= 5

# This is enemy sprites
class Enemy(pygame.sprite.Sprite):
    """
    Spawn an enemy
    """
    def __init__(self, x, y,type_):
        super(Enemy, self).__init__()

        self.type = type_
        self.image_list = []
        for i in range(1):
            if type_ == 1:
                img = pygame.image.load(f'Desktop/group project/small enemy 1-{i+1}.png')
            img = pygame.transform.scale(img, (50, 50))
            self.image_list.append(img)
        
        self.index = 0
        self.image = self.image_list[self.index]
        self.rect = self.image.get_rect(center=(x, y))

        self.counterr = 0
        self.speed = 3
    def uptade(self, moving_left, moving_right):
        self.rect.y += self.speed

#This section is Screen when run and add sumethings
pygame.init()
clock = pygame.time.Clock()
screen_width, screen_height = 400,600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.mouse.set_visible(False)

player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

bullet_group = pygame.sprite.Group()

enemy = Enemy(144, 80, 1)
smallenemy_group = pygame.sprite.Group()
smallenemy_group.add(enemy)

#This section is run game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullet_group.add(player.create_bullet())

    #Drawing
    screen.fill((30,30,30))
    player_group.draw(screen)
    bullet_group.draw(screen)
    smallenemy_group.draw(screen)
    player_group.update()
    bullet_group.update()
    smallenemy_group.update()
    pygame.display.flip()
    clock.tick(120)
