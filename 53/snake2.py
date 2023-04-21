import pygame , sys , random


pygame.init()


# variables 
win_w = 800
win_h = 600
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
worm_x = random.randrange(0,win_w - 20,20)
worm_y = random.randrange(0,win_h - 20,20)
speed_worm_x = 0
speed_worm_y = 0
clock = pygame.time.Clock()
fps = 10
food_x = random.randrange(0,win_w,20)
food_y = random.randrange(0,win_h,20)
worm_list = []
worm_length = 0
game_over = False 

#  make display 
win = pygame.display.set_mode((win_w,win_h))
pygame.display.set_caption('Snake')

# make function for change length of worm   --> tagiir andaze worm
def worm(worm_x,worm_y,worm_list):
    g_over = False
    worm_head = [worm_x,worm_y]
    worm_list.append(worm_head)
    # print(worm_list)
    for item in worm_list:
        pygame.draw.rect(win,green,(item[0],item[1] ,20,20))

    for section in worm_list[:-1]:
        if worm_head == section:
            g_over = True
    return g_over



#  main game loop
while not game_over:
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
    # make hit ya barkbhord 
    if worm_x == food_x and worm_y == food_y:
        food_x = random.randrange(0,win_w,20)
        food_y = random.randrange(0,win_h,20)
        worm_length += 1
    # shart afzayesh tool worm
    if len(worm_list) > worm_length:
        worm_list.pop(0)
    # make snake
    game_over = worm(worm_x,worm_y,worm_list)
    pygame.draw.rect(win,red,(food_x,food_y ,20,20))

    clock.tick(fps)
    pygame.display.update()        

