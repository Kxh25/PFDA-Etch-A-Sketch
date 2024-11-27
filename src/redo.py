import turtle
import os


line = turtle.Turtle()
line.shape('turtle')
line.color('black')

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


if __name__ == "__main__":
    main()