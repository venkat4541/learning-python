import turtle

def two_turtle():
    window = turtle.Screen()
    window.bgcolor("yellow")
    uppi = turtle.Turtle()
    venki = turtle.Turtle()
    uppi.speed(1)
    uppi.color("red")
    uppi.shape("circle")
    uppi.circle(40)
    uppi.right(90)
    uppi.shape("triangle")
    uppi.forward(40)
    uppi.circle(60)
    uppi.right(180)
    uppi.color("blue")
    uppi.shape("circle")
    uppi.circle(60)
    venki.speed(1)
    venki.color("red")
    venki.shape("circle")
    venki.circle(40)
    venki.right(90)
    venki.shape("triangle")
    venki.forward(40)
    venki.circle(60)
    venki.right(180)
    venki.color("blue")
    venki.shape("circle")
    venki.circle(60)
    window.exitonclick()
    
two_turtle()
    
