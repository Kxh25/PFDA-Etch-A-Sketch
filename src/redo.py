import turtle
import os


line = turtle.Turtle()

click_count = 0
def main():
    """draws a line, and affects the size, color, and speed of lines
     by using different buttons """
    
    turtle.setup(700, 500)
    turtle.title("Etch A Sketch")
    screen = turtle.Screen()
    screen.bgcolor('red')
    turtle.showturtle()
    canvas()
    draw_button()
    direction_button()
    color_button()
    size_button()
    speed_button()
    line.shape('turtle')
    
    

    
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.onscreenclick(draw_click)

    turtle.done()


def canvas():
    turtle.penup()
    turtle.goto(-300, 200)
    turtle.pendown()
    turtle.fillcolor('white')
    turtle.begin_fill()

    for i in range (2):
        turtle.forward(500)
        turtle.right(90)
        turtle.forward(300)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()

def draw_click(x, y):
    
    
    #draw button
    if -250 <= x <= -200 and -170 <= y <= -100:
        print("Draw Button clicked!")
        line.forward(20)
        
    #direction button
    elif -150 <= x <= -100 and -170 <= y <= -100:
        print("Direction Button clicked!")
        movement

    elif 250 <= x <= 300 and 60 <= y <= 110:
        print("Color Button Clicked!")
        color_change

    elif 250 <= x <= 300 and -50 <= y <= 0:
        print("Size Button clicked!")
        change_size

    elif 250 <= x <= 300 and -180 <= y <= -150:
        print("Speed Button clicked!")
        speed_change


def movement():
    global click_count
    click_count += 1
    if click_count == 1:
            line.setheading(0)
    elif click_count == 2:
        line.setheading(90)
    elif click_count == 3:
        line.setheading(180)
    elif click_count == 4:
        line.setheading(270)
    elif click_count > 4:
        click_count = 0

def color_change():
    global click_count
    click_count += 1
    
    color = ['black', 'red', 'orange', 'yellow', 'green', 'blue',
             'purple', 'pink', 'brown']
    #color = [(0,0,0), (255,0,0), (236,98,0), (255,239,0), (0,255,0), (0,0,255),
             #(118,0,255), (254,101,225), (115,57,0)]
    
    
    line.pencolor('black')

    if click_count == 1:
        linecolor = 'red'
        line.pencolor('red')
        return linecolor
    elif click_count == 2:
        linecolor = 'orange'
        line.pencolor('orange')
        return linecolor
    elif click_count == 3:
        linecolor = 'yellow'
        line.pencolor('yellow')
        return linecolor
    elif click_count == 4:
        linecolor = 'green'
        line.pencolor('green')
        return linecolor
    elif click_count == 5:
        linecolor = 'blue'
        line.pencolor('blue')
        return linecolor
    elif click_count == 6:
        linecolor = 'purple'
        line.pencolor('purple')
        return linecolor
    elif click_count == 7:
        linecolor = 'pink'
        line.pencolor('pink')
        return linecolor
    elif click_count == 8:
        linecolor = 'brown'
        line.pencolor('brown')
        return linecolor
    elif click_count > 8:
        click_count = 0
        linecolor = 'black'
        return linecolor
    
def speed_change():
    global click_count
    click_count += 1
    speed = [4, 5, 6, 7, 8]
    line.speed(speed[0])
    
    if click_count == 1:
        line.speed(speed[1])
    elif click_count == 2:
        line.speed(speed[2])
    elif click_count == 3:
        line.speed(speed[3])
    elif click_count == 4:
        line.speed(speed[4])
    elif click_count > 4:
        click_count = 0


def change_size():
    global click_count
    click_count += 1
    up = '2'
    size_point = [1, 2, 3, 4, 5]
    line.pensize(size_point[1])
    if click_count == 1:
        line.pensize(size_point[2])
        up = '3'
        return up
    elif click_count ==2:
        line.pensize(size_point[3])
        up = '4'
        return up
    elif click_count == 3:
        line.pensize(size_point[4])
        up = '5'
        return up
    elif click_count == 4:
        line.pensize(size_point[0])
        up = '1'
        return up
    elif click_count > 4:
        click_count = 0


#buttons
def draw_button():
    turtle.penup()
    turtle.goto(-250, -150)
    turtle.pendown()
    turtle.fillcolor('light gray')
    turtle.begin_fill()

    for i in range(2):
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)

    turtle.end_fill()
    turtle.penup()
    turtle.goto(-230, -170) 
    turtle.write("Draw", align='center', font=('Arial', 12, 'normal'))

def direction_button():
    turtle.penup()
    turtle.goto(-150, -150)
    turtle.pendown()
    turtle.fillcolor('light gray')
    turtle.begin_fill()

    for i in range(2):
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)

    turtle.end_fill()
    turtle.penup()
    turtle.goto(-120, -190) 
    turtle.write("Direction", align='center', font=('Arial', 12, 'normal'))

def color_button():
    turtle.penup()
    turtle.goto(250, 130)
    turtle.pendown()
    turtle.fillcolor('light gray')
    turtle.begin_fill()

    for i in range(2):
        turtle.forward(70)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)

    turtle.end_fill()
    turtle.penup()
    turtle.goto(280, 110) 
    turtle.write("Color", align='center', font=('Arial', 12, 'bold'))

    #box underneath button
    turtle.penup()
    turtle.goto(250, 80)
    turtle.pendown()
    turtle.fillcolor(color_change())
    turtle.begin_fill()
    for e in range(2):
        turtle.forward(70)
        turtle.right(90)
        turtle.forward(30)
        turtle.right(90)
    turtle.end_fill()
    #turtle.penup()
    #turtle.goto(280, 60)
    #turtle.write(color_change(), align = 'center', font=('Arial', 12, 'bold'))

def size_button():
    turtle.penup()
    turtle.goto(250, 0)
    turtle.pendown()
    turtle.fillcolor('light gray')
    turtle.begin_fill()

    for i in range(2):
        turtle.forward(70)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)

    turtle.end_fill()
    turtle.penup()
    turtle.goto(280, -20) 
    turtle.write("Size", align='center', font=('Arial', 12, 'bold'))

    #box underneath button
    turtle.penup()
    turtle.goto(250, -50)
    turtle.pendown()
    turtle.fillcolor('dark gray')
    turtle.begin_fill()
    for e in range(2):
        turtle.forward(70)
        turtle.right(90)
        turtle.forward(30)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(280, -70)
    line.color('white')
    turtle.write(change_size(), align='center', font=('Arial', 12, 'bold'))
    line.color('black')
    line.pencolor('black')

def speed_button():
    turtle.penup()
    turtle.goto(250, -140)
    turtle.pendown()
    turtle.fillcolor('light gray')
    turtle.begin_fill()

    for i in range(2):
        turtle.forward(70)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)

    turtle.end_fill()
    turtle.penup()
    turtle.goto(280, -165) 
    turtle.write("Speed", align='center', font=('Arial', 12, 'bold'))

    #box underneath button
    turtle.penup()
    turtle.goto(250, -190)
    turtle.pendown()
    turtle.fillcolor('dark gray')
    turtle.begin_fill()
    for e in range(2):
        turtle.forward(70)
        turtle.right(90)
        turtle.forward(30)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(280, -200)
    line.color('white')
    turtle.write(speed_change, align='center', font=('Arial', 12, 'bold'))
    line.color('black')
    line.pencolor('black')

if __name__ == "__main__":
    main()