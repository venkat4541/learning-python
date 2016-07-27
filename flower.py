import turtle

window = turtle.Screen()
window.bgcolor("red")

def create_diamond(dude):
    for i in range(1,3):
        dude.forward(30)
        dude.right(40)
        dude.forward(30)
        dude.right(140)

def create_art():
    bot = turtle.Turtle()
    bot.speed(0)
    bot.color("yellow")
    for j in range(1,31):
        create_diamond(bot)
        bot.right(12)

    window.exitonclick()
    
create_art()
