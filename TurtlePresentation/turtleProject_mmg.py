import turtle
import random



def setup():
    tk = turtle
    t = turtle.Turtle()
    tp = turtle.pos()
    sun_size = 864337 / 10000 # diameter of the sun, and planets divided by 10000, and 1000 for scale.
    earth_size = 7917 / 1000
    moon_size = 2159 / 1000
    jupiter_size = 86881 / 1000
    mercury_size = 3032 / 1000
    venus_size = 7520 / 1000
    mars_size = 4212 / 1000
    running = True
    tk.setup(width=1920, height=1080)
    tk.ht()
    tk.bgcolor("black")
    tk.title("Mason's Turtle")
    tk.speed(0)


def mason():
    setup()
    i = 1 #call setup function
    tk.pu()
    tk.goto(0,-200/2)
    tk.color("white") #color white
    tk.pd() #pen down
    tk.circle(200/2) #draw circle
    tk.pu() #pen up
    tk.goto(0, -300/2) #go to coordinates
    tk.color("white") #draw circle
    tk.pd() #pen down
    tk.circle(300/2) #draw circle
    tk.pu() #pen up
    tk.goto(0, -400/2) #go to coordinates
    tk.pd()
    tk.circle(400/2)
    tk.pu()
    tk.goto(0, -500/2)
    tk.pd()
    tk.circle(500/2)
    tk.pu()
    tk.goto(0,-600/2)
    tk.color("white") #color white
    tk.pd() #pen down
    tk.circle(600/2) #draw circle
    tk.pu() #pen uptk = turtle
    tk.goto(0, -700/2) #go to coordinates
    tk.color("white") #draw circle
    tk.pd() #pen down
    tk.circle(700/2) #draw circle
    tk.pu() #pen up
    tk.goto(0, -800/2) #go to coordinates
    tk.pd()
    tk.circle(800/2)
    tk.pu()
    tk.goto(0, -900/2)
    tk.pd()
    tk.circle(900/2)tk = turtle
t = turtle.Turtle()
tp = turtle.pos()
sun_size = 864337 / 10000 # diameter of the sun, and planets divided by 10000, and 1000 for scale.
earth_size = 7917 / 1000
moon_size = 2159 / 1000
jupiter_size = 86881 / 1000
mercury_size = 3032 / 1000
venus_size = 7520 / 1000
mars_size = 4212 / 1000
running = True
    tk.pu()

    tk.goto(0, -85)
    tk.pd()
    tk.color("yellow")
    tk.begin_fill()
    tk.circle(sun_size)
    tk.end_fill()
    tk.pu()
    tk.goto(0, -103)
    tk.pd()tk = turtle
t = turtle.Turtle()
tp = turtle.pos()
sun_size = 864337 / 10000 # diameter of the sun, and planets divided by 10000, and 1000 for scale.
earth_size = 7917 / 1000
moon_size = 2159 / 1000
jupiter_size = 86881 / 1000
mercury_size = 3032 / 1000
venus_size = 7520 / 1000
mars_size = 4212 / 1000
running = True
    tk.color("red")
    tk.begin_fill()
    tk.circle(mercury_size)
    tk.end_fill()
    tk.pu()
    tk.goto(0, -155)
    tk.pd()
    tk.color("brown")
    tk.begin_fill()
    tk.circle(venus_size)tk = turtle
t = turtle.Turtle()
tp = turtle.pos()
sun_size = 864337 / 10000 # diameter of the sun, and planets divided by 10000, and 1000 for scale.
earth_size = 7917 / 1000
moon_size = 2159 / 1000
jupiter_size = 86881 / 1000
mercury_size = 3032 / 1000
venus_size = 7520 / 1000
mars_size = 4212 / 1000
running = True
    tk.end_fill()
    tk.pu()
    tk.goto(0, -208)
    tk.pd()
    tk.color("blue")
    tk.begin_fill()
    tk.circle(earth_size)
    tk.end_fill()
    tk.pu()
    tk.goto(0, -253)tk = turtle
t = turtle.Turtle()
tp = turtle.pos()
sun_size = 864337 / 10000 # diameter of the sun, and planets divided by 10000, and 1000 for scale.
earth_size = 7917 / 1000
moon_size = 2159 / 1000
jupiter_size = 86881 / 1000
mercury_size = 3032 / 1000
venus_size = 7520 / 1000
mars_size = 4212 / 1000
running = True
    tk.pd()
    tk.color("red")
    tk.begin_fill()
    tk.circle(mars_size)
    tk.end_fill()

#    tk.pu()
#    tk.goto(300, -90)
#    tk.pd()
#    tk.color("brown")
#    tk.begin_fill()
#    tk.circle(65)
#    tk.end_fill()


    #for i in range(360):

        #a = -random.random() * -random.random() * 100
        #b = random.random() * random.random() * 100
        #tk.begin_fill()
        #tk.circle(100)
        #tk.end_fill()
        #print(a)
    tk.exitonclick() #exit on click

mason()  #call main function
