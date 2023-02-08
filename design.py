import turtle,time
turtle.bgcolor("green")
s=turtle.Turtle()
s.speed(20)
s.pencolor("orange")
s.hideturtle()
for i in range(400):
	s.circle(i)
	s.left(40)
time.sleep(10)

