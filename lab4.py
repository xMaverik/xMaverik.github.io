import turtle

def draw_rectangle(length, width):
    i = 0
    while i < 2:
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)
        i += 1

draw_rectangle(100,50)

turtle.done()