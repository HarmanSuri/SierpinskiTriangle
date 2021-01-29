"""sierpinski_triangle.py
Author: Harman Suri
Nov 15, 2020

Description:    Draws the Sierpinski Triangle fractal by using the turtle
                module and recursion.
"""

import turtle

# creates new turtle
drawer = turtle.Turtle()

# height and width of screen
h = 600
w = 600

# creates new screen with custom width and height
screen = turtle.Screen()
screen.setup(width=w, height=h)

# makes screen not re-sizable
screen.cv._rootwindow.resizable(False, False)


def draw_triangle(level, ax, ay, bx, by, cx, cy):
    """Based on a level and 3 points, the sierpinski triangle is drawn to a certain iteration
    using a recursive function that draws 3 new triangles based on the midpoints of the old triangle.

    Args:
        level: specify which iteration to draw the sierpinski triangle.

        ax, ay, bx, by, cx, cy: x and y coordinates of the three points needed to form a triangle
    """
    if level <= 1:
        # final triangle when level is 1
        drawer.penup()
        drawer.goto(ax, ay)
        drawer.pendown()
        drawer.goto(bx, by)
        drawer.goto(cx, cy)
        drawer.goto(ax, ay)
    else:
        drawer.penup()
        # AB midpoint
        abMidX = (ax + bx) / 2
        abMidY = (ay + by) / 2

        # BC midpoint
        bcMidX = (bx + cx) / 2
        bcMidY = (by + cy) / 2

        # CA midpoint
        caMidX = (cx + ax) / 2
        caMidY = (cy + ay) / 2

        # main triangle at current level
        drawer.goto(ax, ay)
        drawer.pendown()
        drawer.goto(bx, by)
        drawer.goto(cx, cy)
        drawer.goto(ax, ay)

        # draw 3 new triangles based of midpoints of the current triangle
        draw_triangle(level - 1, ax, ay, abMidX, abMidY, caMidX, caMidY)
        draw_triangle(level - 1, bx, by, bcMidX, bcMidY, abMidX, abMidY)
        draw_triangle(level - 1, cx, cy, caMidX, caMidY, bcMidX, bcMidY)


# sets turtle speed to max
drawer.speed("fastest")

# asks user for the iteration of sierpinski triangle
iteration = int(
    input("What iteration of the sierpinski triangle would you like to see?"))

# triangles initial coordinates are based on the width and height of the screen to get a perfect triangle
draw_triangle(iteration, 0, h - 400, -w + 400, -h + 450, w - 400, -h + 450)

# return turtle to origin
drawer.penup()
drawer.goto(0, 0)
turtle.done()
