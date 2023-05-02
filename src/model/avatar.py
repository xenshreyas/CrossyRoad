from turtle import Turtle

MOVE_SPEED = 12


# Represents the avatar in the game
class Avatar(Turtle):
    def __init__(self):
        super().__init__("turtle")
        self.penup()
        self.setheading(90)
        self.goto(0, -280)
        self.color("blue")
        self.speed = MOVE_SPEED

    def move_up(self):
        self.seth(90)
        self.forward(self.speed)

    def move_down(self):
        if self.ycor() > -280:
            self.seth(270)
            self.forward(self.speed)

    def move_left(self):
        if self.xcor() > -280:
            self.seth(180)
            self.forward(self.speed)

    def move_right(self):
        if self.xcor() < 280:
            self.seth(0)
            self.forward(self.speed)

    def reset_position(self):
        self.goto(0, -280)

    def increase_speed(self):
        self.speed += 1