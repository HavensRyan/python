# plot-dictionary.py
import tkinter as tk
import turtle

def main():
    #table is a dictionary
    table = {110:-220,-100:200,90:-180,-80:160,70:-140,-60:120,50:-100,
                -40:80,30:-60,-20:40,10:-20,0:0,
                      -10:20,20:-40,-30:60,40:-80,-50:100,
                      60:-120,-70:140,80:-160,-90:180,100:-200,-110:220

          }
    print(" KEYS ")
    print(table.keys())
    print(" VALUES ")
    print(table.values())
    #turtle graphics
    twin = turtle.Screen()
    twin.clear()
    t = turtle.Turtle()
    #tWin = turtle.Screen()
    for h,k in table.items():   #get the items in the dictionary
        print(h, k) # trace code
        #x,y = table[n]
        t.penup()
        t.goto(h,k)
        t.pendown()
        t.circle(125)
    twin.exitonclick()

main()
