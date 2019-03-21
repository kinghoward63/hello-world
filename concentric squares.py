#Dante Howard
#2/28/2019

# Drawns a set of concentric squares

import turtle
def drawSquare(t, sz):
    for i in range (4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()

dante = turtle.Turtle()
dante.color("blue")

size = [20, 40, 60, 80, 100]

for x in size:
    drawSquare(dante, x)
    dante.penup()
    dante.backward(10)
    dante.right(90)
    dante.forward(10)
    dante.left(90)
    dante.pendown()

#drawSquare (dante,100)

wn.exitonclick()
