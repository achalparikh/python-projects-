import turtle


window = turtle.Screen()
window.bgcolor("black")


def funnel():

    #draws a funnel line by line

    line = turtle.Turtle()
    line.shape("circle")
    line.color("yellow")
    line.speed(2)
    
    line.forward(100)
    line.left(120)
    
    line.forward(100)
    line.right(30)
    
    line.forward(100)
    line.left(90)
    
    line.forward(40)
    line.left(90)

    line.forward(100)
    line.right(30)

    line.forward(100)
    line.right(240)

    line.forward(50)

def square():
    square = turtle.Turtle()
    square.shape("square")
    square.color("green")
    square.speed(2)

    counter = 0

    while (counter <= 3):
        square.forward(100)
        square.right(90)
        counter = counter + 1

def circle ():
    circle = turtle.Turtle()
    circle.shape("circle")
    circle.color("pink")
    circle.speed(2)

    circle.circle(100)

def triangle():
    tri = turtle.Turtle()
    tri.shape("triangle")
    tri.color("blue")
    tri.speed(2)
    

    counter = 0
    while (counter < 3):
        tri.backward(100)
        tri.left(120)
        counter = counter + 1
    
def draw():
    triangle()
    funnel()
    square()
    circle()
    window.exitonclick()

draw()
