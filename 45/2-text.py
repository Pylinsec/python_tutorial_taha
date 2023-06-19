import pygame , sys , time
from tkinter import colorchooser

# color =  colorchooser.askcolor(title='rang')
# print(color[0])
pygame.init()
size = (800,600)
color_font=(255, 128, 0)
win = pygame.display.set_mode(size)
pygame.display.set_caption('text and font')
font = pygame.font.Font('DS-DIGI.TTF',80) # khodesh font pishfarz mizareh

text = 'First Game'
# text = time.strftime('%H:%M:%S')
text_surface = font.render(text,True,color_font)
win.blit(text_surface,(100,100))
# t_r = text_surface.get_rect() # gereftan fezaye mostetily
# t_r.topleft = (100,100)
# win.blit(text_surface,t_r)


while 1:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()    