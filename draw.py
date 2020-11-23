import turtle
from random import randint

def drawCellTowers():
     myPen = turtle.Turtle()
     myPen.hideturtle()
     turtle.tracer(0)
     myPen.speed(0)
     
     window = turtle.Screen()
     window.bgcolor("#F0F0F0")
     
     x1 = randint(-150,-80)
     y1 = randint(-150,150)
     x2 = randint(80,150)
     y2 = randint(20,150)
     x3 = randint(80,150)
     y3 = randint(-150,-20)
     x = randint(-60,60)
     y = randint(-60,60)
     r1 = ((x-x1)**2 + (y-y1)**2)**0.5
     r2 = ((x-x2)**2 + (y-y2)**2)**0.5
     r3 = ((x-x3)**2 + (y-y3)**2)**0.5

     myPen.color("#ff5744")
     myPen.penup()
     myPen.goto(x1-5,y1)
     myPen.pendown()
     myPen.goto(x1+5,y1)
     myPen.penup()
     myPen.goto(x1,y1-5)
     myPen.pendown()
     myPen.goto(x1,y1+5)
     myPen.penup()
     
     myPen.goto(x1,y1-r1)
     myPen.pendown()
     myPen.circle(r1)
     
     myPen.color("#41befc")
     myPen.penup()
     myPen.goto(x2-5,y2)
     myPen.pendown()
     myPen.goto(x2+5,y2)
     myPen.penup()
     myPen.goto(x2,y2-5)
     myPen.pendown()
     myPen.goto(x2,y2+5)
     myPen.penup()
     
     myPen.goto(x2,y2-r2)
     myPen.pendown()
     myPen.circle(r2)
     myPen.penup()
     
     myPen.color("#52bf54")
     myPen.goto(x3-5,y3)
     myPen.pendown()
     myPen.goto(x3+5,y3)
     myPen.penup()
     myPen.goto(x3,y3-5)
     myPen.pendown()
     myPen.goto(x3,y3+5)
     
     myPen.penup()
     myPen.goto(x3,y3-r3)
     myPen.pendown()
     myPen.circle(r3)
     
     myPen.getscreen().update()
     return x1,y1,r1,x2,y2,r2,x3,y3,r3