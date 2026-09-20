"""
SHAPE DRAWER - built with the turtle module
==============================================
Teaching sequence:
  STAGE 1: Draw one square using a loop
  STAGE 2: Generalize into a function draw_shape(sides, length)
  STAGE 3: Let the user type in the number of sides
  STAGE 4: Add color choices
  STAGE 5 (stretch): Draw spirals / stars by changing the turn angle

turtle comes built into Python - no install needed.
"""

import turtle


def setup_screen():
    screen = turtle.Screen()
    screen.title("Shape Drawer")
    screen.bgcolor("white")
    return screen


def draw_shape(pen, sides, length, color="black"):
    """
    STAGE 2: The key generalization step.
    A regular polygon with N sides always turns by (360 / N) degrees
    at each corner. This ONE formula is what lets a square, triangle,
    pentagon, hexagon etc. all use the same function.
    """
    pen.color(color)
    turn_angle = 360 / sides
    for _ in range(sides):
        pen.forward(length)
        pen.right(turn_angle)


def draw_star(pen, length, color="red"):
    """
    STAGE 5 (stretch): A 5-point star uses a sharper turn (144 degrees)
    so the lines cross over each other instead of forming a closed polygon.
    Encourage students to experiment with different angles here.
    """
    pen.color(color)
    for _ in range(5):
        pen.forward(length)
        pen.right(144)


def draw_spiral(pen, sides, length, growth, color="blue"):
    """
    STAGE 5 (stretch): Same turning idea as draw_shape, but the side
    length grows a little each time, so the shape spirals outward.
    """
    pen.color(color)
    turn_angle = 360 / sides
    current_length = length
    for _ in range(sides * 6):  # loop several times around to make it spiral
        pen.forward(current_length)
        pen.right(turn_angle)
        current_length += growth


def main():
    screen = setup_screen()
    pen = turtle.Turtle()
    pen.speed(4)

    # STAGE 3: ask the user what to draw
    print("Shape Drawer")
    print("1. Regular polygon (choose number of sides)")
    print("2. Star")
    print("3. Spiral")
    choice = input("Choose an option (1/2/3): ").strip()

    # STAGE 4: color choice
    color = input("Choose a color (e.g. red, blue, green): ").strip() or "black"

    if choice == "1":
        sides = int(input("How many sides? (3-10 works well): "))
        length = int(input("Side length? (try 100): "))
        draw_shape(pen, sides, length, color)
    elif choice == "2":
        length = int(input("Side length? (try 150): "))
        draw_star(pen, length, color)
    elif choice == "3":
        sides = int(input("Base number of sides? (try 5): "))
        length = int(input("Starting length? (try 10): "))
        draw_spiral(pen, sides, length, growth=2, color=color)
    else:
        print("Invalid choice, drawing a default square.")
        draw_shape(pen, 4, 100, color)

    screen.exitonclick()  # keeps the window open until clicked


if __name__ == "__main__":
    main()
