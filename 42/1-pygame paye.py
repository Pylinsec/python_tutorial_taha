import pygame ,sys, time
#  keyboard , joystick , mouse , mouse motion   --> asas kar pygame 
# pygame.init()

display_size = (600,600)
white = (255,255,255) 
black= (0,0,0)
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
gray = (127,127,127)
yellow = (255,255,0)
magenta = (255 ,0,255)
cyan = (0 ,255,255)
color_list = [black , white,gray,red,blue , cyan, magenta,yellow,green]
win = pygame.display.set_mode(display_size) # dadan size display
win.fill(white)
pygame.display.update() # flip()  --> har do yekar anjam midan



# revesh avval jehat khoroj bedon error az panjardh pygame  
# while 1:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: #  event.type --> adadi ke ba asas kar ma bargardande mishe 
#             # pygame.QUIT --> ADAD 256 
#             pygame.quit()
#             sys.exit()
# revesh 2 jehat khoroj bedon error az panjardh pygame    
running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False   
        for color in color_list:
            win.fill(color)    
            pygame.display.flip()#--> update()=flip()
            time.sleep(1)
        pygame.quit()
        running = False      


