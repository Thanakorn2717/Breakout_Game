from turtle import Turtle, Screen
from box import Box
from paddle import Paddle
from ball import Ball
import tkinter as tk
from tkinter import messagebox
import time

game_is_on = False
count_point = 0

root = tk.Tk()
root.withdraw()  # Hide the root window
start = messagebox.askyesno("Breakout Game", "Start the game?")
root.destroy()

screen = Screen()
screen.setup(width=750, height=600)
screen.bgcolor("black")
screen.title("Breakout-Game")
screen.tracer(0)

box_1 = Box(-300, 280)
box_2 = Box(-152, 280)
box_3 = Box(-4, 280)
box_4 = Box(144, 280)
box_5 = Box(292, 280)

box_6 = Box(-300, 250)
box_7 = Box(-152, 250)
box_8 = Box(-4, 250)
box_9 = Box(144, 250)
box_10 = Box(292, 250)

box_11 = Box(-300, 220)
box_12 = Box(-152, 220)
box_13 = Box(-4, 220)
box_14 = Box(144, 220)
box_15 = Box(292, 220)

box_list = [box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9,
            box_10, box_11, box_12, box_13, box_14, box_15]

goto_pos = [(-300, 280), (-152, 280), (-4, 280), (144, 280), (292, 280),
            (-300, 250), (-152, 250), (-4, 250), (144, 250), (292, 250),
            (-300, 220), (-152, 220), (-4, 220), (144, 220), (292, 220)]

paddle = Paddle()
ball = Ball()

screen.listen()
screen.onkey(paddle.go_left, "a")
screen.onkey(paddle.go_right, "d")

# print(f"distance = {ball.distance(paddle)}")
# print(f"ball x core = {ball.xcor()}")
# print(f"ball y core = {ball.ycor()}")
# print(f"paddle x core = {paddle.xcor()}")
# print(f"paddle y core = {paddle.ycor()}")

if start:
    game_is_on = True

    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        for item in box_list:
            if (20.0 <= ball.distance(item) <= 72) and (item.ycor() - ball.ycor() < 30):
                ball.bounce_y()
                ball.speed_up()
                item.disappear()
                count_point += 1

        if (20.0 <= ball.distance(paddle) <= 72) and (paddle.ycor() - ball.ycor() > -30):
            ball.bounce_y()

        if count_point == 15:
            restart = messagebox.askyesno("Breakout Game", "You win! Do you want to restart?")
            if restart is False:
                screen.bye()
                game_is_on = False
            else:
                for box, pos in zip(box_list, goto_pos):
                    box.goto(pos[0], pos[1])
                    box.recolor()

                ball.reset_position()
                paddle.reset_position()
                count_point = 0

        if ball.ycor() < -300:
            restart = messagebox.askyesno("Breakout Game", "Game over! Do you want to restart?")
            if restart is False:
                screen.bye()
                game_is_on = False
            else:
                for box, pos in zip(box_list, goto_pos):
                    box.goto(pos[0], pos[1])
                    box.recolor()

                ball.reset_position()
                paddle.reset_position()
                count_point = 0
        
    screen.exitonclick()
