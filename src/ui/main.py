from turtle import Screen
import time

from src.model.avatar import Avatar
from src.model.obstacle import Obstacle
from src.model.level import Level

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Crossy Road")
screen.colormode(255)

obstacle = Obstacle()
level = Level()
avatar = Avatar()

screen.listen()
screen.onkey(avatar.move_up, "w")
screen.onkey(avatar.move_left, "a")
screen.onkey(avatar.move_down, "s")
screen.onkey(avatar.move_right, "d")
screen.onkey(screen.bye, "Escape")

game_is_on = True
while game_is_on:
    obstacle.move()
    screen.update()
    time.sleep(0.05)

    if avatar.ycor() > 280:
        avatar.reset_position()
        level.increase_level()
        obstacle.speed += 1
        obstacle.create_car(0)

    for coin in obstacle.coins:
        if coin.distance(avatar) < 20:
            coin.hideturtle()
            obstacle.coins.remove(coin)
            avatar.increase_speed()

    for car in obstacle.cars:
        if car.distance(avatar) < 20:
            game_is_on = False
            level.clear()
            level.goto(0, 0)
            level.color("red")
            level.goto(0, 0)
            level.write("Game Over", align="center", font=("Courier", 24, "normal"))

screen.exitonclick()
