import turtle

def draw():
    window = turtle.Screen()
    window.bgcolor("black")
    draw_init()
    window.exitonclick()

def draw_init():
    brad = turtle.Turtle()
    brad.shape("triangle")
    brad.color("orange")
    brad.speed(100)

    brad.rt(90)
    brad.forward(100)
    brad.lt(90)
    brad.forward(50)

    brad.penup()
    brad.forward(50)
    brad.lt(90)

    brad.pendown()
    brad.forward(100)
    brad.rt(90)
    
    for i in range (0,2):  
        brad.forward(30)
        brad.rt(60)
        brad.forward(20)
        brad.rt(30)
        brad.forward(15)
        brad.rt(30)
        brad.forward(20)
        brad.rt(60)
        brad.forward(30)
        brad.rt(180)

    brad.penup()
    brad.goto(-100,-100)
    

draw()
