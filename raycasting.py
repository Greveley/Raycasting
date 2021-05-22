import pygame
import numpy as np
from intersect import *

# initialising pygame
pygame.init()

# Colours
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

height = 600
width = 600
angles = np.arange(0,np.pi*2,0.05)


disp = pygame.display.set_mode((width,height))
pygame.display.set_caption('Raycasting')
disp.fill(black)

walls_x1_side = [0,0,width,0]
walls_y1_side = [0,0,0,height]
walls_x2_side = [0,width,width,width]
walls_y2_side = [height,0,height,height]

extra_walls = 10

walls_x1 = np.random.randint(50,width,extra_walls)
walls_y1 = np.random.randint(50,height,extra_walls)
walls_x2 = np.random.randint(50,width,extra_walls)
walls_y2 = np.random.randint(50,height,extra_walls)

walls_x1 = list(walls_x1) + walls_x1_side
walls_y1 = list(walls_y1) + walls_y1_side
walls_x2 = list(walls_x2) + walls_x2_side
walls_y2 = list(walls_y2) + walls_y2_side

num_walls = len(walls_x1)

close = False
click = 2


def draw_cirle(x,y):
    pygame.draw.circle(disp,red,(x,y),2)

def draw_rays(x,y,x2,y2):
    pygame.draw.line(disp, white, (x, y), (x2, y2))


def draw_walls(x1,y1,x2,y2):
    for i in np.arange(0,len(x1)):
        pygame.draw.line(disp, white, (x1[i], y1[i]), (x2[i],y2[i]),4)

while not close:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close = True


    disp.fill(black)
    # Mouse locations
    (loc_x,loc_y) = pygame.mouse.get_pos()

    x1 = loc_x
    y1 = loc_y
    x2 = []
    y2 = []
    for angle in angles:
        x2.append((np.sin(angle))*1000)
        y2.append((np.cos(angle))*1000)

    # Draw circle on mouse location

    # draw_walls(walls_x1,walls_y1,walls_x2,walls_y2)
    closest = []
    for i in np.arange(0, len(angles)):
        min_dist = 100000
        for j in np.arange(0,num_walls):
            if intersect(x1,y1,x2[i],y2[i],walls_x1[j],walls_y1[j],walls_x2[j],walls_y2[j]):
                px, py = intersect_points(x1, y1, x2[i], y2[i], walls_x1[j], walls_y1[j], walls_x2[j], walls_y2[j])
                dist = np.sqrt(pow((px-x1),2)+pow((py-y1),2))
                if dist < min_dist:
                    min_dist = dist
                    closest_x,closest_y = (px,py)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                click+=1
        if click %2 ==0:
            draw_rays(x1,y1,int(closest_x),int(closest_y))

        else:
            continue

    draw_cirle(x1,y1)

    pygame.display.update()

