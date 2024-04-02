from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.goto(0, 275)
        self.update_scoreboard()
        self.hideturtle()

    def snake_ate(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f" Score : {self.score}", align="center", font=("Arial", 14, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over Your Score : {self.score}", align="center", font=("Arial", 14, "bold"))
