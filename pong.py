#!/usr/bin/env python3
import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong by Marcio Freitas")
wn.bgcolor("black")
wn.setup(800,600)
wn.tracer(1)

class player():
	def __init__(self, color, shape, x, y):
		self._player = turtle.Turtle()
		self._player.color(color)
		self._player.shape(shape)
		self._player.speed(0)
		self._player.shapesize(stretch_wid=5, stretch_len=1)
		self._player.penup()
		self._player.goto(x, y)

	def move_up(self):
		y = self._player.ycor()
		y += 20
		self._player.sety(y)

	def move_down(self):
		y = self._player.ycor()
		y -= 20
		self._player.sety(y)

	def get_x(self):
		return self._player.xcor()

	def get_y(self):
		return self._player.ycor()		

class ball():
	def __init__(self, color, shape, x, y):
		self._ball = turtle.Turtle()
		self._ball.speed(0)
		self._ball.color(color)
		self._ball.shape(shape)
		self._ball.penup()
		self._ball.goto(x, y)
		self.dx = 1
		self.dy = 1

	def move_ball(self):
		self._ball.sety(self._ball.ycor() + self.dy)
		self._ball.setx(self._ball.xcor() + self.dx)

	def change_y_dir(self):
		self.dy *= -1

	def change_x_dir(self):
		self.dx *= -1

	def get_x(self):
		return self._ball.xcor()

	def get_y(self):
		return self._ball.ycor()		

class score():
	def __init__(self, color):
		self._pen = turtle.Turtle()
		self._pen.speed(0)
		self._pen.color(color)
		self._pen.penup()
		self._pen.hideturtle()
		self._pen.goto(0, 250)
		self._pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))	
		self.score_p1 = 0
		self.score_p2 = 0

	def p1_goal(self):
		self.score_p1 += 1
		self._pen.clear()
		self._pen.write(f"Player A: {self.score_p1} Player B: {self.score_p2}", align="center", font=("Courier", 24, "normal"))

	def p2_goal(self):
		self.score_p2 += 1
		self._pen.clear()
		self._pen.write(f"Player A: {self.score_p1} Player B: {self.score_p2}", align="center", font=("Courier", 24, "normal"))	


player1 = player("white", "square", -350, 0)
player2 = player("white", "square", 350, 0)	
ball1 = ball("white", "square", 0, 0)
score1 = score('white')

wn.listen()
wn.onkeypress(player1.move_up, "w")
wn.onkeypress(player1.move_down, "s")
wn.onkeypress(player2.move_up, "Up")
wn.onkeypress(player2.move_down, "Down")

while True:
	wn.update()
	ball1.move_ball()
	# reflect ball if it reaches the top/botton bounderies
	if abs(ball1.get_y()) >= 290:
		ball1.change_y_dir()
		winsound.PlaySound("bounce.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

	# repositioning the ball at center if a goal is scored
	if abs(ball1.get_x()) > 390:
		if ball1.get_x() > 0:
			score1.p1_goal()
		else:
			score1.p2_goal()

		ball1._ball.goto(0,0)
		ball1.change_x_dir()

	# reflect the ball if it reaches any player
	if abs(ball1.get_x()) > 335 and abs(ball1.get_x()) < 350:
		if ball1.get_y() <= (player1.get_y() + 50) and ball1.get_y() >= (player1.get_y() - 50):
			ball1.change_x_dir()

		if ball1.get_y() <= (player2.get_y() + 50) and ball1.get_y() >= (player2.get_y() - 50):
			ball1.change_x_dir()

		winsound.PlaySound("bounce.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)		
