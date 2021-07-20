import turtle

turtle.speed(7)
turtle.bgcolor("black")

for i in range(5):
    for colours in ["Red", "Cyan", "Green", "Orange", "Blue", "Lime", "Light Blue"]:
        turtle.color(colours)
        turtle.pensize(3)
        turtle.lt(12)
        for i in range(4):
            turtle.fd(200)
            turtle.lt(90)
turtle.done()
