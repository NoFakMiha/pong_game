from turtle import Turtle
from player_two import PlayerTwo

class PongBall(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self, ball_movment):
        self.fd(ball_movment)



