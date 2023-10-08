import turtle
def ractangle(color):
    turtle.begin_fill()
    turtle.fillcolor(color)
    for i in range(2):
        turtle.forward(300)
        turtle.right(90)
        turtle.forward(200)
        turtle.right(90)
    turtle.end_fill()
def circle(color):
    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.circle(-70)
    turtle.end_fill()

turtle.up()
turtle.goto(0, -200)
turtle.down()
turtle.goto(0, 200)
ractangle('green')

turtle.goto(0,170)
turtle.color('green')
turtle.forward(150)
circle('red')

turtle.exitonclick()
