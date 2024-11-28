# how do you write code
import pygame
import time
import os
import turtle
import tkinter as tk


"""
The main function of the script.

Creates a screen with the design qualities of a digital 
Etch-A-Sketch.
    
This function ties all the class functions together to create the screen. The screen
should include a canvas, a drawing cursor that can only move within
the canvas bounds, a directional knob/button, a size button, a color button,
a speed modifier, a save button, and an ESC button.
    
"""
class Canvas:

    def __init__(self, pos = (0,0), width = 500, height = 300):
        self.pos = pos
        self.width = width
        self.height = height
        self.color = pygame.Color(255, 255, 255)
        self.surface = self.update_surface()

    def update_surface(self):
        surf = pygame.Surface((self.width, self.height))
        surf.fill(self.color)
        return surf
    
    def draw(self):
        screen.blit(self.surface, self.pos)


   
class DrawButton:
    def __init__(self, text, x_pos, y_pos, enabled):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled
        self.draw()

    def draw(self):
        font = pygame.font.Font(None, 30)
        button_text = font.render(self.text, True, 'black')
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos),(70, 25))
        if self.check_click():
             pygame.draw.rect(screen, 'dark gray', button_rect, 0, 5)
             turtle.listen()
        else:
             pygame.draw.rect(screen, 'light gray', button_rect, 0, 5)

        pygame.draw.rect(screen, 'black', button_rect, 2, 5)
        screen.blit(button_text, (self.x_pos, self.y_pos + 3))

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        leftClick = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos),(150, 25))
        if leftClick and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False
    
    def line_draw(self, s, e, p):
        line = turtle.Turtle()
        line.speed(0)
        line.forward(100)

        

        
        
    
      
    #def line_print(self):
    #    line_start = (100,100)
    #    line_end = (500, 300)
    #    line_printed = False
    #    if self.check_click:
    #        line_printed = True
            
    #        if line_printed:
    #            line = pygame.draw.line(screen, 'black', line_start, line_end, 2)
    #            screen.blit(line)
    #    else:
    #        line_printed = False
            


class DirectionButton:
    def __init__(self, text, x_pos, y_pos, enabled):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled
        self.draw()

    def draw(self):
        font = pygame.font.Font('freesansbold.ttf', 2)
        button_text = font.render(self.text, True, 'black')
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos),(70, 25))
        if self.check_click():
             pygame.draw.rect(screen, 'dark gray', button_rect, 0, 5)
        else:
             pygame.draw.rect(screen, 'light gray', button_rect, 0, 5)

        pygame.draw.rect(screen, 'black', button_rect, 2, 5)
        screen.blit(button_text, (self.x_pos, self.y_pos + 3))

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        leftClick = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos),(150, 25))
        if leftClick and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False

class SizeButton:
    def __init__(self, text, x_pos, y_pos, enabled):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled
        self.draw()

    def draw(self):
        font = pygame.font.Font('freesansbold.ttf', 2)
        button_text = font.render(self.text, True, 'black')
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos),(150, 25))
        if self.check_click():
             pygame.draw.rect(screen, 'dark gray', button_rect, 0, 5)
        else:
             pygame.draw.rect(screen, 'light gray', button_rect, 0, 5)

        pygame.draw.rect(screen, 'black', button_rect, 2, 5)
        screen.blit(button_text, (self.x_pos, self.y_pos + 3))

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        leftClick = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos),(150, 25))
        if leftClick and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False

class ColorButton:
    def __init__(self, text, x_pos, y_pos, enabled):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled
        self.draw()

    def draw(self):
        font = pygame.font.Font('freesansbold.ttf', 2)
        button_text = font.render(self.text, True, 'black')
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos),(150, 25))
        if self.check_click():
             pygame.draw.rect(screen, 'dark gray', button_rect, 0, 5)
        else:
             pygame.draw.rect(screen, 'light gray', button_rect, 0, 5)

        pygame.draw.rect(screen, 'black', button_rect, 2, 5)
        screen.blit(button_text, (self.x_pos, self.y_pos + 3))

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        leftClick = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos),(150, 25))
        if leftClick and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False

class SpeedButton:
    def __init__(self, text, x_pos, y_pos, enabled):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled
        self.draw()

    def draw(self):
        font = pygame.font.Font('freesansbold.ttf', 2)
        button_text = font.render(self.text, True, 'black')
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos),(150, 25))
        if self.check_click():
             pygame.draw.rect(screen, 'dark gray', button_rect, 0, 5)
        else:
             pygame.draw.rect(screen, 'light gray', button_rect, 0, 5)

        pygame.draw.rect(screen, 'black', button_rect, 2, 5)
        screen.blit(button_text, (self.x_pos, self.y_pos + 3))

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        leftClick = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos),(150, 25))
        if leftClick and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False

class SaveButton:
    def __init__(self, text, x_pos, y_pos, enabled):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled
        self.draw()

    def draw(self):
        font = pygame.font.Font('freesansbold.ttf', 2)
        button_text = font.render(self.text, True, 'black')
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos),(150, 25))
        if self.check_click():
             pygame.draw.rect(screen, 'dark gray', button_rect, 0, 5)
        else:
             pygame.draw.rect(screen, 'light gray', button_rect, 0, 5)

        pygame.draw.rect(screen, 'black', button_rect, 2, 5)
        screen.blit(button_text, (self.x_pos, self.y_pos + 3))

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        leftClick = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos),(150, 25))
        if leftClick and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False
pygame.init()
pygame.display.set_caption("Digital Etch-A-Sketch")


    #screen Dimensions
screenWidth = 800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
    
    #screen Colors
background_color = (255, 0, 0)
border_color = (0, 0, 0)
inner_color = (255, 255, 255)
button_color = (200, 200, 200)
    
    #border
border = 10
    
    #canvas dimensions
#canvasWidth = 700
#canvasHeight = 300
#canvas = pygame.Surface((canvasWidth, canvasHeight))

    #buttons
buttonWidth = 70
buttonHeight = 40
buttonX = 0
buttonY = 0
button = pygame.Surface((buttonWidth, buttonHeight))

    #line
line_color = (0,0,0)
line_start = (0,0)
line_end = (0,0)

    #clock
fps = 60
timer = pygame.time.Clock()

lineDraw = False

running = True
while running:
    screen.fill(background_color)
    timer.tick(fps)
    canvas = Canvas()
    canvas.draw
    canvas.pos = 90, 90
    
    drawbutton = DrawButton('Draw', 10, 500, True)
    directionButton = DirectionButton('Change', 100, 500, True)
    sizeButton = SizeButton('Size', 600, 150, True)
    colorButton = ColorButton('Color', 600, 230, True)
    speedButton = SpeedButton('speed', 600, 300, True)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
       
    
        
        #canvas
    #canvas.fill(inner_color)
    #pygame.draw.rect(canvas, inner_color, (500, 300, 90, 90))

       #draw Button
    #pygame.draw.rect(button, (200,200,200), (buttonX, buttonY, buttonWidth, buttonHeight))
    #font = pygame.font.Font(None, 30)
    #text = font.render("Draw", True, (0,0,0))
    #text_rect = text.get_rect(center= ((buttonX + buttonWidth // 2),
                                            # (buttonY + buttonHeight // 2)))
    #screen.blit(text, text_rect)
        
        #screen.blit(canvas, (50, 70))
        
    if lineDraw:
        pygame.draw.line(pygame.surface.Surface(canvas), line_color, line_start, line_end, 2)
        
    pygame.display.flip()

pygame.quit()
turtle.done()






def draw_button():
    




#if __name__ == "__main__":
    #main()
