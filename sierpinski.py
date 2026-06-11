import turtle
import sys

def sierpinski(points, depth, t):
    if depth == 0:
        t.up()
        t.goto(points[0])
        t.down()
        for p in points[1:] + [points[0]]:
            t.goto(p)
        t.up()
    else:
        p1, p2, p3 = points
        m1 = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
        m2 = ((p2[0] + p3[0]) / 2, (p2[1] + p3[1]) / 2)
        m3 = ((p3[0] + p1[0]) / 2, (p3[1] + p1[1]) / 2)
        sierpinski([p1, m1, m3], depth - 1, t)
        sierpinski([p2, m2, m1], depth - 1, t)
        sierpinski([p3, m3, m2], depth - 1, t)

if __name__ == "__main__":
    sys.setrecursionlimit(2000)
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    screen = turtle.Screen()
    screen.bgcolor("white")
    points = [(-200, -150), (200, -150), (0, 200)]
    sierpinski(points, 6, t)
    screen.exitonclick()