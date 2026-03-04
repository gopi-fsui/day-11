from turtle import Turtle, Screen
# import turtle as t

tam = Turtle()
screen = Screen()
screen.listen()

def forward():
    tam.fd(20)

def backward():
    tam.bk(20)

def counter_clockwise():
    # tam.left(20)
    new_heading = tam.heading() + 20
    tam.setheading(new_heading)

def clockwise():
    # tam.right(20)
    new_heading = tam.heading() - 20
    tam.setheading(new_heading)


screen.onkey(key="Up",fun=forward)
screen.onkey(key="Left", fun=counter_clockwise)
screen.onkey(key="Right", fun=clockwise)
screen.onkey(key="Down",fun=backward)

screen.onkey(key="c",fun=tam.reset)



screen.mainloop()

