# Faisal Al- taie
# Computing Science 10
# Henry Wise Wood School
# 2021-2022 semester 1
# October 14th, 2021

# import turtle library
import turtle

# set vansh as our variable
vansh = turtle.Turtle()

# set values
x = 0
y = 0
b = "black"

# creation of rows
for c in range(8):
    vansh.penup()
    vansh.goto(x, y)
    vansh.pendown()
    vansh.speed(0)

    for r in range(8):

        # filling in colour.
        # if the colum is divisible by 0 and the colum is divisible by 0 square is white
        if c % 2 == 0 and r % 2 == 0:
            vansh.fillcolor(b)
            vansh.begin_fill()

        # if the colum is not divisible by 0 and the row is not divisible by 0 then the square is black
        elif c % 2 == 1 and r % 2 == 1:
            vansh.fillcolor(b)
            vansh.begin_fill()

            #  drawing square
        for s in range(5):
            vansh.forward(50)
            if s != 4:
                vansh.right(90)

        # end the filling of colour
        vansh.end_fill()

    # moving downwards
    y -= 50


