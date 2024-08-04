from turtle import Turtle
import random

BOX_COLOR = ["red", "green", "blue", "orange", "purple"]


class Box(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=7)
        self.color(random.choice(BOX_COLOR))
        self.penup()
        self.goto(x, y)

    def disappear(self):
        self.goto(500, 500)

    def recolor(self):
        self.color(random.choice(BOX_COLOR))



