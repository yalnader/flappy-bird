#imports
import sys
import pygame

#const
script_dir = sys.path[0]
gravity = 0.05


#class which handles bird sprite. 
class Bird(pygame.sprite.Sprite):
    def __init__(self, bird_up, bird_middle, bird_down):
        super().__init__()

        #define images
        self.sprites = [bird_up, bird_middle, bird_down]
        
        self.x_position = 50
        self.y_position = 300
        self.speed = 0

        self.current_sprite = 1

        self.image = self.sprites[self.current_sprite]

        # create bird rect
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.mask.get_rect()
        self.rect.center = (self.x_position, self.y_position)

    def update(self):
        #logic for bird falling
        self.speed += gravity
        self.rect.centery += self.speed
        
    def flap(self):
        #logic for bird flap
        self.speed = 0
        self.rect.centery -= 150
  



