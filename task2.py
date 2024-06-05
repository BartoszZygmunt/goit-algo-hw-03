import turtle
import argparse

def koch_curve(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        length /= 3
        koch_curve(t, length, depth-1)
        t.left(60)
        koch_curve(t, length, depth-1)
        t.right(120)
        koch_curve(t, length, depth-1)
        t.left(60)
        koch_curve(t, length, depth-1)

def koch_snowflake(t, length, depth):
    for _ in range(3):
        koch_curve(t, length, depth)
        t.right(120)

def main():
    parser = argparse.ArgumentParser(description="Koch snowflake fractal visualizer.")
    parser.add_argument("depth", type=int, help="Level of recursion")
    args = parser.parse_args()

    window = turtle.Screen()
    window.title("Koch Snowflake")
    t = turtle.Turtle()
    t.speed(0)  # Max speed

    length = 300  # Length of the sides of the snowflake
    t.penup()
    t.goto(-length / 2, length / 3)
    t.pendown()

    koch_snowflake(t, length, args.depth)

    turtle.done()

if __name__ == "__main__":
    main()
