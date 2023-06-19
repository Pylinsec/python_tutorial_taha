import pygame , sys ,time


size = (400,600)
white =(255,255,255)
yellow =(255,255,0)
black =(0,0,0)
red =(255,0,0)
green = (0,255,0)
blue =(0,0,255)
pi = 3.14159

win = pygame.display.set_mode(size)
pygame.display.set_caption('line')
# win.fill(white)

# pygame.draw.circle(win,red,(100,100),50,50)
# pygame.draw.arc(win,blue,(location,diameter1 ,diameter2),angel 1 be radian , angel 2 be radian,w)  # diameter --> qotr hast 
# pygame.draw.arc(win,blue,(200,200,100 ,100),0, pi,2) 
while 1:
    win.fill(black) 
    pygame.draw.arc(win,blue,(200,200,300 ,200),0, pi/2,5)
    pygame.display.flip()
    time.sleep(.25)
    win.fill(black) 
    pygame.draw.arc(win,red,(200,200,300 ,200),pi/2, pi,5) 
    pygame.display.flip()
    time.sleep(.25)
    win.fill(black)
    pygame.draw.arc(win,white,(200,200,300 ,200),pi,3*pi/2,5) 
    pygame.display.flip()
    time.sleep(.25) 
    win.fill(black)
    pygame.draw.arc(win,green,(200,200,300 ,200),3 * pi/2,2 * pi,5) 
    pygame.display.flip()
    time.sleep(.25) 

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()        