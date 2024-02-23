import turtle

#第一个
turtle.width(10)
turtle.color("blue")
turtle.circle(50)
turtle.penup()

#第二个圆
turtle.goto(70,0)
turtle.pendown()
turtle.color("red")
turtle.circle(50)
turtle.penup()
#第三个
turtle.goto(140,0)
turtle.pendown()
turtle.color("black")
turtle.circle(50)
turtle.penup()
#第四个
turtle.goto(30,-60)
turtle.pendown()
turtle.color("green")
turtle.circle(50)
turtle.penup()

#第五个圆
turtle.goto(100,-60)
turtle.pendown()
turtle.color("yellow")
turtle.circle(50)
turtle.penup()

turtle.done()