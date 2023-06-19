import pygame ,  sys , time

pygame.init()

#define variables
x_display = 600
y_display = 600
caption = 'keyboard in pygame'
black = (0,0,0)
blue = (0,0,255)
purple = (0,255,255)
red = (255,0,0)
green = (0,255,0)

#create display
pygame.display.set_mode((x_display,y_display))
pygame.display.set_caption(caption)

# for i in range(1,800,50):
#     time.sleep(1)
#     x_display= i
#     y_display = i
#     pygame.display.set_mode((x_display,y_display))
#     pygame.display.update()
    


# check event 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # print(f'{event.unicode} key has been pressed') # event.unicode --> name character
            # print(f'{event.key} key has been pressed') # event.key --> ascii character
            if event.key == pygame.K_f:
                print(pygame.K_f , event.key)
                print('you press key',' f')

        # if event.type == pygame.KEYUP:
        #     print(f'{event.unicode} key has been released')    
        pygame.display.update()    
