import pygame ,sys , random

pygame.init()

# variabls
red = (255,0,0)
blue = (0,0,255)
black = (0,0,0)
p_pos = [370,500] # player_position
e_pos = [random.randint(0,740),0]
p_speed = 10
e_speed = 5
fps = 60 # frame per second
game_over = False
enemy_list = [e_pos]

win = pygame.display.set_mode((800,600))
pygame.display.set_caption('SimpleGame')
clock = pygame.time.Clock()

#define functions 
# tabe beraye chek barkhord 
def collision(player_pos,enemy_pos):
    p_x , p_y = player_pos[0] , player_pos[1]
    e_x ,e_y = enemy_pos[0], enemy_pos[1]
    if  e_x < p_x < (e_x + 60) or p_x < e_x <(p_x + 60):
        if  e_y < p_y < (e_y +60) or p_y < e_y < (p_y + 60):
            return True
        

# sakht tedad ziad doshman  
def make_enemy(enemy_list):
    a = random.randint(0,30)
    if len(enemy_list) <= 10 and a < 1:
        x = random.randint(0,740)
        y = 0
        enemy_list.append([x,y]) 
        print(enemy_list)   

def draw_enemy(enemy_list):
    for enemy in enemy_list:
        pygame.draw.rect(win,red,(enemy[0],enemy[1],60,60))

def enemy_pos_update(enemy_list):
    for index,enemy_pos in enumerate(enemy_list):
        if 0 <= enemy_pos[1] <= 600:
            enemy_pos[1] += e_speed
        else:
            enemy_list.pop(index)         

def check_collision(enemy_list,player_pos):
    for enemy in enemy_list:
        if collision(player_pos,enemy):
            return True
    return False  
  
while not game_over:
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

    # voorood majadad doshamn az bala 
    # if e_pos[1] >= 0 and e_pos[1] <= 600:
    #     e_pos[1] += e_speed
    # else:
    #     e_pos[1] = 0
    #     e_pos[0] = random.randint(80,740)    
    win.fill(black)
    # make player
    # game_over = collision(p_pos,e_pos)      
    pygame.draw.rect(win,blue,(p_pos[0],p_pos[1],60,60)) 
    
    clock.tick(fps) 
    make_enemy(enemy_list)
    draw_enemy(enemy_list)
    enemy_pos_update(enemy_list)
    game_over = check_collision(enemy_list,p_pos)
    pygame.display.update()        

