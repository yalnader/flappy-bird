#imports
import sys
import pygame
#const
script_dir = sys.path[0]
gravity = 1

#images, and scaling
bird_up = pygame.image.load("img/bird-wings-up-1.png")
bird_up = pygame.transform.scale(bird_up, (40,30))
bird_middle = pygame.image.load("img/bird-wings-middle-1.png")
bird_middle = pygame.transform.scale(bird_middle, (40,30))
bird_down = pygame.image.load("img/bird-wings-down-1.png")
bird_down = pygame.transform.scale(bird_down, (40,30))

#class which handles bird sprite. 
class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        #define images
        self.sprites = [bird_up, bird_middle, bird_down]
        
        self.x_position = 100
        self.y_position = 300
        self.velocity = 0
        self.acceleration = 0

        self.current_sprite = 1

        self.image = self.sprites[self.current_sprite]

        # create bird rect
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.mask.get_rect()
        self.rect.center = (self.x_position, self.y_position)




