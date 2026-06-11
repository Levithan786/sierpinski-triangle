import turtle

def draw_sierpinski(t, order, size):
    """Recursively draw Sierpinski triangle."""
    if order == 0:
        # Draw a filled triangle
        t.begin_fill()
        for _ in range(3):
            t.forward(size)
            t.left(120)
        t.end_fill()
    else:
        size /= 2
        draw_sierpinski(t, order - 1, size)
        t.forward(size)
        draw_sierpinski(t, order - 1, size)
        t.backward(size)
        t.left(120)
        t.forward(size)
        t.right(120)
        draw_sierpinski(t, order - 1, size)
        t.left(120)
        t.backward(size)
        t.right(120)

def main():
    screen = turtle.Screen()
    screen.title("Sierpinski Triangle")
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.goto(-150, -100)
    t.pendown()
    draw_sierpinski(t, 6, 300)
    turtle.done()

if __name__ == "__main__":
    main()
