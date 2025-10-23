import turtle

turtle.Screen().bgcolor("aqua")
turtle.Screen().setup(400,600)

square=turtle.Turtle()

length=100
angle=90

for i in range(4):
    square.forward(length)
    square.right(angle)
turtle.done()