import pygame , sys , random , time 

pygame.init()
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
black = (0,0,0)
p_pos = [300,740]
e_pos = [random.randrange(0,540),0]
clock = pygame.time.Clock()
fps = 60
speed_e = 2
speed_p = 20
exit_flag = False
enemy_list = [e_pos]
score = 0
font1 = pygame.font.Font(None,30)
font2 = pygame.font.Font(None,80)

screen = pygame.display.set_mode((600,800))

def game_start():
    for i in range(3,0,-1):
        font3 = pygame.font.Font(None,400)
        t_s = font3.render(str(i),True , blue)
        screen.blit(t_s , (200,250))
        pygame.display.update()
        time.sleep(1)
        screen.fill(black)

game_start()    

def collision(e_pos,p_pos):
    # print(e_pos,p_pos)
    if ( e_pos[0] <= p_pos[0] < (e_pos[0] + 60) ) or (p_pos[0] <= e_pos[0] < (p_pos[0] + 60)):
        if (e_pos[1] <= p_pos[1] < (e_pos[1]+60)) or (p_pos[1] <= e_pos[1] < (p_pos[1] + 60)):
            return True
    else:
        return False

def enemies(enemy_list):
    num = random.randint(0,30)
    if len(enemy_list) <= 10 and num < 1:
        enemy_x = random.randrange(0,540)
        enemy_y = 0
        enemy_list.append([enemy_x,enemy_y])
        # print(enemy_list)

def draw_enemy(enemy_list):
    for enemy in enemy_list:
        pygame.draw.rect(screen,red,(enemy[0],enemy[1],60,60))

def enemy_pos_update(enemy_list ,score ):
    for index , enemy_pos in enumerate(enemy_list):
        if 0 <= enemy_pos[1] <800:
            enemy_pos[1] += speed_e
        else:
            enemy_list.pop(index)    
            score += 1
    return score         
        
def check_collision(enemy_list,player_pos):
    for enemy in enemy_list:
       if collision(enemy,player_pos):
         return True
    else:
         return False
def speed_level(score,spd):
    if score <= 10:
        spd = 2
    elif score <= 20:
        spd = 4
    elif score <= 50:
        spd = 8 
    elif score <= 100:
        spd = 10
    else:
        spd = 12
    return spd


while not exit_flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                p_pos[0] += speed_p
                keys = pygame.key.get_pressed()
            if event.key == pygame.K_LEFT:
                p_pos[0] -= speed_p

    if check_collision(enemy_list,p_pos):
        screen.fill(black)
        t_s3 = font2.render('you are game over!',True,red)
        screen.blit(t_s3,(100,300))
        t_s1 = font1.render(f"your score is{str(score)}",True,green)
        screen.blit(t_s1,(200,400))
        pygame.display.update()
        time.sleep(3)
        exit_flag = True
        break


    if p_pos[0] < 0:
        p_pos[0] = 0
    if p_pos[0] > 540:
        p_pos[0]= 540    

    screen.fill(black)
    enemies(enemy_list)
    draw_enemy(enemy_list)
    score = enemy_pos_update(enemy_list ,score)
    check_collision(enemy_list,p_pos)
    pygame.draw.rect(screen,blue,(p_pos[0],p_pos[1],60,60))
    t_s1 = font1.render(f"score:{str(score)}",True,green)
    screen.blit(t_s1,(20,20))
    speed_e = speed_level(score , speed_e)
    clock.tick(fps)
    pygame.display.update()
