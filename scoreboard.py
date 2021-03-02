from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super(Score, self).__init__()
        self.penup()
        self.score = 0
        with open("/Users/dell/Desktop/score.txt") as file:
            self.highscore = int(file.read())
        self.goto(0, 280)
        self.color("white")
        self.write(f"Your Score : {self.score}  High Score : {self.highscore}", False, align="center",
                   font=("Arial", 12, "normal"))
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Your Score : {self.score}  High Score : {self.highscore}", False, align="center",
                   font=("Arial", 12, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("--- GAME OVER ---", False, align="center", font=("Arial", 12, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("score.txt", mode="w") as file:
                file.write(str(self.highscore))

        self.score = 0
        self.update_score()
