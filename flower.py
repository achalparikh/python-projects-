import turtle

window = turtle.Screen()
window.bgcolor("black")

circle = turtle.Turtle()
circle.shape("arrow")
circle.color("pink")
circle.speed(100)
    
def flower1():
    counter = 0

    while (counter < 36):
        circle.circle(20)
        circle.right(10)
        counter = counter + 1

def flower2 ():
    c = 0
    while (c < 3):
        circle.right(90)
        circle.forward(51)
        flower1()
        c = c + 1

    
def draw():
    flower1()
    flower2()
    window.exitonclick()

draw()
