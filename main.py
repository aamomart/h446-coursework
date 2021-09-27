from collision import rectCollision
import turtle

colour = 'white'

x1 = 20
y1 = 30
w1 = 20
h1 = 20

x2 = 30
y2 = 20
w2 = 20
h2 = 20

if rectCollision(x2, y2, w2, h2, x1, y1, w1, h1):
    colour = 'red'
else:
    colour = 'green'

t = turtle.Turtle()

t.hideturtle()

t.penup()

t.forward(x1)
t.left(90)
t.forward(y1)
t.forward(h1/2)

t.pendown()

t.fillcolor(colour)
t.begin_fill()

t.right(90)
t.forward(w1/2)
t.right(90)
t.forward(h1)
t.right(90)
t.forward(w1)
t.right(90)
t.forward(h1)
t.right(90)
t.forward(w1/2)
t.right(90)

t.penup()

t.forward(h1/2 + y1)
t.right(90)
t.forward(x1)
t.right(180)
t.forward(x2)
t.left(90)
t.forward(y2 + h2/2)
t.right(90)

t.pendown()

t.fillcolor(colour)
t.begin_fill()

t.forward(w2/2)
t.right(90)
t.forward(h2)
t.right(90)
t.forward(w2)
t.right(90)
t.forward(h2)
t.right(90)
t.forward(w2/2)


turtle.done()