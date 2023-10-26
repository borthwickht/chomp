import pygame
import random
import sys

from game_parameters import *
from fish import Fish, fishes
from background import draw_background
from player import Player

# initialize pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Beach in St Petersburg, FL with moving fish')

# clock object
clock = pygame.time.Clock()

# main loop
running = True
background = screen.copy()
draw_background(background)

# draw fish on screen
for _ in range(5):
    fishes.add(Fish(random.randint(SCREEN_WIDTH, SCREEN_WIDTH*1.5), random.randint(TILE_SIZE, SCREEN_HEIGHT-2*TILE_SIZE)))

# create a player fish
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

while running:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            running = False
        # control fish with keyboard
        player.stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print('You pressed the up key')
                player.move_up()
            if event.key == pygame.K_DOWN:
                print('You pressed the down key')
                player.move_down()
            if event.key == pygame.K_LEFT:
                print('You pressed the left key')
                player.move_left()
            if event.key == pygame.K_RIGHT:
                print('You pressed the right key')
                player.move_right()

    # draw background
    screen.blit(background, (0, 0))

    # draw green fish
    fishes.update()

    # draw a player fish
    player.update()

    for fish in fishes:
        if fish.rect.x < - fish.rect.width:
            fishes.remove(fish)  # removes that fish off the screen
            fishes.add(Fish(random.randint(SCREEN_WIDTH+50, SCREEN_WIDTH + 100),
                            random.randint(TILE_SIZE, SCREEN_HEIGHT - 2 * TILE_SIZE)))

    # draw fish
    fishes.draw(screen)
    player.draw(screen)

    # update display
    pygame.display.flip()

    # limit frame rate
    clock.tick(60)

# quit pygame
pygame.quit()
sys.exit()