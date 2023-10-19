import pygame
import sys
import random

#Initialize pygame
pygame.init()

#screen dimensions
screen_width = 800
screen_height = 600
tile_size = 64

#create screen
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Beach in St Petersburg, FL')

#load our game font
custom_font = pygame.font.Font('assets/Fonts/28 Days Later.ttf', 64)

# define a funtion to draw the background
def draw_background(screen):
    #load our tiles
    water = pygame.image.load("assets/sprites/water.png").convert()
    sand = pygame.image.load("assets/sprites/sand_top.png").convert()
    seagrass = pygame.image.load("assets/sprites/seagrass.png").convert()
    #use png transparency
    sand.set_colorkey((0,0,0))
    seagrass.set_colorkey((0,0,0))

    #fill the screen
    for x in range(0,screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            screen.blit(water, (x,y))

    #draw the sandy bottom
    for x in range(0,screen_width, tile_size):
        screen.blit(sand, (x,screen_height-tile_size))

    #add seagrass randomly at the bottom of the beach
    for _ in range(7):
        x = random.randint(0, screen_width)
        screen.blit(seagrass,(x,screen_height-2*tile_size))

    #draw the text
    text = custom_font.render('Chomp', True, (255,0,0))
    screen.blit(text, (screen_width/2 - text.get_width()/2,screen_height/17 - text.get_height()/2))

#load some fish tiles

def draw_fishes(screen):
    green_fish = pygame.image.load('assets/sprites/green_fish.png').convert()
    green_fish.set_colorkey((0,0,0)) #set png transparency

    for _ in range(5):
        x = random.randint(0,screen_width-tile_size)
        y = random.randint(0,screen_height-tile_size-tile_size)
        screen.blit(green_fish, (x,y))

def draw_fishes_puffer(screen):
    puffer_fish = pygame.image.load('assets/sprites/puffer_fish.png').convert()
    puffer_fish = pygame.transform.flip(puffer_fish, True, False)
    puffer_fish.set_colorkey((0,0,0)) #set png transparency

    for _ in range(5):
        x = random.randint(0,screen_width-tile_size)
        y = random.randint(0,screen_height-tile_size-tile_size)
        screen.blit(puffer_fish, (x,y))


#main loop
running = True
background = screen.copy()
draw_background(background)
draw_fishes(background)
draw_fishes_puffer(background)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #draw background
    screen.blit(background, (0,0))

    draw_fishes(background)


    #update display
    pygame.display.flip()

#quit pygame
pygame.quit()
