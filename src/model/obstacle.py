from turtle import Turtle
import random


# Represents the vehicle in the game
def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return tuple((r, g, b))


class Obstacle(Turtle):
    def __init__(self):
        super().__init__("square")
        self.penup()
        self.speed = 5
        self.cars = []
        self.coins = []

        for i in range(0, 10):
            self.create_car(0)

    def create_car(self, x_cor):
        car = Turtle("square")
        car.color(generate_random_color())
        car.penup()
        car.shapesize(stretch_wid=1, stretch_len=random.randrange(2, 5))
        car.setheading(180)
        if x_cor == 0:
            car.goto(random.randint(-250, 250), random.randint(-250, 250))
        else:
            car.goto(x_cor, random.randint(-250, 250))
        car.speed = self.speed
        self.cars.append(car)

    def move(self):

        for car in self.cars:
            car.forward(car.speed)

            if car.xcor() < -320:
                car.hideturtle()
                self.cars.remove(car)
                self.create_car(280)

                coin = random.randint(1, 20)
                if coin == 1:
                    self.create_coin()

                for coin in self.coins:
                    coin.forward(coin.speed)

                    if coin.xcor() < -320:
                        coin.hideturtle()
                        self.coins.remove(coin)

    def create_coin(self):
        coin = Turtle("circle")
        coin.color("yellow")
        coin.penup()
        coin.shapesize(stretch_wid=0.3, stretch_len=0.3)
        coin.setheading(180)
        coin.goto(300, random.randint(-250, 250))
        coin.speed = self.speed / 2
        self.coins.append(coin)
