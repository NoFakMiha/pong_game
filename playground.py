from turtle import Screen, Turtle
# Screen settings
BG_COLOR = "black"
SCREEN_WIDTH = 1500
SCREEN_HEIGHT= 800

# Turtle settings
TT_COLOR = "white"
TT_TURN_LEFT = 90
X_START = 0
Y_START = - 370
TT_SPEED = 0
TT_PENSIZE= 5


class PongScreen:

    def __init__(self):
        self.turtle = Turtle()
        self.turtle.color(TT_COLOR)
        self.turtle.left(TT_TURN_LEFT)
        self.turtle.penup()
        self.turtle.goto(x=X_START, y=Y_START )
        self.turtle.speed(TT_SPEED)
        self.turtle.pensize(TT_PENSIZE)
        self.turtle.hideturtle()

        for _ in range(19):
            self.turtle.pendown()
            self.turtle.fd(20)
            self.turtle.penup()
            self.turtle.fd(20)

        self.screen = Screen()
        self.screen.bgcolor(BG_COLOR)
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)



