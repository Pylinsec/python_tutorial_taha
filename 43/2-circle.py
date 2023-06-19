import pygame,sys , time

pygame.init()
size = (800,600)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
black = (0,0,0)
white = (255,255,255)
win = pygame.display.set_mode(size)
pygame.display.set_caption('circle') # dadan name be panjereh 
# pygame.draw.circle(surface , color,location , radius, width)
# location --> mokhtasat markaz dayerh hast
# radius --> andazeh shoaa hast ke int , float mitone bashe
# width --> zekhamat --> hadaksar possesh andazeh shoaa 

for i in range(1,750,23):
    for j in range (1 , 550,21):
        a = pygame.draw.circle(win , blue,(i,j) ,9,0)
        print(a)
        if (a[0] + a[1]) % 2 == 0:
            a = pygame.draw.circle(win , blue,(i,j) ,9,-1)
            time.sleep(.25)
            pygame.display.update()





while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()    