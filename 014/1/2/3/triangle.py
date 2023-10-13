from turtle import *
bgcolor("black")
pensize(3)
for colors in ["yellow","blue","red","pink","navy","Tomato","aqua",
"green","yellow","blue","red",
"pink","navy","Tomato","aqua","green","yellow","blue",
"red","pink","yellow","blue","red","pink","navy","Tomato","aqua","green","yellow","blue","red","pink",
"navy","Tomato","aqua","green"]:
    pencolor(colors)
    lt(10)
    for i in range(3):
        lt(120)
        fd(200)
