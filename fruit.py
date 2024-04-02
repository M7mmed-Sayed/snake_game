from turtle import Turtle
import random


class Fruit(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("food.gif")
        self.speed("fastest")
        self.penup()
        self.eaten()

    def eaten(self):
        # using 14*20 to set the point at multiple of 20
        rand_x = random.randint(-14, 14) * 20
        rand_y = random.randint(-14, 14) * 20
        self.goto(rand_x, rand_y)
