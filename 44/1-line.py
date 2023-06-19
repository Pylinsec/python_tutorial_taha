import pygame , sys 


size = (400,600)
white =(255,255,255)
yellow =(255,255,0)
black =(0,0,0)
red =(255,0,0)
blue =(0,0,255)


win = pygame.display.set_mode(size)
pygame.display.set_caption('line')
win.fill(white)

# pygame.draw.line(surface,color,(x-start , y-start),(x-end , y-end), width)
#  start --> noghteh shoroo   , end --> neghte payan 

# pygame.draw.line(win,blue,(100 ,20),(100 , 200),5) #--> kayfiet in bishatr hast 
# pygame.draw.aaline(win,red,(30 ,20),(30 , 200)) # width fegat 1 hast  w --> blind

# lines
pygame.draw.lines(win,red,True,((30 ,20),(60 , 200),(150,360),(240,300)),5) # True --> vasl mikonad ebteda be noghte entehei
# pygame.draw.aalines(win,red,True,((30 ,20),(60 , 200),(150,360),(240,300)),0) # True --> vasl mikonad ebteda be noghte entehei
# False --> vasl nemikonad ebteda be enteha 



while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()        