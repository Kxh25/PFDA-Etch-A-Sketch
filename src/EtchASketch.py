# how do you write code
import pygame
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

    def __innit__(self, pos = (0,0), width = 500, height = 300):
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
    def __innit__(self, text, x_pos, y_pos, enabled):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled
        self.draw()

    def draw(self):
        button_text = pygame.font.Font.render(self.text, True, 'black')
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos),(150, 25))
        pygame.draw.rect(screen, 'gray', button_rect, 0, 5)
        pygame.draw.rect(screen, 'black', button_rect, 2, 5)
        screen.blit(button_text, (self.x_pos, self.y_pos + 3))


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
canvas = Canvas()
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

fps = 60
timer = pygame.time.Clock()

lineDraw = False

running = True
while running:
    screen.fill(background_color)
    timer.tick(fps)
    canvas.pos = 90, 90
    canvas.draw
    drawbutton = DrawButton('Draw', 10, 10, True)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if buttonX <= mouse_x <= buttonX + buttonWidth and \
                buttonY <= mouse_y <= buttonY + buttonHeight:
                    lineDraw = True
                    line_start = (mouse_x, mouse_y)
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                lineDraw = False
        if event.type == pygame.MOUSEMOTION and lineDraw:
            line_end = pygame.mouse.get_pos()
        
    
        
        #canvas
    #canvas.fill(inner_color)
    #pygame.draw.rect(canvas, inner_color, (500, 300, 90, 90))

       #draw Button
    pygame.draw.rect(button, (200,200,200), (buttonX, buttonY, buttonWidth, buttonHeight))
    font = pygame.font.Font(None, 30)
    text = font.render("Draw", True, (0,0,0))
    text_rect = text.get_rect(center= ((buttonX + buttonWidth // 2),
                                             (buttonY + buttonHeight // 2)))
    screen.blit(text, text_rect)
        
        #screen.blit(canvas, (50, 70))
        
    if lineDraw:
        pygame.draw.line(canvas, line_color, line_start, line_end, 2)
        
    pygame.display.flip()

pygame.quit()











#if __name__ == "__main__":
    #main()
