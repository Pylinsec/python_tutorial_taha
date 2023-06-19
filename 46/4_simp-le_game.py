import pygame , sys , time

pygame.init()
size = (600,600)
color=(255, 128, 0)
rect_x = 0
rect_y = 0
speed = 60
win = pygame.display.set_mode(size)
pygame.display.set_caption('bodobodo')

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        win.fill((0,0,0))
        pygame.draw.rect(win,color,((rect_x,rect_y),(60,60)))
        if event.type == pygame.KEYDOWN:
        # w --> up  x --> down d--> right    a --> left
            if event.key == pygame.K_a and rect_x > 0:
                rect_x -= speed
            if event.key == pygame.K_w and rect_y > 0:
                rect_y -= speed
            if event.key == pygame.K_d and rect_x < 540 :
                rect_x += speed
            if event.key == pygame.K_x and rect_y < 540:
                rect_y += speed
    

    pygame.display.update() 
