from turtle import Screen
import time
import snake
import food
import scoreboard


s = snake.Snake()
f = food.Food()
score = scoreboard.Score()
screen = Screen()


screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("| Snake_Game |")
screen.tracer(0)
screen.listen()
screen.onkey(fun=s.snake_up, key="Up")
screen.onkey(s.snake_down, "Down")
screen.onkey(s.snake_right, "Right")
screen.onkey(s.snake_left, "Left")


game = True
while game:
    screen.update()
    time.sleep(0.1)
    s.move()

    # Detecting Collision with Food

    if s.segment[0].distance(f) < 15:
        f.refresh()
        score.update_score()
        s.extend_segment()

    # Detecting Collision with Wall

    if s.segment[0].xcor() > 290 or s.segment[0].xcor() < -290 or s.segment[0].ycor() > 290 or s.segment[0].ycor() < -290:
        # game = False
        score.reset()
        s.reset()

    for seg in s.segment[1:]:
        if s.segment[0].distance(seg) < 1:
            # game = False
            score.reset()
            s.reset()

screen.exitonclick()
