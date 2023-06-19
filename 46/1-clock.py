import pygame , sys , time
from tkinter import colorchooser

# color =  colorchooser.askcolor(title='rang')
# print(color[0])
pygame.init()
#font ya heman text
# fonts = pygame.font.get_fonts()
# for font in fonts:
#     print(font)
# print(len(fonts))

# font haye dakheli
size = (800,600)
color_font=(255, 128, 0)
win = pygame.display.set_mode(size)
pygame.display.set_caption('text and font')
# revesh avval --> estefadeh az font haye system
# font = pygame.font.SysFont('Arial',120) # font dakhlei 

# revesh dovvom --> estefadeh az font delkhah 
# font = pygame.font.Font(None,120) # khodesh font pishfarz mizareh
font = pygame.font.Font('DS-DIGI.TTF',80) # khodesh font pishfarz mizareh

# text = 'First Game'
# te
# text = '18:35:21'
# text = time.strftime('%H:%M:%S')
# text_surface = font.render(text,True,color , bgcolor(ekhtiari))
# text_surface = font.render(text,True,color_font)
# text_surface = font.render(text,False,color_font)
# False --> matn ya font lebedar hast  True --> font matn ma saf hast

while 1:
    # time.sleep(1)
    # text = time.strftime('%A %C-->%H:%M:%S') # just time 
    text = time.strftime('%T') # just time 
    # text = time.ctime() # date and time 
    win.fill((0,0,0))
    text_surface = font.render(text,True,color_font)
    win.blit(text_surface,(100,200))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()    