import pygame, sys, random

# variable display size
win_w, win_h = 900 , 600
pygame.init()
win = pygame.display.set_mode((win_w, win_h))
pygame.display.set_caption('type speed')

# define variable 
input_text = ''
#  define function for write text in display
def print_text(screen,message,font_size,color,x,y):
    font = pygame.font.Font(None,font_size)
    font_render = font.render(message,True,color)
    screen.blit(font_render,(x,y))
    pygame.display.update()


# define function for make random sentence 
def make_setence():
    with open('sentence.txt','r') as file:
        text = file.read()
        text_list = text.split('\n')
        sentence = random.choice(text_list)
        return sentence
    

#  define function for start game
def start_game():
    new_sentence = make_setence()
    print_text(win,new_sentence,40,(255,0,0),100,250)
    pygame.draw.rect(win,(255,255,0),(50,300,800,80),5)
    pygame.display.update()
  
start_game()    
        

#  main loop 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
                # K_RETURN heman enter vesat keyboard
                # K_KP_ENTER heman enter dar keypad ya kelid haye mashin hesab
            if event.key == pygame.K_RETURN:
                print(input_text)
                # tarhai kar backspace
            if event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]    
            else:
                # zekhireh kelid heye feshorde shode 
                input_text += event.unicode    
    # win.fill(color,rect)--> (rang,(mokhtesat sohro,size))
    win.fill((0,0,0),(55,310,790,65)) 
     #    chap input_text
    print_text(win,input_text,30,(255,255,255),60,325)
    # print type speed 
    print_text(win,'Type Speed',150,(0,255,255),180,70)

    pygame.display.update()