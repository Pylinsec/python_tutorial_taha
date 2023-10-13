from turtle import *
pensize(2)
speed(0)
color("red","black")
for j in range(72):
    rt(5)
    begin_fill()
    for i in range(5):
        fd(100)
        rt(144)
        fd(100)
        lt(72)
    end_fill()
hideturtle()

