from turtle import Turtle, Screen
import random

def wow_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    color = (r, b, g)
    return color

ahad = Turtle()
screen = Screen()
ahad.speed("fastest")
def draw(x):
    for _ in range(int(360/x)):
        ahad.circle(100)
        # ahad.pensize(15)
        ahad.color(wow_color())
        ahad.setheading(ahad.heading() + x)

def close_window(x, y):
    screen.bye()

draw(10)  # Call draw function initially

screen.onclick(close_window)  # Bind close_window function to the screen's onclick event
screen.mainloop()  # Keeps the window open until manually closed
