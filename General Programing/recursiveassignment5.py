import turtle
def drawBranc(t, n, a, length):
    if n == 0:
       return #leaves()
    t.left(90)
    t.forward(length)
    t.left(a)
    t.forward(length/2)
    t.left(a)
    t.forward(length/2)
    t.penup()
    t.goto(0,0)
    t.pendown()
    drawBranc(t, n-1, a-1, length)

def main():
    t = turtle.Turtle()
    screen = t.getscreen()
    t.speed(100)
    t.penup()
    t.goto(0,0)
    t.pendown()
    drawBranc(t, 30, 30, 100)
    screen.exitonclick()
if __name__ =="__main__":
    main()
    
