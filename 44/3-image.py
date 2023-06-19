import pygame , sys ,time


size = (800,600)
white =(255,255,255)
yellow =(255,255,0)
black =(0,0,0)
red =(255,0,0)
green = (0,255,0)
blue =(0,0,255)
pi = 3.14159

win = pygame.display.set_mode(size)
pygame.display.set_caption('image')


#  first --> make icon 
img = pygame.image.load('icon.jpg')
print(img)
pygame.display.set_icon(img)

#  second --> image for background 
bg = pygame.image.load('horse2.bmp') # jpg , png , bmp , gif , ico 
# win.blit(bg,(0,0))

BG = pygame.transform.scale(bg,(800,600))
win.blit(BG,(0,0))

#  third --> image on bg 

sheep = pygame.image.load('sheep.jpg')
# win.blit(sheep,(250,300))
new_sheep = pygame.transform.scale(sheep,(100,120))
win.blit(new_sheep,(250,300))


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()        