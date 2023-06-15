import pygame , sys , random , time

pygame.init()

# variable for screen
width = 800
height = 600
typing = False
input_text = ''
start_time = 0
total_time = 0


win  = pygame.display.set_mode((width,height))
pygame.display.set_caption('Type speed checker')


# function for  display text in win
def print_text(screen,message,x,y,font_s,clr):
    font = pygame.font.Font(None,font_s)
    text = font.render(message,True,clr)
    screen.blit(text,(x,y))
    pygame.display.update()


# make function for making random sentence  
def get_message()    :
    with open('sentence.txt','r',encoding='utf-8') as file:
        text = file.read()
        text_list = text.split('\n')
        sentence = random.choice(text_list)
        return sentence


#  function for display result
def result():
    total_time = time.time() - start_time
    number = 0
    for i , c in enumerate(sentence):
        try:
            if input_text[i] == c:
                number += 1
        except:
            pass    

    accuracy = number * 100 / len(sentence)        
    # text = f"time: {round(total_time)} seconds accuracy: {round(accuracy)}%"
    final_time = time.gmtime(total_time)
    text = f"time {final_time.tm_hour}:{final_time.tm_min}:{final_time.tm_sec}  accuracy: {round(accuracy)}%"
    print_text(win,text,50,20,40,(0,255,0))


sentence = get_message()
def start_game():
    print_text(win,sentence,50,200,40,(255,0,0))  
    pygame.draw.rect(win,(255,255,0),(30,250,750,60),3)
    pygame.display.update()



start_game()
# main loop
while True:
    win.fill((0,0,0),(35,255,740,40))
    # win.fill((0,0,0),(660,20,25,25))
    # print_text(win,str(time.localtime().tm_sec),650,20,40,(0,255,0))
    print_text(win,input_text,35,265,40,(255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            if (30 <= x <= 780)  and (250<= y <= 310):
                typing = True
                start_time = time.time()
                

        elif event.type == pygame.KEYDOWN:
            if typing:
                if event.key == pygame.K_RETURN:
                    result()
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]      
                else:
                    input_text += event.unicode      
    print_text(win,'Type Speed Program',70,100,100,(0,255,255))  
        
    pygame.display.update()        