# how do you write code
import pygame
import os




def main():

    """
    The main function of the script.

    Creates a screen with the design qualities of a digital 
    Etch-A-Sketch.
    
    This function ties all the class functions together to create the screen. The screen
    should include a canvas, a drawing cursor that can only move within
    the canvas bounds, a directional knob/button, a size button, a color button,
    a speed modifier, a save button, and an ESC button.
    
     """
    
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
    
    #border
    border = 10
    
    #canvas dimensions
    canvasWidth = 300
    canvasHeight = 200
    canvas = pygame.Surface((canvasWidth, canvasHeight))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(background_color)
        
        #canvas
        canvas.fill(inner_color)
        pygame.draw.rect(canvas, inner_color, (300, 0, 90, 90))

        screen.blit(canvas, (100, 100))
        
        
        pygame.display.flip()

    pygame.quit()






if __name__ == "__main__":
    main()
