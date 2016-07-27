import turtle

def two_turtle():
    window = turtle.Screen()
    window.bgcolor("yellow")
    venki = turtle.Turtle()
    venki.color("red")
    venki.shape("turtle")
    venki.speed(1)
    i=0
    while i<3:
        venki.forward(180)
        venki.left(120)
        i = i+1
    window.exitonclick()

    
two_turtle()
    
