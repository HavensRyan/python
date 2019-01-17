import turtle

def ryan():
	t = turtle.Turtle()
	w = turtle.Screen()
	#t.shape("turtle")
	w.bgcolor("grey")
	t.pensize(10)
	t.color("red")

	for i in range(12):
		t.color("#00d9ff")
		t.begin_fill()
		t.rt(90)
		t.fd(200)
		t.lt(120)
		t.fd(200)
		t.lt(120)
		t.fd(200)
		t.color("#830505")
		t.end_fill()
		t.fd(200)
	w.exitonclick()
#ryan()
