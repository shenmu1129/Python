import turtle #导入海归模块

turtle.showturtle() #显示箭头
turtle.write("你好Python")
turtle.forward(300) #前进三百个像素
turtle.color("red") #改变画笔的颜色
turtle.left(90) #箭头左转九十度
turtle.forward(200)

turtle.goto(0,0)#箭头去向00点
turtle.penup() #抬起笔，可以不画出来
turtle.goto(0,50)
turtle.pendown()#笔放下
turtle.circle(100) #画一个半径为一百的圆

turtle.done() #程序结束可以一直运行