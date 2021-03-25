#import a module
import turtle

# background screen
win=turtle.Screen()
win.title("pong game by pranjal")
win.bgcolor("black")
win.setup(width=800,height=600)
win.tracer(0)

#left paddle 
paddle_l=turtle.Turtle()
paddle_l.speed(0)
paddle_l.shape("square")
paddle_l.color("white")
paddle_l.shapesize(stretch_wid=5,stretch_len=1)
paddle_l.penup()
paddle_l.goto(-350,0)


#right paddle 

paddle_r=turtle.Turtle()
paddle_r.speed(0)
paddle_r.shape("square")
paddle_r.color("white")
paddle_r.shapesize(stretch_wid=5,stretch_len=1)
paddle_r.penup()
paddle_r.goto(350,0)

#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.2
ball.dy=0.2

#scoring
score_a=0
score_b=0
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A:0  Player B:0",align="center",font=("couier",24,"normal"))

# functions to move left paddle
def paddle_l_up():
    y=paddle_l.ycor()
    y+=20
    paddle_l.sety(y)

def paddle_l_down():
    y=paddle_l.ycor()
    y-=20
    paddle_l.sety(y)
win.listen()
win.onkeypress(paddle_l_up,"w")
win.onkeypress(paddle_l_down,"s")

#functions to move right paddle
def paddle_r_up():
    y=paddle_r.ycor()
    y+=20
    paddle_r.sety(y)

def paddle_r_down():
    y=paddle_r.ycor()
    y-=20
    paddle_r.sety(y)

#keyboard     
win.onkeypress(paddle_r_up,"Up")
win.onkeypress(paddle_r_down,"Down")


#game loop
while True:
    win.update()
    #moving the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    #controlling ball movement 
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
    if ball.ycor()< -290:
        ball.sety(-290)
        ball.dy*=-1
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        score_a+=1
        pen.clear()
        pen.write("Player A:{}  Player B:{}".format(score_a,score_b),align="center",font=("couier",24,"normal"))
    if ball.xcor()< -390:
        ball.goto(0,0)
        ball.dx*=-1
        score_b+=1
        pen.clear()
        pen.write("Player A:{}  Player B:{}".format(score_a,score_b),align="center",font=("couier",24,"normal"))
    #paddle and ball collisions
    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor() < paddle_r.ycor()+40 and ball.ycor()> paddle_r.ycor()-40):
        ball.setx(340)
        ball.dx*=-1
    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor() < paddle_l.ycor()+40 and ball.ycor()> paddle_l.ycor()-40):
        ball.setx(-340)
        ball.dx*=-1
    
    

    
