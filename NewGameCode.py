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
