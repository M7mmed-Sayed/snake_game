from turtle import Screen, Turtle

from fruit import Fruit
from score import Score
from snake import Snake
import time

WIDTH = 280
HEIGHT = 280

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("white")
screen.title("my Game")
screen.tracer(0)
image_path = "headsnake.gif"
screen.addshape("food.gif")
screen.addshape(image_path)
snake = Snake()
fruit = Fruit()
scoreboard = Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_over = False

while not game_over:
    screen.update()
    time.sleep(.09)
    snake.move()

    # check if you eat the fruit
    if snake.head.distance(fruit) < 15:
        fruit.eaten()
        scoreboard.snake_ate()
        snake.extend()

    if snake.head.xcor() > screen.window_width() or snake.head.xcor() < - screen.window_width()  or snake.head.ycor() > screen.window_height() or snake.head.ycor() < -screen.window_height():
        game_over = True
        scoreboard.game_over()

    for seg in snake.segments:
        if snake.head == seg:
            continue

        if snake.head.distance(seg) < 14:
            game_over = True
            scoreboard.game_over()



screen.exitonclick()
