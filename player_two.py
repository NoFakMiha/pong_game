from turtle import Turtle
#Player one settings

PT_SHAPE = "square"
PT_COLOR = "white"
PT_SIZE_WIDTH = 8
PT_SIZE_LENGTH = 1
PT_SIZE_OUTLINE = 0
PT_START_X = +720
PT_START_Y = 0
PT_SPEED = 0

class PlayerTwo:

    def __init__(self):
        self.player_two = Turtle(PT_SHAPE)
        self.player_two.color(PT_COLOR)
        self.player_two.hideturtle()
        self.player_two.speed(PT_SPEED)
        self.player_two.penup()
        self.player_two.goto(x=PT_START_X, y=PT_START_Y)
        self.player_two.showturtle()
        self.player_two.shapesize(stretch_wid=PT_SIZE_WIDTH, stretch_len=PT_SIZE_LENGTH, outline=PT_SIZE_OUTLINE)

    def up(self):
        positon_y = self.player_two.ycor()
        positon_y += 20
        self.player_two.goto(x=PT_START_X, y=positon_y)

    def down(self):
        positon_y = self.player_two.ycor()
        positon_y -= 20
        self.player_two.goto(x=PT_START_X, y=positon_y)