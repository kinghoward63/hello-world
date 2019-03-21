#Dante Howard

import turtle          # set up alex
wn = turtle.Screen()
alex = turtle.Turtle()

sideNumber = int(input("How many sides for your polygon?"))
sideLength = int(input("what is the length per side?"))

angle = 360 / sideNumber 

for aColor in range(sideNumber):
    alex.forward(sideLength)
    alex.left(angle)

wn.exitonclick()
