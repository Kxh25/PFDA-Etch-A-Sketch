import turtle

#following a turtle etchasketch tutorial to apply to mine,
#with alterations of course!
line = turtle.Turtle()
line.shape('turtle')
line.color('black')

def move_right():
    line.setheading(0)
    line.forward(20)

def move_left():
    line.setheading(180)
    line.forward(20)

def move_up():
    line.setheading(90)
    line.forward(20)
    
def move_down():
    line.setheading(270)
    line.forward(20)
    
while True:
    direction = input("left/right/up/down")
    if (direction == "right"):
        move_right()
    elif(direction == "left"):
        move_left()
    elif(direction == "up"):
        move_up()
    elif(direction == "down"):
        move_down()
    else:
        print("Please enter a direction")

    turtle.done()