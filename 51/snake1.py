import pygame , sys


pygame.init()


# variables 
win_w = 800
win_h = 600
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
worm_x = 380
worm_y = 280
speed_worm_x = 0
speed_worm_y = 0
clock = pygame.time.Clock()
fps = 10

#  make display 
win = pygame.display.set_mode((win_w,win_h))
pygame.display.set_caption('Snake')


#  main game loop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                speed_worm_x = 20
                speed_worm_y = 0
            if event.key == pygame.K_LEFT:
                speed_worm_x = -20
                speed_worm_y = 0
            if event.key == pygame.K_UP:
                speed_worm_y = -20
                speed_worm_x = 0
            if event.key == pygame.K_DOWN:
                speed_worm_y = 20
                speed_worm_x = 0

    win.fill(black) 
    # jehat harakat   
    worm_x += speed_worm_x
    worm_y += speed_worm_y    
    # barhgasht be safheh
    if worm_x < 0:
        worm_x = win_w -20
    if worm_x > win_w -20:
        worm_x = 0
    if worm_y > win_h -20:
        worm_y = 0
    if worm_y < 0:
        worm_y= win_h-20     

    # make snake
    pygame.draw.rect(win,green,(worm_x,worm_y ,20,20))
    clock.tick(fps)
    pygame.display.update()        

