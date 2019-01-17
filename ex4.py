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
		cr.speed(50)
		
		
		size = size + 2

sqrfunc(0)
sqrfunc(25)
sqrfunc(50)
sqrfunc(75)
sqrfunc(100)
sqrfunc(125)
sqrfunc(150)
sqrfunc(175)
sqrfunc(200)
holdit = input(225)
