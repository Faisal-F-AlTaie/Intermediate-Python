#2019-12-13

import turtle
import digits

GRID_SIZE = 16

wn = turtle.Screen()
wn.bgcolor('black')
turtle.setup(GRID_SIZE * 44, GRID_SIZE * 14)

LEFT_EDGE = wn.window_width() * -0.5 + (GRID_SIZE * 2)
TOP_EDGE = wn.window_height() * 0.5 - (GRID_SIZE * 2)

myrtle = turtle.Turtle()
myrtle.shapesize(0.5, 0.5)
myrtle.penup()
myrtle.speed(0)
myrtle.hideturtle()

myrtle.shape('circle')
myrtle.color("#404040")
for y in range(10):
    myrtle.setpos(LEFT_EDGE, TOP_EDGE - (y * GRID_SIZE))
    for x in range(40):
        myrtle.stamp()
        myrtle.forward(16)

myrtle.color("white")
myrtle.right(90)
for x in range(11):
    myrtle.setpos(LEFT_EDGE - 8 + (x * 4 * GRID_SIZE), TOP_EDGE + 8)
    myrtle.pendown()
    myrtle.forward(160)
    myrtle.penup()

myrtle.left(90)
for x in range(3):
    myrtle.setpos(LEFT_EDGE - 8, TOP_EDGE - (GRID_SIZE * 5 * x) + 8)
    myrtle.pendown()
    myrtle.forward(GRID_SIZE * 40)
    myrtle.penup()

#ROW ONE
myrtle.penup()
myrtle.shape('square')
myrtle.fillcolor('yellow')
myrtle.pencolor('yellow')
myrtle.setpos(LEFT_EDGE, TOP_EDGE)
digits.draw_zero(myrtle)
digits.draw_zero(myrtle)
digits.draw_one(myrtle)
digits.draw_one(myrtle)
digits.draw_two(myrtle)
digits.draw_two(myrtle)
digits.draw_three(myrtle)
digits.draw_three(myrtle)
digits.draw_four(myrtle)
digits.draw_four(myrtle)

#ROW TWO
myrtle.shape('circle')
myrtle.pencolor('red')
myrtle.fillcolor('red')
myrtle.setpos(LEFT_EDGE, TOP_EDGE - (GRID_SIZE * 5))
digits.draw_five(myrtle)
digits.draw_five(myrtle)
digits.draw_six(myrtle)
digits.draw_six(myrtle)
digits.draw_seven(myrtle)
digits.draw_seven(myrtle)
digits.draw_eight(myrtle)
digits.draw_eight(myrtle)
digits.draw_nine(myrtle)
digits.draw_nine(myrtle)

franklin = turtle.Turtle()
franklin.shapesize(0.5, 0.5)
franklin.fillcolor('blue')
franklin.pencolor('blue')
franklin.penup()
franklin.speed(0)
franklin.hideturtle()
franklin.setpos(LEFT_EDGE, TOP_EDGE - (GRID_SIZE * 10))
digits.draw_line(franklin, 40)

wn.exitonclick()
