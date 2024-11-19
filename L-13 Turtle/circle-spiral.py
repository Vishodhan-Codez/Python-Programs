import turtle
turtle.Screen().bgcolor("black")
turtle.Screen().setup(400,400)
t=turtle.Turtle()
t.speed(30)
for i in range(0,5) :
    t.circle(50)
    t.goto()
turtle.hideturtle()
turtle.done()