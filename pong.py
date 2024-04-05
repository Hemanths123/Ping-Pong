from turtle import Turtle, Screen


class Pong(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.turtlesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(x, y)

    def up(self):
        new_y = self.ycor() + 20
        new_x = self.xcor()
        self.goto(x=new_x, y=new_y)

    def down(self):
        new_y = self.ycor() - 20
        new_x = self.xcor()
        self.goto(x=new_x, y=new_y)
