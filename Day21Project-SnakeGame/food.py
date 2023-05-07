from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.color(random.choice(["blue", "red", "yellow", "purple", "white"]))
        self.refresh()

    def refresh(self):
        random_x_position = random.randint(-270, 270)
        random_y_position = random.randint(-270, 270)
        self.goto(random_x_position, random_y_position)

