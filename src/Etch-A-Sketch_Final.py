import turtle
import os
from PIL import Image



line = turtle.Turtle()

color_text = 'black'
size_text = '2'
speed_text = '4'

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
    clear_button()
    save_button()
    line.shape('turtle')
    
    
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.onscreenclick(draw_click)

    turtle.done()



def canvas():
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-300, 200)
    turtle.pendown()
    turtle.fillcolor('white')
    turtle.pensize(4)
    turtle.begin_fill()

    for i in range (2):
        turtle.forward(500)
        turtle.right(90)
        turtle.forward(320)
        turtle.right(90)
    turtle.end_fill()
    turtle.pensize(2)
    turtle.penup()

def draw_click(x, y):
    
    
    #draw button
    if -250 <= x <= -200 and -190 <= y <= -100:
        print("Draw Button clicked!")
        line.forward(30)
        
    #direction button
    elif -150 <= x <= -70 and -190 <= y <= -100:
        print("Direction Button clicked!")
        movement()

    #color button
    elif 250 <= x <= 320 and 60 <= y <= 130:
        print("Color Button Clicked!")
        color_change()
        

    #size button
    elif 250 <= x <= 320 and -50 <= y <= 0:
        print("Size Button clicked!")
        change_size()

    #speed button
    elif 250 <= x <= 320 and -180 <= y <= -150:
        print("Speed Button clicked!")
        speed_change()

    #Clear button
    elif 0 <= x <= 50 and -190 <= y <= -100:
        print("Clear Button clicked!")
        travel_change()

    #save button
    elif 270 <= x <= 320 and 220 <= y <= 250:
        print("Save Button clicked!")
        save()


#changes
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

def travel_change():
   line.clear()
   line.penup()
   line.goto(0,0)
   line.pendown()
  
def save():
    line.hideturtle()
    canvas = turtle.getcanvas()
    canvas.postscript(file="test.eps")

    img = Image.open("test.eps")
    img.save("test.png")
    line.showturtle()
    
    

#buttons
def draw_button():
    
    turtle.penup()
    turtle.goto(-250, -150)
    turtle.pendown()
    turtle.fillcolor('#a9ea04')
    turtle.begin_fill()

    for i in range(2):
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)

    turtle.end_fill()
    turtle.penup()
    turtle.goto(-220, -180) 
    turtle.write("Draw", align='center', font=('Trebuchet MS', 12, 'normal'))

def direction_button():
    turtle.penup()
    turtle.goto(-150, -150)
    turtle.pendown()
    turtle.fillcolor('#ffa804')
    turtle.begin_fill()

    for i in range(2):
        turtle.forward(90)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)

    turtle.end_fill()
    turtle.penup()
    turtle.goto(-110, -180) 
    turtle.write("Direction", align='center', font=('Trebuchet MS', 12, 'normal'))

def color_button():
    turtle.penup()
    turtle.goto(250, 130)
    turtle.pendown()
    turtle.fillcolor('#de22ef')
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

def speed_button():
    turtle.penup()
    turtle.goto(250, -140)
    turtle.pendown()
    turtle.fillcolor('#f3f3f2')
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

def clear_button():
    turtle.penup()
    turtle.goto(0, -150)
    turtle.pendown()
    turtle.fillcolor('#620504')
    turtle.begin_fill()

    for i in range(2):
        turtle.forward(70)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)

    turtle.end_fill()
    turtle.penup()
    turtle.goto(35, -170) 
    turtle.write("Clear", align='center', font=('Verdana', 12, 'bold'))

def save_button():
    turtle.penup()
    turtle.goto(270, 250)
    turtle.pendown()
    turtle.fillcolor('#ff5775')
    turtle.begin_fill()

    for i in range(2):
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(30)
        turtle.right(90)

    turtle.end_fill()
    turtle.penup()
    turtle.goto(290, 220) 
    turtle.write("Save", align='center', font=('Arial', 12, 'bold'))


if __name__ == "__main__":
    main()