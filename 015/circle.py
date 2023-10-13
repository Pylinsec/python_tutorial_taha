from turtle import *
pensize(2)
speed(0)
colors=["blue","yellow","pink","#B23AEE","aqua","brown"]
for k in range (5):
    lt(134)
    fd(200)
    for i in range (6):
        rt(10)
        for color in colors:
            pencolor(color)
            circle(40)
            rt(10)
