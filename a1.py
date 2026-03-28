import turtle
turtle.Screen().bgcolor("lightgreen")
turtle.Screen().setup(600,600)
poly = turtle.Turtle()

side = 8
lenn = 100
angle = 360.0 / side
for i in range(side):
    poly.forward(lenn)
    poly.left(angle)

turtle.done()