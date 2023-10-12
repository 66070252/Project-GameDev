import pygame
import random
import time
from math import sqrt

#Normal Setting Ready to draw it
pygame.init()

display_width = 800
display_height = 600

fix_width = display_width/800
fix_height = display_height/600

black = (0,0,0)
white = (255,255,255)

gray = (55,55,55)
pink = (200,50,180)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

brightblue = (100,100,255)

darkred = (200,0,0)
darkgreen = (0,200,0)
darkblue = (0,0,200)

yellow = (255,255,0)

savefile_opened_or_created = list()

background_color1 = (255,255,255)
background_color2 = (0,0,255)

#Text
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('ShipHi!')
clock = pygame.time.Clock()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def text_objects_blue(text, font):
    textSurface = font.render(text, True, blue)
    return textSurface, textSurface.get_rect()

#Running game
def game_intro():
    game_loop()

#Keep Game still running
def game_loop():
    
    choose_difficulty = True

    left_clicked = True

    #Choose difficulty
    while choose_difficulty:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        gameDisplay.fill(white)

        largeText = pygame.font.Font('freesansbold.ttf', 50)
        TextSurf, TextRect = text_objects("Difficulty", largeText)
        TextRect.center = ((display_width/2),(display_height/7))
        gameDisplay.blit(TextSurf, TextRect)

        largeText = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = text_objects("HINT: To win you need to dodge the bullet and wait until time pass to 40", largeText)
        TextRect.center = ((display_width/2),(display_height*(7/8)))
        gameDisplay.blit(TextSurf, TextRect)

        mouse_pos = pygame.mouse.get_pos()
        x_mouse = mouse_pos[0]
        y_mouse = mouse_pos[1]
        
        mouse_pressed = pygame.mouse.get_pressed()

        if x_mouse > 150*fix_width and x_mouse < 250*fix_width and y_mouse > 175*fix_height and y_mouse < 225*fix_height:
            pygame.draw.rect(gameDisplay, green,(150*fix_width, 175*fix_height, 100*fix_width, 50*fix_height))
            if mouse_pressed[0] == 1 and left_clicked == False:
                difficulty = 'easy'
                choose_difficulty = False
                
        else:
            pygame.draw.rect(gameDisplay, darkgreen,(150*fix_width, 175*fix_height, 100*fix_width, 50*fix_height))

        if x_mouse > 350*fix_width and x_mouse < 450*fix_width and y_mouse > 175*fix_height and y_mouse < 225*fix_height:
            pygame.draw.rect(gameDisplay, green,(350*fix_width, 175*fix_height, 100*fix_width, 50*fix_height))
            if mouse_pressed[0] == 1 and left_clicked == False:
                difficulty = 'normal'
                choose_difficulty = False
                
        else:
            pygame.draw.rect(gameDisplay, darkgreen,(350*fix_width, 175*fix_height, 100*fix_width, 50*fix_height))

        if x_mouse > 550*fix_width and x_mouse < 650*fix_width and y_mouse > 175*fix_height and y_mouse < 225*fix_height:
            pygame.draw.rect(gameDisplay, green,(550*fix_width, 175*fix_height, 100*fix_width, 50*fix_height))
            if mouse_pressed[0] == 1 and left_clicked == False:
                difficulty = 'hard'
                choose_difficulty = False
        else:
            pygame.draw.rect(gameDisplay, darkgreen,(550*fix_width, 175*fix_height, 100*fix_width, 50*fix_height))

        if x_mouse > 250*fix_width and x_mouse < 350*fix_width and y_mouse > 375*fix_height and y_mouse < 425*fix_height:
            pygame.draw.rect(gameDisplay, green,(250*fix_width, 375*fix_height, 100*fix_width, 50*fix_height))
            if mouse_pressed[0] == 1 and left_clicked == False:
                difficulty = 'very hard'
                choose_difficulty = False
                
        else:
            pygame.draw.rect(gameDisplay, darkgreen,(250*fix_width, 375*fix_height, 100*fix_width, 50*fix_height))

        if x_mouse > 450*fix_width and x_mouse < 550*fix_width and y_mouse > 375*fix_height and y_mouse < 425*fix_height:
            pygame.draw.rect(gameDisplay, green,(450*fix_width, 375*fix_height, 100*fix_width, 50*fix_height))
            if mouse_pressed[0] == 1 and left_clicked == False:
                difficulty = 'extreme'
                choose_difficulty = False

        else:
            pygame.draw.rect(gameDisplay, darkgreen,(450*fix_width, 375*fix_height, 100*fix_width, 50*fix_height))

        if left_clicked == False and mouse_pressed[0] == 1:
            left_clicked = True
        elif left_clicked == True and mouse_pressed[0] == 0:
            left_clicked = False

        smallText = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = text_objects("EASY", smallText)
        TextRect.center = ((200*fix_width),(200*fix_height))
        gameDisplay.blit(TextSurf, TextRect)

        smallText = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = text_objects("NORMAL", smallText)
        TextRect.center = ((400*fix_width),(200*fix_height))
        gameDisplay.blit(TextSurf, TextRect)

        smallText = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = text_objects("HARD", smallText)
        TextRect.center = ((600*fix_width),(200*fix_height))
        gameDisplay.blit(TextSurf, TextRect)

        smallText = pygame.font.Font('freesansbold.ttf', 15)
        TextSurf, TextRect = text_objects("VERY HARD", smallText)
        TextRect.center = ((300*fix_width),(400*fix_height))
        gameDisplay.blit(TextSurf, TextRect)

        smallText = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = text_objects("EXTREME", smallText)
        TextRect.center = ((500*fix_width),(400*fix_height))
        gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(60)

    #Player movement and speed
    x_player = display_height // 2
    y_player = display_width // 2
    speed_player = 5

    gameExit = False

    game_over = False

    restart = False

    player_time = 120
    time = 0

    #Collect Bullet Ready to add pattern
    x_bullet = list()
    y_bullet = list()
    x_bullet_speed = list()
    y_bullet_speed = list()
    bullet_color = list()

    x_bullet_type_2 = list()
    y_bullet_type_2 = list()
    x_bullet_type_2_speed = list()
    y_bullet_type_2_speed = list()
    bullet_type_2_color = list()

    x_bullet_type_3 = list()
    y_bullet_type_3 = list()
    x_bullet_type_3_speed = list()
    y_bullet_type_3_speed = list()
    bullet_type_3_color = list()

    x_yellow_enemie = list()
    y_yellow_enemie = list()

    x_green_enemie = list()
    y_green_enemie = list()

    x_red_enemie = list()
    y_red_enemie = list()

    x_blue_enemie = list()
    y_blue_enemie = list()

    yellow_time = 90
    green_time = 0

    bullet_time = 0

    #Running and drawing a whole game
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and x_player - speed_player > 0:
            x_player -= speed_player
        if keys[pygame.K_d] and x_player + speed_player < display_width:
            x_player += speed_player
        if keys[pygame.K_w] and y_player - speed_player > 0:
            y_player -= speed_player
        if keys[pygame.K_s] and y_player + speed_player < display_height:
            y_player += speed_player

        mouse_pressed = pygame.mouse.get_pressed()
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        gameDisplay.fill(white)

        mouse_pressed = pygame.mouse.get_pressed()

        if keys[pygame.K_ESCAPE] == 1:
            gameExit = True
            game_intro()
            
        if gameExit == False:

            #Check difficulty
            if difficulty == 'easy':
                time += 5
                yellow_time += 0.15
                green_time += 0.15
            if difficulty == 'normal':
                time += 3
                yellow_time += 0.3
                green_time += 0.3
            if difficulty == 'hard':
                time += 2
                yellow_time += 0.5
                green_time += 0.5
            if difficulty == 'very hard':
                time += 1.5
                yellow_time += 0.75
                green_time += 0.75
            if difficulty == 'extreme':
                time += 1
                yellow_time += 1
                green_time += 1

            bullet_time += 1

            #Make bullet disappear
            if difficulty == 'easy' and bullet_time > 199:
                bullet_time = 0
            if difficulty == 'normal' and bullet_time > 109:
                bullet_time = 0
            if difficulty == 'hard' and bullet_time > 79:
                bullet_time = 0
            if difficulty == 'very hard' and bullet_time > 44:
                bullet_time = 0
            if difficulty == 'extreme' and bullet_time > 19:
                bullet_time = 0

            #Adding Enemy Yellow
            if yellow_time > 89 and time < 4000:
                yellow_time = 0
                x_yellow_enemie.append(850)
                y_yellow_enemie.append(random.randrange(51,551))

            #Adding Enemy Green
            if green_time > 134 and time > 800 and time < 4000:
                green_time = 0
                x_green_enemie.append(random.randrange(51,751))
                y_green_enemie.append(650)

            #Game win condition
            if time > 3999 and game_over == False and len(x_bullet) < 1 and len(x_bullet_type_2) < 1 and len(x_bullet_type_3) < 1 and len(x_yellow_enemie) < 1 and len(x_green_enemie) < 1 and len(x_red_enemie) < 1 and len(x_blue_enemie) < 1:
                largeText = pygame.font.Font('freesansbold.ttf', 70)
                TextSurf, TextRect = text_objects("YOU DID IT!!!", largeText)
                TextRect.center = ((display_width/2),(display_height/2))
                gameDisplay.blit(TextSurf, TextRect)

            #Pattern type 1
            for i in range(len(x_bullet)-1, -1, -1):
                x_bullet[i] += x_bullet_speed[i] * 5
                y_bullet[i] += y_bullet_speed[i] * 5
                
                pygame.draw.rect(gameDisplay, bullet_color[i],(x_bullet[i] - 5, y_bullet[i] - 5, 10, 10))

                if x_player > x_bullet[i] - 10 and x_player < x_bullet[i] + 10 and y_player > y_bullet[i] - 10 and y_player < y_bullet[i] + 10:
                    game_over = True

                if x_bullet[i] < -25 or x_bullet[i] > 825 or y_bullet[i] > 625 or y_bullet[i] < -25:
                    del x_bullet[i]
                    del y_bullet[i]
                    del x_bullet_speed[i]
                    del y_bullet_speed[i]
                    del bullet_color[i]
            
            #Pattern type 2
            for i in range(len(x_bullet_type_2)-1, -1, -1):
                x_bullet_type_2[i] += x_bullet_type_2_speed[i] / 5
                y_bullet_type_2[i] += y_bullet_type_2_speed[i] / 2.5
                y_bullet_type_2_speed[i] += 0.4
                
                pygame.draw.rect(gameDisplay, red,(x_bullet_type_2[i] - 5, y_bullet_type_2[i] - 5, 10, 10))

                if x_player > x_bullet_type_2[i] - 10 and x_player < x_bullet_type_2[i] + 10 and y_player > y_bullet_type_2[i] - 10 and y_player < y_bullet_type_2[i] + 10:
                    game_over = True

                if x_bullet_type_2[i] < -25 or x_bullet_type_2[i] > 825 or y_bullet_type_2[i] > 625:
                    del x_bullet_type_2[i]
                    del y_bullet_type_2[i]
                    del x_bullet_type_2_speed[i]
                    del y_bullet_type_2_speed[i]
                    del bullet_type_2_color[i]
            
            #Pattern type 3
            for i in range(len(x_bullet_type_3)-1, -1, -1):
                x_bullet_type_3[i] += x_bullet_type_3_speed[i] * 5
                y_bullet_type_3[i] += y_bullet_type_3_speed[i] * 5
                
                pygame.draw.rect(gameDisplay, yellow,(x_bullet_type_3[i] - 5, y_bullet_type_3[i] - 5, 10, 10))

                if x_player > x_bullet_type_3[i] - 10 and x_player < x_bullet_type_3[i] + 10 and y_player > y_bullet_type_3[i] - 10 and y_player < y_bullet_type_3[i] + 10:
                    game_over = True

                if x_bullet_type_3[i] < -25 or x_bullet_type_3[i] > 825 or y_bullet_type_3[i] > 625 or y_bullet_type_3[i] < -25:
                    del x_bullet_type_3[i]
                    del y_bullet_type_3[i]
                    del x_bullet_type_3_speed[i]
                    del y_bullet_type_3_speed[i]
                    del bullet_type_3_color[i]

            #Drawing Enemy Yellow
            for i in range(len(x_yellow_enemie)-1, -1, -1):
                x_yellow_enemie[i] += -3
                
                pygame.draw.rect(gameDisplay, yellow,(x_yellow_enemie[i] - 15, y_yellow_enemie[i] - 15, 30, 30))
                
                pygame.draw.rect(gameDisplay, black,(x_yellow_enemie[i] - 12, y_yellow_enemie[i] - 12, 6, 6))
                pygame.draw.rect(gameDisplay, black,(x_yellow_enemie[i] + 6, y_yellow_enemie[i] - 12, 6, 6))
                pygame.draw.rect(gameDisplay, black,(x_yellow_enemie[i] - 12, y_yellow_enemie[i] + 6, 24, 6))

                if difficulty == 'easy':
                    number = 66
                if difficulty == 'normal':
                    number = 46
                if difficulty == 'hard':
                    number = 31
                if difficulty == 'very hard':
                    number = 21
                if difficulty == 'extreme':
                    number = 11

                if random.randrange(1,number) == 1:
                    x = x_yellow_enemie[i]
                    y = y_yellow_enemie[i]
                    
                    if random.randrange(0,2) == 1:
                        if random.randrange(0,2) == 1:
                            x_random = 800
                            y_random = random.randrange(1,601)
                        else:
                            x_random = 0
                            y_random = random.randrange(1,601)
                    else:
                        if random.randrange(0,2) == 1:
                            x_random = random.randrange(1,801)
                            y_random = 600
                        else:
                            x_random = random.randrange(1,801)
                            y_random = 0

                    distance = sqrt((x_random - x)**2 + (y_random - y)**2)
                            
                    x_speed = (x_random - x) / 240
                    y_speed = (y_random - y) / 240
                            
                    x_speed /= distance / 150
                    y_speed /= distance / 150
                            
                    x_bullet_speed.append(x_speed)
                    y_bullet_speed.append(y_speed)
                            
                    x_bullet.append(x)
                    y_bullet.append(y)

                    bullet_color.append(blue)

                if x_player > x_yellow_enemie[i] - 20 and x_player < x_yellow_enemie[i] + 20 and y_player > y_yellow_enemie[i] - 20 and y_player < y_yellow_enemie[i] + 20:
                    game_over = True
                if x_player > x_yellow_enemie[i] - 30 and x_player < x_yellow_enemie[i] - 10 and y_player > y_yellow_enemie[i] - 25 and y_player < y_yellow_enemie[i] - 5:
                    game_over = True
                if x_player > x_yellow_enemie[i] + 10 and x_player < x_yellow_enemie[i] + 30 and y_player > y_yellow_enemie[i] - 25 and y_player < y_yellow_enemie[i] - 5:
                    game_over = True
                if x_player > x_yellow_enemie[i] - 30 and x_player < x_yellow_enemie[i] - 10 and y_player > y_yellow_enemie[i] + 10 and y_player < y_yellow_enemie[i] + 30:
                    game_over = True
                if x_player > x_yellow_enemie[i] + 10 and x_player < x_yellow_enemie[i] + 30 and y_player > y_yellow_enemie[i] + 10 and y_player < y_yellow_enemie[i] + 30:
                    game_over = True

                if x_yellow_enemie[i] < -25:
                    del x_yellow_enemie[i]
                    del y_yellow_enemie[i]
            
            #Drawing Enemy Green
            for i in range(len(x_green_enemie)-1, -1, -1):
                y_green_enemie[i] += -2
                
                pygame.draw.rect(gameDisplay, green,(x_green_enemie[i] - 25, y_green_enemie[i] - 15, 50, 30))
                pygame.draw.rect(gameDisplay, green,(x_green_enemie[i] - 15, y_green_enemie[i] - 25, 30, 50))
                
                pygame.draw.rect(gameDisplay, black,(x_green_enemie[i] - 15, y_green_enemie[i] - 15, 8, 8))
                pygame.draw.rect(gameDisplay, black,(x_green_enemie[i] + 7, y_green_enemie[i] - 15, 8, 8))
                pygame.draw.rect(gameDisplay, black,(x_green_enemie[i] - 15, y_green_enemie[i] + 7, 30, 8))

                if difficulty == 'easy':
                    number = 56
                if difficulty == 'normal':
                    number = 36
                if difficulty == 'hard':
                    number = 21
                if difficulty == 'very hard':
                    number = 11
                if difficulty == 'extreme':
                    number = 4

                if random.randrange(1,number) == 1:
                    x = x_green_enemie[i]
                    y = y_green_enemie[i]
                            
                    x_bullet_type_2_speed.append(random.randrange(-30,31))
                    y_bullet_type_2_speed.append(random.randrange(-20,0))
                            
                    x_bullet_type_2.append(x)
                    y_bullet_type_2.append(y)

                    bullet_type_2_color.append(darkred)

                if x_player > x_green_enemie[i] - 30 and x_player < x_green_enemie[i] + 30 and y_player > y_green_enemie[i] - 20 and y_player < y_green_enemie[i] + 20:
                    game_over = True
                if x_player > x_green_enemie[i] - 20 and x_player < x_green_enemie[i] + 20 and y_player > y_green_enemie[i] - 30 and y_player < y_green_enemie[i] + 30:
                    game_over = True
                if x_player > x_green_enemie[i] - 8 and x_player < x_green_enemie[i] + 8 and y_player > y_green_enemie[i] - 45 and y_player < y_green_enemie[i] - 10:
                    game_over = True
                if x_player > x_green_enemie[i] - 15 and x_player < x_green_enemie[i] + 15 and y_player > y_green_enemie[i] - 65 and y_player < y_green_enemie[i] - 35:
                    game_over = True

                if y_green_enemie[i] < -25:
                    del x_green_enemie[i]
                    del y_green_enemie[i]
            
        pygame.draw.rect(gameDisplay, green,(x_player - 5, y_player - 5, 10, 10))
        pygame.draw.rect(gameDisplay, black,(x_player - 4, y_player - 4, 2, 2))
        pygame.draw.rect(gameDisplay, black,(x_player + 2, y_player - 4, 2, 2))
        pygame.draw.rect(gameDisplay, black,(x_player - 4, y_player + 2, 8, 2))

        if restart == True:
            x_player = 400
            y_player = 300

            gameExit = False

            x_bullet = list()
            y_bullet = list()
            x_bullet_speed = list()
            y_bullet_speed = list()
            bullet_color = list()

            x_bullet_type_2 = list()
            y_bullet_type_2 = list()
            x_bullet_type_2_speed = list()
            y_bullet_type_2_speed = list()
            bullet_type_2_color = list()

            x_bullet_type_3 = list()
            y_bullet_type_3 = list()
            x_bullet_type_3_speed = list()
            y_bullet_type_3_speed = list()
            bullet_type_3_color = list()

            x_yellow_enemie = list()
            y_yellow_enemie = list()

            x_green_enemie = list()
            y_green_enemie = list()

            game_over = False

            time = 0

            yellow_time = 90
            green_time = 0

            bullet_time = 0
        
        largeText = pygame.font.Font('freesansbold.ttf', 50)
        TextSurf, TextRect = text_objects("Time:%d" %(time/100), largeText)
        TextRect.center = ((display_width/2),(display_height/10))
        gameDisplay.blit(TextSurf, TextRect)
        
        if game_over == True:
            largeText = pygame.font.Font('freesansbold.ttf', 120)
            TextSurf, TextRect = text_objects_blue("GAME OVER", largeText)
            TextRect.center = ((display_width/2),(display_height/2))
            gameDisplay.blit(TextSurf, TextRect)
            
        pygame.display.update()
        clock.tick(60)

game_intro()

pygame.quit()
quit()
