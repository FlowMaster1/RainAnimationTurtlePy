import turtle
import random

wn = turtle.Screen()

wn.title("Rain")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)

speed = 0

prototype = turtle.Turtle()
prototype.hideturtle()
prototype.speed(6)
prototype.shape("square")
prototype.penup()

moon = turtle.Turtle()
moon.shape("circle")
moon.penup()
moon.color("white")
moon.shapesize(stretch_wid = 6, stretch_len = 6)
moon.goto(200,200)


rain = []

for i in range(150):
    drop = prototype.clone()
    drop.color("blue")
    drop.goto(random.randrange(-400,400),random.randrange(400,1000))
    drop.shapesize(stretch_wid = random.randrange(1,5), stretch_len = random.randrange(1,10)/100)
    drop.showturtle()
    rain.append(drop)

stars = []
for i in range(120):
    star = prototype.clone()
    star.color("white")
    star.goto(random.randrange(-400,400),random.randrange(-400,400))
    star.shapesize(stretch_wid = random.randrange(1,10)/100, stretch_len = random.randrange(1,10)/100)
    star.showturtle()
    stars.append(star)



while(True):
    wn.update()

    for i in rain:
        i.resizemode("user")
        wid = i.shapesize()[1]
        hei = i.shapesize()[0]
        if wid <= 0.01 and hei < 2:
            i.sety(i.ycor() - 7 - speed)
        elif wid > 0.05 and hei < 3:
            i.sety(i.ycor() - 13 - speed)
        else:
            i.sety(i.ycor() - 15 - speed)
        if i.ycor() < 100:
            speed += 0.01
        if i.ycor() < -410:
            i.sety(410)
            speed = 0

  
    

