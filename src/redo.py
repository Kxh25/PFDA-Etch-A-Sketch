import turtle
import os

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
    turtle.onscreenclick(button_click)

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

def button_click(x, y):
    if -250 <= x <= -100 and -170 <= y <= -100:
        print("Button clicked!")

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


if __name__ == "__main__":
    main()