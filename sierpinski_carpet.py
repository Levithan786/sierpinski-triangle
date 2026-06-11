"""Sierpinski Carpet - Standard recursive implementation and variations.
Variations include: colored levels, different division factors, probabilistic removal."""
import turtle
import sys

def draw_square(t, x, y, size):
    t.up()
    t.goto(x, y)
    t.down()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.up()

def carpet(t, x, y, size, depth, variation='standard'):
    if depth == 0:
        draw_square(t, x, y, size)
        return
    new_size = size / 3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                # Center gap - variation point
                if variation == 'probabilistic' and random.random() > 0.7:
                    carpet(t, x + i*new_size, y + j*new_size, new_size, depth-1, variation)
                continue
            carpet(t, x + i*new_size, y + j*new_size, new_size, depth-1, variation)

import random
if __name__ == "__main__":
    sys.setrecursionlimit(1000)
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    screen = turtle.Screen()
    screen.bgcolor('black')
    t.color('white')
    carpet(t, -300, -300, 600, 5, 'standard')
    screen.exitonclick()