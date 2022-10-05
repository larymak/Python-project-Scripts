import turtle as t
'''Author: Rajarshi Banerjee | GSAUC3'''
class logo:

    def __init__(i,t) -> None:
        i.t=t

    def blue_part(i):
        i.t.penup()
       
       # d = 200
       # x = 10
        i.t.pencolor('blue')
        i.t.color('blue')
        i.t.goto(-110,-100)
        i.t.pendown()
        i.t.begin_fill()
        i.t.right(180)
        i.t.forward(100/3)

        for _ in range(5):
            i.t.right(15)
            i.t.forward(15)
        i.t.forward(15)
        i.t.right(5)
        for _ in range(5):
            i.t.forward(15)
            i.t.right(5)
        i.t.forward(27.58789)
        for _ in range(5):
            i.t.right(15)
            i.t.forward(15)
       
        
 
        i.t.goto(0,100)
        i.t.goto(0,110)
        i.t.goto(-100,110)
        i.t.goto(-100,110+100/3)
        i.t.left(90)
      
        for _ in range(5):
            i.t.right(15)
            i.t.forward(15)
        i.t.forward(15)
        i.t.right(5)
        for _ in range(5):
            i.t.forward(15)
            i.t.right(5)
        i.t.forward(27.58789)
        for _ in range(5):
            i.t.right(15)
            i.t.forward(15)

        i.t.forward(60+10)


        for _ in range(5):
            i.t.right(15)
            i.t.forward(15)

        i.t.right(5)
        i.t.goto(-100+30,10)

        
        for _ in range(5):
            i.t.left(15)
            i.t.forward(15)
        i.t.left(5)

        i.t.goto(-110,-100)
        i.t.end_fill()

    def yellow_part(i):
        i.t.penup()
        i.t.pencolor('yellow')
        i.t.color('yellow')
        i.t.goto(110,100)
        i.t.right(90)
        i.t.pendown()
        i.t.begin_fill()
        i.t.right(180)
        i.t.forward(100/3)

        for _ in range(5):
            i.t.right(15)
            i.t.forward(15)
        i.t.forward(15)
        i.t.right(5)
        for _ in range(5):
            i.t.forward(15)
            i.t.right(5)
        i.t.forward(27.58789)
        for _ in range(5):
            i.t.right(15)
            i.t.forward(15)
       
        
 
        i.t.goto(0,-100)
        i.t.goto(0,-110)
        i.t.goto(100,-110)
        i.t.goto(100,-110-100/3)
        i.t.left(90)
      
        for _ in range(5):
            i.t.right(15)
            i.t.forward(15)
        i.t.forward(15)
        i.t.right(5)
        for _ in range(5):
            i.t.forward(15)
            i.t.right(5)
        i.t.forward(27.58789)
        for _ in range(5):
            i.t.right(15)
            i.t.forward(15)

        i.t.forward(60+10)


        for _ in range(5):
            i.t.right(15)
            i.t.forward(15)

        i.t.right(5)
        i.t.goto(70,-10)

        
        for _ in range(5):
            i.t.left(15)
            i.t.forward(15)
        i.t.left(5)

        i.t.goto(110,100)
        i.t.end_fill()
        
        
    def eyes(i):
        i.t.penup()
        i.t.color('white')
        i.t.goto(-70,130)
        i.t.pendown()
        i.t.begin_fill()
        i.t.circle(10)
        i.t.end_fill()

        i.t.penup()
        i.t.color('white')
        i.t.goto(70+20,-130)
        i.t.pendown()
        i.t.begin_fill()
        i.t.circle(10)
        i.t.end_fill()

        i.t.hideturtle()
        


if __name__ =="__main__":
    t.Turtle()
    obj=logo(t)
    obj.blue_part()
    obj.yellow_part()
    obj.eyes()
    t.done()

