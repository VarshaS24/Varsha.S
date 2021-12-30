import turtle as t
import os

# Score varibales

player_a_score = 0
player_b_score = 0

win = t.Screen()
win.title("Ding Dong") 
win.bgcolor('blue')    
win.setup(width=800,height=600) 
win.tracer(0)   

# Creating left paddle for the game

paddle_left = t.Turtle()
paddle_left.speed(0)
paddle_left.shape('square')
paddle_left.color('red')
paddle_left.shapesize(stretch_wid=5,stretch_len=1)
paddle_left.penup()
paddle_left.goto(-380,0)

# Creating a right paddle for the game

paddle_right = t.Turtle()
paddle_right.speed(0)
paddle_right.shape('square')
paddle_right.shapesize(stretch_wid=5,stretch_len=1)
paddle_right.color('red')
paddle_right.penup()
paddle_right.goto(380,0)

# Creating a  ball for the game

ball = t.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('yellow')
ball.penup()
ball.goto(0,0)
ball_dx = 0.3  
ball_dy = 0.3

# Creating a pen for updating the Score

pen = t.Turtle()
pen.speed(0)
pen.color('black')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0                    Player B: 0 ",align="center",font=('Arial',24,"normal"))


# Moving the left Paddle up

def paddle_left_up():
    y = paddle_left.ycor()
    y = y + 15
    paddle_left.sety(y)

# Moving the left paddle down

def paddle_left_down():
    y = paddle_left.ycor()
    y = y - 15
    paddle_left.sety(y)

# Moving the right paddle up

def paddle_right_up():
    y = paddle_right.ycor()
    y = y + 15
    paddle_right.sety(y)

# Moving right paddle down

def paddle_right_down():
    y = paddle_right.ycor()
    y = y - 15
    paddle_right.sety(y)

# Keyboard binding

win.listen()
win.onkeypress(paddle_left_up,"q")
win.onkeypress(paddle_left_down,"a")
win.onkeypress(paddle_right_up,"Up")
win.onkeypress(paddle_right_down,"Down")




# Main Game Loop

while True:
    win.update() 

    # Moving the ball
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)

    # setting up the border

    if ball.ycor() > 290:   
        ball.sety(290)
        ball_dy = ball_dy * -1
        
    
    if ball.ycor() < -290:  
        ball.sety(-290)
        ball_dy = ball_dy * -1
        

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball_dx = ball_dx * -1
        player_a_score = player_a_score + 1
        pen.clear()
        pen.write("Player A: {}                    Player B: {} ".format(player_a_score,player_b_score),align="center",font=('Arial',24,"normal"))
        os.system("afplay wallhit.wav&")



    if(ball.xcor()) < -390: 
        ball.goto(0,0)
        ball_dx = ball_dx * -1
        player_b_score = player_b_score + 1
        pen.clear()
        pen.write("Player A: {}                    Player B: {} ".format(player_a_score,player_b_score),align="center",font=('Arial',24,"normal"))
        os.system("afplay wallhit.wav&")


    # Handling the collisions with paddles.

    if(ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < paddle_right.ycor() + 40 and ball.ycor() > paddle_right.ycor() - 40):
        ball.setx(340)
        ball_dx = ball_dx * -1
        os.system("afplay paddle.wav&")

    if(ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < paddle_left.ycor() + 40 and ball.ycor() > paddle_left.ycor() - 40):
        ball.setx(-340)
        ball_dx = ball_dx * -1
        os.system("afplay paddle.wav&")
