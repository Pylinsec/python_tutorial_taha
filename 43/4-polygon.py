import pygame,sys

pygame.init()
size = (800,600)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
black = (0,0,0)
white = (255,255,255)
win = pygame.display.set_mode(size)
pygame.display.set_caption('polygon') # dadan name be panjereh 

# pygame.draw.polygon(win,red,((10,250),(30,300),(100,220),(400,410),(500,550)),0)
pygame.draw.polygon(win,red,((400,100),(400,200),(500,250),(600,200),(600,100),(500,50)),0)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()    