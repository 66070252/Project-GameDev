#import function
import pygame, os, time, random, math, json
pygame.font.init()

#Screen
width, height = 750, 750
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("ShipHi!")

#Enemy images
Red_ship = pygame.image.load(os.path.join("Images", "Red_Enemy.png"))
Green_ship = pygame.image.load(os.path.join("Images", "Green_Enemy.png"))
Blue_ship = pygame.image.load(os.path.join("Images", "Blue_Enemy.png"))

#Player images
Player_ship = pygame.image.load(os.path.join("Images", "player_ship.png"))

#Player Bullet
Player_bullet = pygame.Surface((3,20))
Player_bullet.fill((0,255,0))

#Enemy Bullet
Enemy_bullet = pygame.Surface((3,20))
Enemy_bullet.fill((255,0,0))

#Create Bullet
class Bullet:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel
        
    def off_screen(self, height):
        return not(self.y <= height and self.y >= 0)
        
    def collision(self, obj):
        return collide(self, obj)

#Create every character
class Ship:
    COOLDOWN = 30

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.bullet_img = None
        self.bullets = []
        self.cool_down_counter = 0

    def move_bullet(self, vel, obj):
        self.cooldown()
        for bullet in self.bullets:
            bullet.move(vel)
            if bullet.off_screen(height):
                self.bullets.remove(bullet)
            elif bullet.collision(obj):
                obj.health -= 10
                self.bullets.remove(bullet)

    def draw(self, screen):
        screen.blit(self.ship_img, (self.x, self.y))
        for bullet in self.bullets:
            bullet.draw(screen)

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            bullet = Bullet(self.x, self.y, self.bullet_img)
            self.bullets.append(bullet)
            self.cool_down_counter = 1
    
    def get_width(self):
        return self.ship_img.get_width()
    
    def get_height(self):
        return self.ship_img.get_height()

#Player character
class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = Player_ship
        self.bullet_img = Player_bullet
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health
  
    def move_bullet(self, vel, objs):
        self.cooldown()
        for bullet in self.bullets:
            bullet.move(vel)
            if bullet.off_screen(height):
                self.bullets.remove(bullet)
            else:
                for obj in objs:
                    if bullet.collision(obj):
                        objs.remove(obj)
                        self.bullets.remove(bullet)

#Enemy Ship
class Enemy(Ship):
    COLOR_MAP = {
                "red": (Red_ship, Enemy_bullet),
                "green": (Green_ship, Enemy_bullet),
                "blue": (Blue_ship, Enemy_bullet)
                }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.bullet_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
    
    #Move vertical line
    def move(self, vel):
        self.y += vel

#Background
BG = pygame.transform.scale \
    (pygame.image.load(os.path.join("Images", "BG.png")), (width,height))

#Collider to check hit box
def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

#Game start
def main():
    run = True
    FPS = 60
    level = 0
    live = 1
    lost = False
    lost_count = 0
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)
    clock = pygame.time.Clock()
    player = Player(300, 650)
    ship_speed = 5
    bullet_speed = 4
    enemies = []
    wave_length = 5
    enemy_val = 1

    #Screen
    def draw():
        screen.blit(BG, (0,0))
        
        #text
        live_label = main_font.render(f"live: {live}", 1, (255,255,255))
        level_label = main_font.render(f"level: {level}", 1, (255,255,255))
        
        #Draw text
        screen.blit(live_label, (10, 10))
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

        if live <= 0 or player.health <= 0:
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
        if key[pygame.K_SPACE]:
            player.shoot()

        #Enemy move and remove
        for enemy in enemies:
            enemy.move(enemy_val)
            enemy.move_bullet(bullet_speed, player)
            if enemy.y + enemy.get_height() > height:
                score -= 1
                enemies.remove(enemy)
        
        player.move_bullet(-bullet_speed, enemies)
main()
