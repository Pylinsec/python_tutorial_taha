import pygame , sys , time

pygame.init()
size = (780,600)
color=(255, 128, 0)
rect_w = 0
rect_h = 0
speed = 60
win = pygame.display.set_mode(size)
pygame.display.set_caption('bodobodo')

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    win.fill((0,0,0))
    pygame.draw.rect(win,color,((rect_w,rect_h),(60,60)))
    time.sleep(0.05)
    if rect_w < 720 and rect_h == 0:
       rect_w += 60
    if rect_w == 720 and rect_h < 540:
       rect_h += 60
    if rect_w >0  and rect_h == 540:
       rect_w -= 60
    if rect_w == 0  and rect_h > 0:
       rect_h -= 60
    pygame.display.update() 
