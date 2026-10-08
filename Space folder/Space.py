import pygame
from pygame.locals import *
from time import *

pygame.init()

screen=pygame.display.set_mode((600,600))
player_x = 150
player_y = 150
keys = [False,False,False,False]
player = pygame.image.load("Player_ship.png")
bg = pygame.image.load("Space_bg.jpg")
background = pygame.transform.scale(bg, (600,600))

while player_y < 600:
    screen.blit(background, (0,0))
    screen.blit(player, (player_x, player_y))
    pygame.display.flip()

    #check if any keyboard button is pressed

    for event  in pygame.event.get():
        if event.type == pygame.KEYDOWN:

             if event.key ==K_UP:
                 keys[0]=True
             if event.key ==K_LEFT:
                 keys[1]=True
             if event.key ==K_DOWN:
                 keys[2]=True
             if event.key ==K_RIGHT:
                 keys[3]=True    
        if event.type == pygame.KEYUP:
            if event.key ==K_UP:
                 keys[0]=False
            if event.key ==K_LEFT:
                 keys[2]=False
            if event.key ==K_DOWN:
                 keys[2]=False
            if event.key ==K_RIGHT:
                 keys[3]=False   

        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    #up is 0, left is 1, down is 2,right is 3
    if keys[0]:
        if player_y > 0:
            player_y = player_y -5

    if keys[1]:
        if player_x > 0:
            player_x = player_x -5 

    if keys[2]:
        if player_y < 540:
            player_y = player_y +5

    if keys[3]:
        if player_x < 540:
            player_x = player_x +5         



                                        
                