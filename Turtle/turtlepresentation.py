import turtle
wn = turtle.Screen()
wn.bgcolor("dark grey")

for i in range(360):

    trip = turtle.Turtle()
trip.color("red")
trip.pensize("5")
trip.speed("100")
for i in range(1,11):
        trip.forward(10)
        trip.right(5)
        trip.backward(10)
        trip.right(5)
