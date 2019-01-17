import tkinter as tk
import turtle
def star(t,x,y):
    t.goto(x,y)
    for angle in range (0,360,15):
        t.color("#c4ff00")
        t.width(8)
        t.forward(150)
        t.color("#000000")
        t.width(1)
        t.back(150)
        t.right(angle)

def outloop(t,angle):
    tk.pu() #pen uptk = turtle
    for i in range (1,21):
        t.forward(20)
        t.right(angle)

def backloop(t,angle):
    for i in range (1,21):
        t.forward(20)
        t.left(angle)

def outloop(t,angle):
    for i in range (1,21):
        t.forward(20)
        t.left(angle)

def backloop(t,angle):
    for i in range (1,21):
        t.forward(20)
        t.left(angle)

def poly(t,size,x,y,color):
    t.width(3)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(color)
    for i in range (1,31):
        t.forward(size)
        t.right(12)

def ace():
    tw = turtle.Screen()
    tw.clear()
    t = turtle.Turtle()
    t.width(10)
    # *******************
    t.speed(1)
    t.width(12)
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.color("#ff1ac6")
    outloop(t,12)
    # *******************
    t.speed(1)
    t.width(12)
    t.goto(100,-100)
    t.color("#00ddb5")
    backloop(t,12)
    # *******************
    t.speed(1)
    t.width(12)
    t.goto(-100,-100)
    t.color("#00ff00")
    outloop(t,12)
    # ******************
    t.width(12)
    t.goto(0,0)
    t.color("#7700dd")
    t.penup()
    t.goto(20,-50)
    t.goto(20,-50)
    t.pendown()
    star(t,10,-50)
    tw.exitonclick()

#ace()
