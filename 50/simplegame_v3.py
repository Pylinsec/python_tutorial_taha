import pygame ,sys , random , time

pygame.init()

# variabls
red = (255,0,0)
blue = (0,0,255)
black = (0,0,0)
green = (0,255,0)
p_pos = [370,500] # player_position
e_pos = [random.randint(0,740),0]
p_speed = 10
e_speed = 5
fps = 60 # frame per second
game_over = False
enemy_list = [e_pos]
stop = False

# make font text
font1 = pygame.font.Font(None,45)
font_game_over = pygame.font.Font(None,100)
font_score = pygame.font.Font(None,45)
score = 0
win = pygame.display.set_mode((800,600))
pygame.display.set_caption('SimpleGame')
clock = pygame.time.Clock()

#define functions 
# tabe beraye chek barkhord 

def start():
    # start_text = font1.render('start',True,blue,green)
    # start_rect = pygame.Rect(300,150,50,50)
    # win.blit(start_text,start_rect)
    # pygame.display.update()
    font_start = pygame.font.Font(None,400)
    for i in range(3,0,-1):
        num = font_start.render(str(i),True,blue)
        win.blit(num,(300,150))
        pygame.display.update()
        time.sleep(1)
        win.fill(black)
    # text2 = font_start.render('2',True,blue)
    # win.blit(text2,(300,150))
    # pygame.display.update()
    # time.sleep(1)
    # win.fill(black)
    # text1 = font_start.render('1',True,blue)
    # win.blit(text1,(300,150))
    # pygame.display.update()
    time.sleep(1)
start()
start_music = pygame.mixer.music.load('music.mp3')       
pygame.mixer.music.play()
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

def draw_enemy(enemy_list):
    for enemy in enemy_list:
        pygame.draw.rect(win,red,(enemy[0],enemy[1],60,60))

def enemy_pos_update(enemy_list , score ):
    for index,enemy_pos in enumerate(enemy_list):
        if 0 <= enemy_pos[1] <= 600:
            enemy_pos[1] += e_speed
        else:
            enemy_list.pop(index)
            score += 1
    return score        


def check_collision(enemy_list,player_pos):
    for enemy in enemy_list:
        if collision(player_pos,enemy):
            return True
    return False  
def level(scr , e_spd):
    if scr <= 10:
        e_spd = 2
    elif scr >= 10:
        e_spd = 5
    elif scr >= 40:
        e_spd = 7
    elif scr >= 70:
        e_spd = 9
    elif scr >= 100:
        e_spd = 10
    else:
        e_spd = 12    
    return e_spd 


def pause_game(stp):
    while stp:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                sys.exit()
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_SPACE:
                    stp = False
        pygame.display.flip()            
    
#  mainloop 
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
            if event.key == pygame.K_SPACE:
                stop = True
                pause_game(stop)



    # print matn gameover and score  
    if check_collision(enemy_list,p_pos):
        pygame.mixer.music.stop(start_music)
        win.fill(black)
        finish = font_game_over.render('Game Over',True,red)
        win.blit(finish,(250,200))
        show_score = font_score.render(f"your score is: {score}" ,True, green)
        win.blit(show_score,(250,300))
        pygame.display.update()
        time.sleep(3)
        game_over = True




    # shart berye kharej nesnodan az screen beraye player   
    if p_pos[0] < 0:
        p_pos[0] = 0
    if p_pos[0] >= 740:
        p_pos[0] = 740


    win.fill(black)
    pygame.draw.rect(win,blue,(p_pos[0],p_pos[1],60,60)) 
    clock.tick(fps) 
    make_enemy(enemy_list)
    draw_enemy(enemy_list)
    score = enemy_pos_update(enemy_list , score)
    e_speed = level(score,e_speed)
    show_score = font_score.render(f"score: {score}" ,True, green)
    win.blit(show_score,(20,20))
    # game_over = check_collision(enemy_list,p_pos)
    pygame.display.update()        

