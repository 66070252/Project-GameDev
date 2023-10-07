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
