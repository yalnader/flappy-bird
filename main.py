#imports
import pygame
import sys
from bird import Bird
#constants
script_dir = sys.path[0]
bg_img_path = "img/flappy-background-2.png"
floor_img_path = "img/flappy-floor-1.png"
screen_width = 500
screen_height = 900



def draw_floor():
    #create 3 surfaces in order to have a fluid moving floor
    screen.blit(floor, (floor_x_pos,800))
    screen.blit(floor, (floor_x_pos + 336,800))
    screen.blit(floor, (floor_x_pos + 672,800))

#init pygame
pygame.init()

#create game window 
screen = pygame.display.set_mode([screen_width, screen_height])
#create clock
clock = pygame.time.Clock()

#create background surface
bg = pygame.image.load(bg_img_path).convert()
bg = pygame.transform.scale2x(bg)

#create floor surface
floor = pygame.image.load(floor_img_path).convert()
floor_x_pos = 0

#bird surface
#images, and scaling
bird_up = pygame.image.load("img/bird-wings-up-1.png").convert_alpha()
bird_up = pygame.transform.scale(bird_up, (40,30))
bird_middle = pygame.image.load("img/bird-wings-middle-1.png").convert_alpha()
bird_middle = pygame.transform.scale(bird_middle, (40,30))
bird_down = pygame.image.load("img/bird-wings-down-1.png").convert_alpha()
bird_down = pygame.transform.scale(bird_down, (40,30))

#create bird group
bird_group = pygame.sprite.Group()
bird = Bird(bird_up,bird_middle, bird_down)
bird_group.add(bird)

# run game until user quits
running = True
while running:

    # check window close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.flap()
                

    #move floor
    floor_x_pos -=1

    #update bird
    bird_group.update()
    
    if  floor_x_pos <= -336:
        floor_x_pos = 0

    screen.blit(bg, (0, 0))
    draw_floor()
    # bird_group.draw(screen)
    screen.blit(bird.image, bird.rect)

    # update display
    pygame.display.update()
    clock.tick(120)
# Done! Time to quit.
pygame.quit()