import pygame
import sys
import random

from fish import Fish, fishes #importing a class and sprite group


#Initialize pygame
pygame.init()

#screen dimensions
screen_width = 800
screen_height = 600
tile_size = 64

#create screen
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Beach in St Petersburg, FL with moving fish')

#clock object
clock = pygame.time.Clock()

def draw_background(screen):
    #load our tiles
    water = pygame.image.load("../assets/sprites/water.png").convert()
    sand = pygame.image.load("../assets/sprites/sand_top.png").convert()
    seagrass = pygame.image.load("../assets/sprites/seagrass.png").convert()
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
    custom_font = pygame.font.Font('../assets/Fonts/28 Days Later.ttf', 64)
    text = custom_font.render('Chomp', True, (255,0,0))
    screen.blit(text, (screen_width/2 - text.get_width()/2,screen_height/17 - text.get_height()/2))

#main loop
running = True
background = screen.copy()
draw_background(background)

#draw fish on screen
for _ in range(5):
    fishes.add(Fish(random.randint(screen_width,screen_width*1.5),random.randint(tile_size,screen_height-2*tile_size)))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #draw background
    screen.blit(background, (0,0))

    #update fish location
    fishes.update()

    #check in any fish is off the screen
    for fish in fishes:
        if fish.rect.x < - fish.rect.width:
            fishes.remove(fish) #removes that fish off the screen
            fishes.add(Fish(random.randint(screen_width, screen_width + 50),
                            random.randint(tile_size, screen_height - 2 * tile_size)))

    #draw the fish
    fishes.draw(screen)

    # update display
    pygame.display.flip()

    #limit frame rate
    clock.tick(60)

# quit pygame
pygame.quit()
