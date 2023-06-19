import pygame, sys 

pygame.init()
width = 800
height = 800
white = (255, 255, 255)
cyan = (0, 255, 255)
x_rect = 0
y_rect = 0
speed = 10
fps = 100

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("FirstProject")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    window.fill(white)
    pygame.draw.rect(window,cyan,(x_rect,y_rect,100,100))
    if (x_rect < 700 ) and (y_rect == 0):
        x_rect += speed
    if (y_rect <= 700) and (x_rect == 700):
        y_rect += speed
    if (x_rect >= 0) and (y_rect == 700):
        x_rect -= speed
    if (y_rect >= 0) and (x_rect == 0):
        y_rect -= speed
    pygame.display.update() 
    clock.tick(fps)