from turtle import Screen
from playground import PongScreen
from player_one import PlayerOne
from player_two import PlayerTwo
from pong_ball import PongBall

user = PlayerOne()
opponent = PlayerTwo()
pong_ball = PongBall()
play_ground = PongScreen()

screen = Screen()

screen.listen()
screen.onkeypress(user.up, "Up")
screen.onkeypress(user.down, "Down")

screen.onkeypress(opponent.up, "w")
screen.onkeypress(opponent.down, "s")


game_on = True

while game_on:
    ball_movment = 2
    pong_ball.move(ball_movment)

    if pong_ball.distance(opponent) < 15:
        ball_movment -= 4



screen.exitonclick()

