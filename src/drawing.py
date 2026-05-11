import turtle
#turtle.hideturtle()
t= turtle

def main():
    screen = turtle.Screen()
    screen.setup(width=1200, height=800)
    screen.bgcolor ("pink")
    screen.title("City") 
    building_sketch()
   
def building_sketch(): 
    def marking_vanishing():
        t.colormode(255)
        turtle.width(4)
        t.penup()
        t.setpos (0,100)
        t.pendown()
        t.forward (1)
        t.penup()

    marking_vanishing()
    t.setpos (-600,200)
    t.pendown()
    t.right (10)
    t.forward (200)
    t.setheading(90)
    t.forward (250)
    t.setheading(-38)  
    t.forward (300)
    t.setheading (-90)
    t.forward (200)
    t.exitonclick()

if __name__=="__main__":
    main()