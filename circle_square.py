import turtle

window = turtle.Screen()
window.bgcolor("red")

def create_square(dude):
    for i in range(1,5):
        dude.forward(100)
        dude.right(90)

def create_art():
    bot = turtle.Turtle()
    bot.speed(0)
    bot.color("yellow")
    for j in range(1,72):
        create_square(bot)
        bot.right(5)

    window.exitonclick()
    
create_art()
