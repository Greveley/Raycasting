import pygame
import numpy as np
from intersect import intersect

# initialising pygame
pygame.init()

# Colours
white = (255,255,255)
black = (0,0,0)

height = 600
width = 600
angles = np.arange(0,np.pi*2,0.1)
# angles = 75


disp = pygame.display.set_mode((width,height))
pygame.display.set_caption('Raycasting')
disp.fill(black)

num_walls = 1

# walls_x_start = np.random.randint(100,width,num_walls)
# walls_x_end = np.random.randint(100,width,num_walls)
# walls_y_start = np.random.randint(100,height,num_walls)
# walls_y_end = np.random.randint(100,height,num_walls)

walls_x1 = 400
walls_y1 = 200
walls_x2 = 400
walls_y2 = 500


close = False

def draw_cirle(x,y):
    pygame.draw.circle(disp,white,(x,y),5)

def draw_rays(x1,y1,x2,y2):
    # for i in np.arange(0,len(x2)):
    #     pygame.draw.line(disp, white, (x, y), (x2[i], y2[i]))
    # pygame.draw.line(disp, white, (x, y), (x * np.sin(75) * 100, y * np.cos(75) * 100))
    pygame.draw.line(disp, white, (x1, y1), (x2, y2))


def draw_walls(x1,y1,x2,y2):
    # for i in np.arange(0,len(x1)):
    #     pygame.draw.line(disp, white, (x1[i], y1[i]), (x2[i],y2[i]),4)
    pygame.draw.line(disp, white, (x1, y1), (x2,y2),4)


while not close:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close = True


    disp.fill(black)
    pygame.display.update()

    # Mouse locations
    (loc_x,loc_y) = pygame.mouse.get_pos()

    x1 = 100
    y1 = 300
    x2 = loc_x
    y2 = loc_y

    draw_cirle(x1,y1)


    draw_walls(walls_x1,walls_y1,walls_x2,walls_y2)

    if intersect(x1,y1,x2,y2,walls_x1,walls_y1,walls_x2,walls_y2):

        draw_rays(x1,y1,x2,y2)
        px,py = intersect(x1,y1,x2,y2,walls_x1,walls_y1,walls_x2,walls_y2)
        pygame.draw.circle(disp, white, (px, py), 5)

    pygame.display.update()




