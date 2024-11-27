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
    
    line.shape('turtle')
    line.color('black')

    
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
    global click_count
    click_count += 1
    
    #draw button
    if -250 <= x <= -200 and -170 <= y <= -100:
        print("Draw Button clicked!")
        line.forward(20)
        
    #direction button
    if -150 <= x <= -100 and -170 <= y <= -100:
        print("Direction Button clicked!")
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

    if 250 <= x <= 300 and 60 <= y <= 110:
        print("Color Button Clicked!")
        color_change()

    
def color_change():
    global click_count
    click_count += 1
    if click_count == 0:
        color = 'black'
        line.color = 'black'
        return color
    elif click_count == 1:
        color = 'red'
        line.color = 'red'
        return color
    elif click_count == 2:
        color = 'orange'
        line.color = 'orange'
        return color
    elif click_count == 3:
        color = 'yellow'
        line.color = 'yellow'
        return color
    elif click_count == 4:
        color = 'green'
        line.color = 'green'
        return color
    elif click_count == 5:
        color = 'blue'
        line.color = 'blue'
        return color
    elif click_count == 6:
        color = 'purple'
        line.color = 'purple'
        return color
    elif click_count == 7:
        color = 'pink'
        line.color = 'pink'
        return color
    elif click_count == 8:
        color = 'brown'
        line.color = 'brown'
        return color
    elif click_count > 8:
        click_count = 0
        return color
    



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

    turtle.penup()
    turtle.goto(250, 80)
    turtle.pendown()
    turtle.fillcolor('dark gray')
    turtle.begin_fill()
    for e in range(2):
        turtle.forward(70)
        turtle.right(90)
        turtle.forward(40)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(280, 60)
    turtle.write(color_change(), align = 'center', font=('Arial', 12, 'bold'))

if __name__ == "__main__":
    main()