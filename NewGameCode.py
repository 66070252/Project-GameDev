"""Start Here"""
import pygame
import random
import time
from math import sqrt

#Normal setting Ready to draw it
pygame.init()

display_width = 800
display_height = 600

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
pygame.display.set_caption('Project B')
clock = pygame.time.Clock()

def text_objects(text, font):
    textSurface = font.render(text, True, blue)
    return textSurface, textSurface.get_rect()

def text_objects_blue(text, font):
    textSurface = font.render(text, True, blue)
    return textSurface, textSurface.get_rect()
#Running game
def game_intro():
    game_loop()
#Keep Game still running
def game_loop():

    choose_difficuly = True

    left_clicked = True

    #Choose difficuly
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

      mouse_pos = pygame.mouse.get_pos()
      x_mouse = mouse_pos[0]
      y_mouse = mouse_pos[1]

      mouse_pressed = pygame.mouse.get_pressed()

      if x_mouse > 150 and x_mouse < 250 and y_mouse > 175 and y_mouse < 225:
          pygame.draw.rect(gameDisplay, green,(150, 175, 100, 50))
          if mouse_pressed[0] == 1 and left_clicked == False:
              difficulty = 'easy'
              choose_difficulty = False
                
      else:
          pygame.draw.rect(gameDisplay, darkgreen,(150, 175, 100, 50))

      if x_mouse > 350 and x_mouse < 450 and y_mouse > 175 and y_mouse < 225:
          pygame.draw.rect(gameDisplay, green,(350, 175, 100, 50))
          if mouse_pressed[0] == 1 and left_clicked == False:
              difficulty = 'normal'
              choose_difficulty = False
                
      else:
          pygame.draw.rect(gameDisplay, darkgreen,(350, 175, 100, 50))

      if x_mouse > 550 and x_mouse < 650 and y_mouse > 175 and y_mouse < 225:
          pygame.draw.rect(gameDisplay, green,(550, 175, 100, 50))
          if mouse_pressed[0] == 1 and left_clicked == False:
              difficulty = 'hard'
              choose_difficulty = False
      else:
          pygame.draw.rect(gameDisplay, darkgreen,(550, 175, 100, 50))

      if x_mouse > 250 and x_mouse < 350 and y_mouse > 375 and y_mouse < 425:
          pygame.draw.rect(gameDisplay, green,(250, 375, 100, 50))
          if mouse_pressed[0] == 1 and left_clicked == False:
              difficulty = 'very hard'
              choose_difficulty = False
                
      else:
          pygame.draw.rect(gameDisplay, darkgreen,(250, 375, 100, 50))

      if x_mouse > 450 and x_mouse < 550 and y_mouse > 375 and y_mouse < 425:
            pygame.draw.rect(gameDisplay, green,(450, 375, 100, 50))
            if mouse_pressed[0] == 1 and left_clicked == False:
                difficulty = 'extreme'
                choose_difficulty = False

        else:
            pygame.draw.rect(gameDisplay, darkgreen,(450, 375, 100, 50))
        
        if left_clicked == False and mouse_pressed[0] == 1:
            left_clicked == True
        elif left_clicked == True and mouse_pressed[0] == 0:
            left_clicked = False
            
        smallText = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = text_objects("EASY", smallText)
        TextRect.center = ((200),(200))
        gameDisplay.blit(TextSurf, TextRect)
        
        smallText = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = text_objects("NORMAL", smallText)
        TextRect.center = ((400),(200))
        gameDisplay.blit(TextSurf, TextRect)

        smallText = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = text_objects("HARD", smallText)
        TextRect.center = ((600),(200))
        gameDisplay.blit(TextSurf, TextRect)

        smallText = pygame.font.Font('freesansbold.ttf', 15)
        TextSurf, TextRect = text_objects("VERY HARD", smallText)
        TextRect.center = ((300),(400))
        gameDisplay.blit(TextSurf, TextRect)

        smallText = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = text_objects("EXTREME", smallText)
        TextRect.center = ((500),(400))
        gameDisplay.blit(TextSurf, TextRect)
        
        pygame.display.update()
        clock.tick(60)
    
    #Player movement and speed
    x_player = display_height // 2
    y_player = display_width // 2
    speed_player = 5

    gameExit = False

    gameOver = False

    restart = False

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

    while not gameExit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x_player -= speed_player
    if keys[pygame.K_d]:
        x_player += speed_player
    if keys[pygame.K_w]:
        y_player -= speed_player
    if keys[pygame.K_s]:
        y_player += speed_player

    mouse_pressed = pygame.mouse.get_preessed()
    if event.type == pygame.QUIT:
        pygame.quit()
        quit()

    gameDisplay.fill(white)

    mouse_pressed = pygame.mouse.get_pressed()

    if mouse_pressed[2] == 1:
        gameExit == True
        game_intro()

    if gameExit == False:

        if difficulty == "easy":
            time += 5
            yellow_time += 0.15
            green_time += 0.15
        if difficulty == "normal":
            time += 3
            yellow_time += 0.3
            green_time += 0.3
        if difficulty == "hard":
            time += 2
            yellow_time += 0.5
            green_time += 0.5
        if difficulty == "hard":
            time += 2
            yellow_time += 0.5
            green_time += 0.5
        if difficulty == "very hard":
            time += 1.5
            yellow_time += 0.75
            green_time += 0.75
        if difficulty == "extreme":
            time += 1
            yellow_time += 1
            green_time += 1

        bullet_time += 1

        if diffculty == "easy" and bullet_time > 199:
            bullet_time = 0
        if diffculty == "normal" and bullet_time > 109:
            bullet_time = 0
        if diffculty == "hard" and bullet_time > 79:
            bullet_time = 0
        if diffculty == "very hard" and bullet_time > 44:
            bullet_time = 0
        if diffculty == "extreme" and bullet_time > 19:
            bullet_time = 0

        if yellow_time > 89 and time < 4000:
            yellow_time = 0
            x_yellow_enemie.append(850)
            y_yellow_enemie.append(random.randrange(51,551))

        if green_time > 134 and time > 800 and time < 4000:
            green_time = 0
            x_green_enemie.append(random.randrange(51,751))
            y_green_enemie.append(650)

        if time > 3999 and game_over == False and len(x_bullet) < 1 and len(x_bullet_type_2) < 1 and len(x_bullet_type_3) < 1 and len(x_yellow_enemie) < 1 and len(x_green_enemie) < 1 and len(x_red_enemie) < 1 and len(x_blue_enemie) < 1:
            largeText = pygame.font.Font("freesansbold.ttf", 70)
            TextSurf, TextRect = text_objects("YOU WON!!!", largeText)
            TextRect.center = ((display_width/2),(display_height/2))
            gameDisplay.blit(TextSurf, TextRect)

        for i in range(len(x_bullet)-1, -1, -1):
            x_bullet[i] += x_bullet_speed[i] * 5
            y_bullet[i] += y_bullet_speed[i] * 5

            pygame.draw.rect(gameDisplay, bullet_color[i],(x_bullet[i] - 5, y_bullet[i] - 5, 10, 10))

            if x_player > x_bullet[i] - 10 and x_player < x_player[i] + 10 and y_player > y_player[i] - 10 and y_player < y_player[i] + 10:
                game_over = True

            if x_bullet[i] < -25 or x_bullet[i]  > 825 or y_bullet[i] > 625 or y_bullet[i] < -25:
                del x_bullet[i]
                del y_bullet[i]
                del x_bullet_speed[i]
                del y_bullet_speed[i]
                del bullet_color[i]

        for i in range(len(x_bullet_type_2)-1, -1, -1):
            x_bullet_type_2[i] += x_bullet_type_2_speed[i] / 5
            y_bullet_type_2[i] += y_bullet_type_2_speed[i] / 2.5
            y_bullet_type_2_speed[i] += 0.4

            pygame.draw.rect(gameDisplay, red,(x_bullet_type_2[i] - 5, y_bullet_type_2[i] - 5, 10, 10))

            if x_player > x_bullet_type_2[i] -10 and x_player < x_bullet_type_2[i] + 10 and if y_player > y_bullet_type_2[i] -10 and y_player < y_bullet_type_2[i] + 10:
                game_over = True

            if x_bullet_type_2[i] < -25 or x_bullet_2[i] > 825 or y_bullet_type_2[i] > 625:
                del x_bullet_type_2[i]
                del y_bullet_type_2[i]
                del x_bullet_type_2_speed[i]
                del y_bullet_type_2_speed[i]
                del bullet_type_2_color[i]

        for i in range(len(x_bullet_type_3)-1, -1, -1);
            x_bullet_type_3[i] += x_bullet_type_3_speed[i] * 5
            y_bullet_type_3[i] += y_bullet_type_3_speed[i] * 5
        
            pygame.draw.rect(gameDisplay, yellow,(x_bullet_type_3[i] - 5, y_bullet_type_3[i] - 5, 10, 10))

            if x_player > x_bullet_type_3[i] -10 and x_player < x_bullet_type_3[i] + 10 and if y_player > y_bullet_type_3[i] -10 and y_player < y_bullet_type_3[i] + 10:
                game_over = True

            if x_bullet_type_3[i] < -25 or x_bullet_3[i] > 825 or y_bullet_type_3[i] > 625 or y_bullet_type_3[i] < -25:
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
            
