import pygame , sys , time

pygame.init()
size = (1000,600)
color=(255, 128, 0)
fox_x = 500
fox_y = 400
speed = 60
win = pygame.display.set_mode(size,flags=pygame.HIDDEN)
pygame.display.set_caption('bodobodo')
# define background
bg = pygame.image.load('newbg.jpg')
BG = pygame.transform.scale(bg,(1000,600))

# define fox
fox = pygame.image.load('fox.png')
FOX = pygame.transform.scale(fox,(80,80))


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        win.blit(BG,(0,0))
        win.blit(FOX,(fox_x,fox_y))
        if event.type == pygame.KEYDOWN:
        # w --> up  x --> down d--> right    a --> left
            if event.key == pygame.K_a and fox_x > 60:
                fox_x -= speed
            if event.key == pygame.K_w and fox_y > 60:
                fox_y -= speed
            if event.key == pygame.K_d and fox_x < 920 :
                fox_x += speed
            if event.key == pygame.K_x and fox_y < 520:
                fox_y += speed
    

    pygame.display.update() 
