import turtle 
def Init():
    turtle.penup()
    turtle.pendown()
def end():
    turtle.done()
def Draw_Petals():
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    turtle.right(61)
    turtle.circle(145, 30)
    turtle.left(100)
    turtle.circle(145, 30)
    turtle.right(122)
    turtle.circle(145, 30)
    turtle.left(100)
    turtle.circle(145, 30)
    turtle.right(122)
    turtle.circle(145, 30)
    turtle.left(100)
    turtle.circle(145, 30)
    turtle.right(122)
    turtle.circle(145, 30)
    turtle.left(100)
    turtle.circle(145, 30)
    turtle.right(122)
    turtle.circle(145, 30)
    turtle.left(100)
    turtle.circle(145, 30)
    turtle.right(122)
    turtle.circle(145, 30)
    turtle.left(100)
    turtle.circle(145, 30)
    turtle.right(122)
    turtle.circle(145, 30)
    turtle.left(100)
    turtle.circle(145, 30)
    turtle.right(122)
    turtle.circle(145, 30)
    turtle.left(100)
    turtle.circle(145, 30)
    turtle.right(122)
    turtle.circle(145, 30)
    turtle.left(100)
    turtle.circle(145, 30)
    turtle.end_fill()
def Draw_Blossom():
    turtle.right(60)
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.circle(100, 370)
    turtle.end_fill()
def Draw_Rod():
    turtle.right(82)
    turtle.fd(250)
    turtle.right(180)
    turtle.fd(80)
def Draw_Leaves():
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.right(120)
    turtle.circle(200, 50)
    turtle.left(130)
    turtle.circle(200, 50)
    turtle.right(110)
    turtle.fd(50)
    turtle.left(60)
    turtle.circle(200, 50)
    turtle.right(130)
    turtle.circle(200, 50)
    turtle.end_fill()
if __name__ == '__main__':
    Init()
    Draw_Petals()
    Draw_Blossom()
    Draw_Rod()
    Draw_Leaves()
