import pygame , sys , random

pygame.init()

# variable for screen
width = 800
height = 600
typing = False
input_text = ''


win  = pygame.display.set_mode((width,height))
pygame.display.set_caption('Type speed checker')


# function for  display text in win
def print_text(screen,message,x,y,font_s,clr): # font_s --> font size , clr --> color
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
    

def start_game():
    text = get_message()
    print_text(win,text,50,200,40,(255,0,0))  
    pygame.draw.rect(win,(255,255,0),(30,250,750,60),3)
    pygame.display.update()



start_game()
# main loop
while True:
    win.fill((0,0,0),(35,255,740,40))
    print_text(win,input_text,35,265,40,(255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            if (30 <= x <= 780)  and (250<= y <= 310):
                typing = True
                

        elif event.type == pygame.KEYDOWN:
            if typing:
                if event.key == pygame.K_RETURN:
                    print(input_text)
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]      
                else:
                    input_text += event.unicode      
    print_text(win,'Type Speed Program',70,100,100,(0,255,255))  
        
    pygame.display.update()        