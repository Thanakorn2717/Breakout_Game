from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.y_move = 10
        self.x_move = random.choice([-10, 10])
        self.move_speed = 0.1
        self.goto(-4, -229)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

        if int(self.xcor()) <= -360 or int(self.xcor()) >= 350:
            self.bounce_x()
        elif int(self.ycor()) >= 300:
            self.bounce_y()

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def speed_up(self):
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(-4, -229)
        self.move_speed = 0.1
        self.bounce_y()
