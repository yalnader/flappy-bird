#imports
import pygame
import sys
from bird import Bird
#constants
script_dir = sys.path[0]
bg_img_path = "img/flappy-background-1.png"
floor_img_path = "img/flappy-floor.png"
screen_width = 300
screen_height = 600



def draw_floor():
    #create 2 surfaces in order to have a fluid moving floor
    screen.blit(floor, (floor_x_pos,500))
    screen.blit(floor, (floor_x_pos + 312,500))

#init pygame
pygame.init()


#create bird group
bird_group = pygame.sprite.Group()
bird = Bird()
bird_group.add(bird)

#create game window 
screen = pygame.display.set_mode([screen_width, screen_height])
#create clock
clock = pygame.time.Clock()

#create background surface
bg = pygame.image.load(bg_img_path).convert()

#create floor surface
floor = pygame.image.load(floor_img_path).convert()
floor_x_pos = 0

# run game until user quits
running = True
while running:

    # check window close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #move floor
    floor_x_pos -=1
    
    if  floor_x_pos <= -312:
        floor_x_pos = 0

    screen.blit(bg, (0, 0))
    draw_floor()
    bird_group.draw(screen)

    # update display
    pygame.display.update()
    clock.tick(100)
# Done! Time to quit.
pygame.quit()