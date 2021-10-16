from turtle import Turtle
#Player one settings

PO_SHAPE = "square"
PO_COLOR = "white"
PO_SIZE_WIDTH = 8
PO_SIZE_LENGTH = 1
PO_SIZE_OUTLINE = 0
PO_START_X = -720
PO_START_Y = 0
PO_SPEED = 0

class PlayerOne:

    def __init__(self):
        self.player_one = Turtle(PO_SHAPE)
        self.player_one.color(PO_COLOR)
        self.player_one.hideturtle()
        self.player_one.speed(PO_SPEED)
        self.player_one.penup()
        self.player_one.goto(x=PO_START_X, y=PO_START_Y)
        self.player_one.showturtle()
        self.player_one.shapesize(stretch_wid=PO_SIZE_WIDTH, stretch_len=PO_SIZE_LENGTH, outline=PO_SIZE_OUTLINE)

    def up(self):
        positon_y = self.player_one.ycor()
        positon_y += 20
        self.player_one.goto(x=PO_START_X, y=positon_y)

    def down(self):
        positon_y = self.player_one.ycor()
        positon_y -= 20
        self.player_one.goto(x=PO_START_X, y=positon_y)