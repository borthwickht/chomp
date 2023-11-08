import pygame
import random
import sys

from game_parameters import *
from fish import Fish, fishes
from background import draw_background, add_fish, add_enemies
from player import Player
from enemy import enemies, Enemy

# initialize pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Beach in St Petersburg, FL with moving fish')

# load sound effects
chomp = pygame.mixer.Sound('../assets/sounds/chomp.wav')

# clock object
clock = pygame.time.Clock()

# main loop
running = True
background = screen.copy()
draw_background(background)

# draw fish on screen and enemies
add_fish(5)
add_enemies(5)

# create a player fish
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

# initialize score for fish game
score = 0
score_font = pygame.font.Font('../assets/Fonts/Black_Crayon.ttf', 48)
text = score_font.render(f'{score}', True, (255, 0, 0))

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

    #draw enemies
    enemies.update()

    # draw a player fish
    player.update()

    # check for player and sprite colisions
    result = pygame.sprite.spritecollide(player, fishes, True)
    # print(result)
    if result:
        # play chomp sound
        pygame.mixer.Sound.play(chomp)
        score += len(result)
        print(score)
    # draw fish on screen
        add_fish(len(result))

    # check for player and sprite colisions
    result = pygame.sprite.spritecollide(player, enemies, True)
    # print(result)
    if result:
        # play chomp sound
        pygame.mixer.Sound.play(chomp)
        # score += len(result)
        # print(score)
        # draw more enemies on screen
        add_enemies(len(result))

    for fish in fishes:
        if fish.rect.x < - fish.rect.width:
            fishes.remove(fish)  # removes that fish off the screen
            add_fish(1)

    for enemy in enemies:
        if enemy.rect.x < - enemy.rect.width:
            enemies.remove(fish)  # removes that enemy off the screen
            add_enemies(1)

    # draw objects
    fishes.draw(screen)
    player.draw(screen)
    enemies.draw(screen)

    # draw the score on the string
    text = score_font.render(f'{score}', True, (255, 0, 0))
    screen.blit(text, (SCREEN_WIDTH-TILE_SIZE, 0))

    # update display
    pygame.display.flip()

    # limit frame rate
    clock.tick(60)

# quit pygame
pygame.quit()
sys.exit()