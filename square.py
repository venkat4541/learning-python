import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")   
    brad = turtle.Turtle()
    brad.speed(1)
    x=0
    while x<4:
        brad.forward(100)
        brad.right(90)
        x = x+1
    
    
draw_square()
    
