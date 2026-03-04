from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500,height=400)
screen.listen()
colors = ["red","orange","yellow","green","blue","purple"]
# red, orange, yellow, green, blue, purple = Turtle("turtle"), Turtle("turtle"),Turtle("turtle"),Turtle("turtle"),Turtle("turtle"),Turtle("turtle")
# turtles = {"red": red,
#            "orange": orange,
#            "yellow" : yellow,
#            "green" : green,
#            "blue" : blue,
#            "purple": purple
#            }

while True:
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win in the race?\n"
                                                              f"Enter a color from below {colors}\n").lower()
    if user_bet in colors:
        break




turtles = {}
for color in colors:
    turtles[color] = Turtle("turtle")

x_pos = -((screen.window_width()/2) - 20)
y_pos = -(((len(turtles)/2)-0.5) * 50)


for trtl in turtles:
    new_turtle = turtles[trtl]
    new_turtle.color(trtl)
    new_turtle.penup()
    new_turtle.goto(x_pos,y_pos)
    y_pos += 50

turtles[user_bet].pencolor("black")

is_running = True
is_win = False
while is_running:
    for trtl in turtles:
        random_distance = random.randint(0,10)
        turtles[trtl].fd(random_distance)
        if turtles[trtl].xcor() > (screen.window_width()/2):
            is_running = False

    user_turtle_x = turtles[user_bet].xcor()
    if not is_running:
        for trtl in turtles:
            if user_turtle_x < turtles[trtl].xcor():
                print("You Loss")
                is_win = False
                break
            else:
                is_win = True

    if is_win:
        print("You Win")

screen.exitonclick()

