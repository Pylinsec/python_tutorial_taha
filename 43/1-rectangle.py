import pygame,sys , time

pygame.init()
size = (800,600)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
black = (0,0,0)
white = (255,255,255)
win = pygame.display.set_mode(size)
pygame.display.set_caption('First Game') # dadan name be panjereh 
win.fill(white)

# pygame.draw.rect(surface , color,(mokhtasat shoroo ,size),width)
# surface heman panjereh hast
# color --> rang 
# mokhrtasat shoroo(x,y) --> tuple bashe 
# size ---> andzazeh tool , arz mostatil -->. tuple bashe
# width --> zekhamat khat dor mostatil 

# pygame.draw.rect(win ,red,((0,500),(100,50)),25)# --. dar soorat zekhamt khat nesf tool ya arz bedim shekl kamel az rang por mishevad 
color_list = [red , blue , black , (255,255,0)]
for i in range(1,770,30):# x
    for j in range(1,570,29): # --> y
        win.fill(white)
        a = pygame.draw.rect(win ,color_list[j % 4],((i,j),(20,15)),100)
        print(f"l-tool --> {a[0]},l-arz-->{a[1]},s-tool --> {a[2]},s-arz-->{a[3]}") # l--> location , s--> size
        time.sleep(0.25)
        pygame.display.update()
        print(pygame.event.get())
        if pygame.event.get() == 256:
            pygame.quit()
            sys.exit()





while True:
    for event in pygame.event.get():
        print(pygame.QUIT)
        if event.type == pygame.QUIT:
            print()
            pygame.quit()
            sys.exit()
        pygame.display.update()    