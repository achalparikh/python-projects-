import turtle

window = turtle.Screen()
window.bgcolor("black")

s = turtle.Turtle()
s.shape("square")
s.color("pink")
    
def square():
    c = 0
    while (c < 4):
        s.forward(100)
        s.right(90)
        c = c + 1

def circleFromSquare():

    for i in range (0,36):
        square()
        s.right(10)
    window.exitonclick()

circleFromSquare()
