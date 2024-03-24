from turtle import Turtle, Screen
import random

def close_window(x, y):
    screen.bye()

ahad = Turtle()
screen = Screen()

def draw():
    for _ in range(200):
        arr = [0, 90, 270]
        color_names = ['blue', 'green', 'red', 'cyan', 'yellow', 'magenta']
        col = random.choice(color_names)
        wow = random.choice(arr)
        ahad.color(col)
        ahad.setheading(wow)
        ahad.width(15)  # '15' to 15
        ahad.forward(10)

draw()  # Call draw function initially

screen.onclick(close_window)  # Bind close_window function to the screen's onclick event
screen.mainloop()  # Keeps the window open until manually closed
