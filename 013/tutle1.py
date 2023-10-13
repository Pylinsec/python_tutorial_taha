# import turtle as t
# t.circle(50)
#  intor import kardan dardesar darad
from turtle import *
# pensize(5)
# color=["green","red","yellow"]
# for i in range(3):
#     pencolor(color[i])
#     left(60)
#     forward(-200) # forward(tool khat bar asas pixel) backward() or back()
#     left(-90) # left(angle) and right(angle bar asas derejeh)
#     forward(-200)
#     left(-90)
#     forward(-200)
#     left(-90)
#     forward(-200)

# import turtle as t
# t.circle(50)
#  intor import kardan dardesar darad

pensize(5)
color=["green","red","yellow"]
for i in range(3):
    pencolor(color[i])
    forward(300)
    right(120)
    for i in range(5):
        forward(100)
        right(144)
        write("star")

hideturtle()

