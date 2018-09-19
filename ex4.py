#https://www.geeksforgeeks.org/turtle-programming-python/
import turtle  #Inside_Out
wn = turtle.Screen()
wn.bgcolor("black")
cr = turtle.Turtle()
cr.color("lime green")

def sqrfunc(size):
	for i in range(360):
		cr.fd(size)
		cr.left(91)
		cr.backward(91)
		cr.forward(91)
		cr.speed(i)
		
		
		size = size + 2

sqrfunc(100)
sqrfunc(101)
sqrfunc(102)
sqrfunc(103)
sqrfunc(104)
sqrfunc(105)
sqrfunc(106)
sqrfunc(107)
holdit = input(50);
