# Making imports
from random import choice
from turtle import Screen, Turtle
from tkinter import *
import tkinter.messagebox
import sys

# Setting up the screen
screen = Screen()
screen.setup(600, 600)
screen.title("My AWESOME Game")

# Setting up the constant's for the game
turtle_lst = []
col_pos = ["red", "blue", "grey", "black", "green", "purple"]
move_lst = [0, 10, 5, 15, 20, 0]
cv = screen.getcanvas()

# Function for the random colors
def color_funk():
    color_pick = col_pos.pop()
    return color_pick

# Spawning turtles
def turtle_spawn():
    for i in range(6):
        turtle = Turtle()
        turtle.penup()
        turtle.speed(0)
        turtle.setheading(90)
        turtle.shape("turtle")
        turtle.color(color_funk())
        turtle.goto(positions())
        turtle_lst.append(turtle)

# Moving turtles into the positions
def positions():
    x_pos = 200
    y_post = -250
    for _ in range(len(turtle_lst)):
        x_pos -= 80
    pots = (x_pos, y_post)
    return pots

# Initial push
def move_forward():
    for element in turtle_lst:
        move_y = choice(move_lst)
        element.forward(move_y)

# Game starts HERE!
def game_start():
    turtle_spawn()
    for _ in range(80):
        for item in turtle_lst:
            if item.ycor() <= 240:
                move_forward()
            else:
                clr = item.color()
                tkinter.messagebox.showinfo("And the winner is...", f"{str(clr[0]).title()} WINS!")
                sys.exit()


game_start()
screen.exitonclick()
