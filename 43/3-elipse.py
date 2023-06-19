import pygame,sys

pygame.init()
size = (800,600)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
black = (0,0,0)
white = (255,255,255)
win = pygame.display.set_mode(size)
pygame.display.set_caption('baizi') # dadan name be panjereh 
# pygame.draw.ellipse(surface, color , (l_x , l-y ,andaze qotre bozorg , andzazeh qotr koochak),w)
# l-x --> tool noqteh markaz baizi
# l-y --> arz noqteh markaz baizi
# 
a = pygame.draw.ellipse(win, white , (200, 300,40 , 60),20)
print(a)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()    