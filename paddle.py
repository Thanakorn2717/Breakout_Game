from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=7)
        self.color("white")
        self.penup()
        self.y_move = 10
        self.goto(-4, -250)

    def go_left(self):
        new_x = self.xcor() - 40
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 40
        self.goto(new_x, self.ycor())

    def reset_position(self):
        self.goto(-4, -250)


