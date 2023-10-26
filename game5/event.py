import pygame
import sys
import random
from background import draw_background
from game_parameters import *

#Initialize pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Beach in St Petersburg, FL with moving fish')

#main loop
running = True
background = screen.copy()
draw_background(background)

while running:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print('You pressed the up key')
            if event.key == pygame.K_DOWN:
                print('You pressed the down key')
            if event.key == pygame.K_LEFT:
                print('You pressed the left key')
            if event.key == pygame.K_RIGHT:
                print('You pressed the right key')

    # draw background
    screen.blit(background, (0, 0))

    # update display
    pygame.display.flip()

    # limit frame rate
    # clock.tick(60)

# quit pygame
pygame.quit()