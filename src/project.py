import turtle
#turtle.hideturtle()
t= turtle

def main():
    screen = turtle.Screen()
    screen.setup(width=1200, height=800)
    screen.bgcolor ("pink")
    screen.title("City") 
    drawing()
   
def drawing(): 
    def marking_vanishing():
        turtle.speed(0)
        t.colormode(255)
        turtle.width(4)
        t.penup()
        t.setpos (0,100)
        t.pendown()
        t.forward (1)
        turtle.width(1)
        t.penup()
    def car_drawing():
        t.penup()
        t.setpos (400,-400)
        t.pendown()
        t.setheading(129)
        t.forward (636)
        t.penup()
        t.setpos (-400,-400)
        t.pendown()
        t.setheading(51)
        t.forward (636)
        t.penup()

    
    def building_one_left():
        t.penup()    
        t.setpos (-600,200)
        t.pendown()
        t.setheading(-9)
        t.forward (200)

    def building_two_left():
        t.penup()
        t.setpos(-400,-400)
        t.pendown()
        t.setheading(90)
        t.forward (900)
        t.setheading(-45)  
        t.forward (320)
        t.setheading(-90)
        t.forward (400)
        t.penup()
        t.setpos(-360,-350)
        t.pendown()
        t.setheading(90)
        t.forward (100)
        t.setheading(42)
        t.forward (240)
        t.setheading(-90)
        t.forward (50)



    def building_three_left():
        t.penup()
        t.setpos (-175,100)
        t.pendown()
        t.setheading(2)
        t.forward (100)
    
        
        
    marking_vanishing()
    car_drawing()
    building_one_left()
    building_two_left() 
    building_three_left()
    t.exitonclick()

if __name__=="__main__":
    main()