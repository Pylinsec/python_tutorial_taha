import pygame ,sys , random
# from pygame.locals import *

pygame.init()

# variabls
red = (255,0,0)
blue = (0,0,255)
black = (0,0,0)
p_pos = [370,500] # player_position
# e_pos = [400,0] # enemy_position
e_pos = [random.randint(0,740),0]
p_speed = 10
e_speed = 0.5

# define screen and name
win = pygame.display.set_mode((800,600))
pygame.display.set_caption('SimpleGame')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            sys.exit()
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_RIGHT:
                p_pos[0] += p_speed
            if event.key == pygame.K_LEFT:
                p_pos[0] -= p_speed   
    # shart berye kharej nesnodan az screen beraye player   
    if p_pos[0] < 0:
        p_pos[0] = 0
    if p_pos[0] >= 740:
        p_pos[0] = 740
    # shart jehat harakt doshman 
    # e_pos[1] += e_speed 
    # voorood majadad doshamn az bala 
    if e_pos[1] >= 0 and e_pos[1] <= 600:
        e_pos[1] += e_speed
    else:
        e_pos[1] = 0
        e_pos[0] = random.randint(0,740)    
    win.fill(black)
    # make player
    pygame.draw.rect(win,blue,(p_pos[0],p_pos[1],60,60)) 
    pygame.draw.rect(win,red,(e_pos[0],e_pos[1],60,60))       
    pygame.display.update()        

