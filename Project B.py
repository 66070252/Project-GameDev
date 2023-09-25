#import function
import pygame, os, time, random, math, json
pygame.font.init()

#Screen
width, height = 750, 750
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Space Ship War")

#Enemy images
Red_ship = pygame.image.load(os.path.join("Images", "Red_Enemy.png"))
Green_ship = pygame.image.load(os.path.join("Images", "Green_Enemy.png"))
Blue_ship = pygame.image.load(os.path.join("Images", "Blue_Enemy.png"))

#Player images
Player_ship = pygame.image.load(os.path.join("Images", "player_ship.png"))

#Player Bullet
Bullet = pygame.Surface((3,20))
Bullet.fill((255,255,255))

#Enemy Bullet
Enemy_Bullet = pygame.Surface((3,20))
Enemy_Bullet.fill((225,255,255))

#Create every character
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
        window.blit(self.ship_img, (self.x, self.y))
    
    def get_width(self):
        return self.ship_img.get_width()
    
    def get_height(self):
        return self.ship_img.get_height()

#Player character
class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = Player_ship
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

#Enemy Ship
class Enemy(Ship):
    COLOR_MAP = {
                "red": (Red_ship),
                "green": (Green_ship),
                "blue": (Blue_ship)
                }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
    
    #Move vertical line
    def move(self, vel):
        self.y += vel

#Background
BG = pygame.transform.scale \
    (pygame.image.load(os.path.join("Images", "BG.png")), (width,height))

#Game start
def main():
    run = True
    FPS = 60
    level = 0
    score = 1
    lost = False
    lost_count = 0
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)
    clock = pygame.time.Clock()
    player = Player(300, 650)
    ship_speed = 5
    enemies = []
    wave_length = 5
    enemy_val = 1

    #Screen
    def draw():
        screen.blit(BG, (0,0))
        
        #text
        score_label = main_font.render(f"score: {score}", 1, (255,255,255))
        level_label = main_font.render(f"level: {level}", 1, (255,255,255))
        
        #Draw text
        screen.blit(score_label, (10, 10))
        screen.blit(level_label, (width - level_label.get_width() - 10, 10))

        #Draw Eney
        for enemy in enemies:
            enemy.draw(screen)

        #Draw Player
        player.draw(screen)

        #Appear text when you lose
        if lost:
            lost_label = lost_font.render("You lose!!", 1, (255,255,255))
            screen.blit(lost_label, (width/2 - lost_label.get_width()/2, 350))

        pygame.display.update()

    #Make game run while loop
    while run:
        clock.tick(FPS)
        draw()

        if score <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

        #You lose
        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue

        #Level of stage
        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, width-100), random.randrange(-1500, -100), \
                              random.choice(["red", "green", "blue"]))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        #Control
        key = pygame.key.get_pressed()
        if key[pygame.K_a] and player.x - ship_speed > 0:
            player.x -= ship_speed
        if key[pygame.K_w] and player.y - ship_speed > 0:
            player.y -= ship_speed
        if key[pygame.K_s] and player.y + ship_speed + player.get_height() < height:
            player.y += ship_speed
        if key[pygame.K_d] and player.x + ship_speed + player.get_width() < width:
            player.x += ship_speed

        #Enemy move
        for enemy in enemies:
            enemy.move(enemy_val)
            if enemy.y + enemy.get_height() > height:
                score -= 1
                enemies.remove(enemy)

main()
