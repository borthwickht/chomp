import pygame
from game_parameters import *
# from event import *

# create a pygame sprite class for a player
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # TODO flip the fish if going the other way
        self.forward_image = pygame.image.load('../assets/sprites/orange_fish.png')
        self.reverse_image = pygame.transform.flip(self.forward_image, True, False)
        self.image = pygame.image.load('../assets/sprites/orange_fish.png')
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.x_speed = 0
        self.y_speed = 0

    def move_up(self):
        self.y_speed = -1 * PLAYER_SPEED

    def move_down(self):
        self.y_speed = PLAYER_SPEED

    def move_left(self):
        self.x_speed = -1 * PLAYER_SPEED
        self.image = self.reverse_image

    def move_right(self):
        self.x_speed = PLAYER_SPEED
        self.image = self.forward_image

    def stop(self):
        self.y_speed = 0
        self.x_speed = 0

    def update(self):
        # TODO: make sure the orange fish stays on the screen
        self.x += self.x_speed
        self.y += self.y_speed
        if self.x > SCREEN_WIDTH - TILE_SIZE:
            self.x = SCREEN_WIDTH-TILE_SIZE
            self.x_speed = 0
        if self.x < 0:
            self.x = 0
            self.x_speed = 0
        if self.y > SCREEN_HEIGHT - (2*TILE_SIZE):
            self.y = SCREEN_HEIGHT -(2*TILE_SIZE)
            self.y_speed = 0
        if self.y < 0:
            self.y = 0
            self.y_speed = 0
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        screen.blit(self.image, self.rect)
