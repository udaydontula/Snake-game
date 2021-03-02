from turtle import Turtle, Screen

screen = Screen()


POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):

        self.segment = []
        self.create_snake()

    def create_snake(self):

        for i in POSITION:
            self.add_segment(i)

    def add_segment(self, i):

        t = Turtle(shape="square")
        t.color("white")
        t.penup()
        t.goto(i)
        self.segment.append(t)

    def reset(self):
        for seg in self.segment:
            seg.goto(1000, 1000)
        self.segment.clear()
        self.create_snake()

    def extend_segment(self):

        self.add_segment(self.segment[-1].position())

    def move(self):

        for seg in range(len(self.segment)-1, 0, -1):
            x = self.segment[seg - 1].xcor()
            y = self.segment[seg - 1].ycor()
            self.segment[seg].goto(x, y)
        self.segment[0].fd(20)

    def snake_up(self):

        if self.segment[0].heading() != 270:
            self.segment[0].setheading(90)
            self.move()

    def snake_down(self):

        if self.segment[0].heading() != 90:
            self.segment[0].setheading(270)
            self.move()

    def snake_right(self):

        if self.segment[0].heading() != 180:
            self.segment[0].setheading(0)
            self.move()

    def snake_left(self):

        if self.segment[0].heading() != 0:
            self.segment[0].setheading(180)
            self.move()
