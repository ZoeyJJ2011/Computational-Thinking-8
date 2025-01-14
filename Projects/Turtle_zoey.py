#beginning
import turtle


t = turtle.Turtle()
#middle
t.goto(100, 0)
colors =["light blue","yellow","pink"]


for i in range(5):
    t.color( colors[ i % 3 ])
    t.forward(100)
    t.left(72)


turtle.exitonclick()
#end