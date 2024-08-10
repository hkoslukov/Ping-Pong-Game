import turtle

wn = turtle.Screen()
wn.title('Pong By HK')
wn.bgcolor('green')
wn.setup(width=1280, height=720)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color('red')
paddle_a.penup()
paddle_a.goto(-620, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color('blue')
paddle_b.penup()
paddle_b.goto(620, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 300)
player_a = 0
player_b = 0
pen.write('Player A: {} Player B: {}'.format(player_a, player_b), align='center', font=('Courier', 28, 'normal'))


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


def paddle_b_left():
    x = paddle_b.xcor()
    x -= 20
    paddle_b.setx(x)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_up, 'W')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_a_down, 'S')
wn.onkeypress(paddle_b_down, 'Down')
wn.onkeypress(paddle_b_up, 'Up')

wn.onkeypress(paddle_b_left, 'Left')


# Main Game Loop
while True:
    wn.update()

    # Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 350:
        ball.sety(350)
        ball.dy *= -1


    elif ball.ycor() < -350:
        ball.sety(-350)
        ball.dy *= -1

    if ball.xcor() > 630:
        player_a += 1
        ball.goto(0, 0)
        ball.dx *= -1
        pen.clear()
        pen.write('Player A: {} Player B: {}'.format(player_a, player_b), align='center',
                  font=('Courier', 28, 'normal'))
    if ball.xcor() < -630:
        player_b += 1
        ball.goto(0, 0)
        ball.dx *= -1
        pen.clear()
        pen.write('Player A: {} Player B: {}'.format(player_a, player_b), align='center',
                  font=('Courier', 28, 'normal'))

    # Paddle and ball collisions
    if (ball.xcor() > 600 and ball.xcor() < 610) and (ball.ycor() < paddle_b.ycor() + 50
                                                      and ball.ycor() > paddle_b.ycor() - 50):

        ball.dx *= -1

    elif (ball.xcor() < -600 and ball.xcor() > -610) and (ball.ycor() < paddle_a.ycor() + 50
                                                      and ball.ycor() > paddle_a.ycor() - 50):

        ball.dx *= -1
