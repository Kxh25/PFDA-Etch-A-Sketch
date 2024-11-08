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
    border = 50
    
    #canvas dimensions
    canvasWidth = screenWidth - 2 * border
    canvasHeight = screenHeight - 2 * border

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running == False
        
        screen.fill(background_color)
        
        #border draw
        pygame.draw.rect(screen, border_color, (0, 0, screenWidth, border)) #Top
        pygame.draw.rect(screen, border_color, (0, screenHeight - border,
                                                screenWidth, border)) #Bottom
        pygame.draw.rect(screen, border_color, (0, 0, border, screenHeight)) #Left
        pygame.draw.rect(screen, border_color, (screenWidth - border, 0, 
                                                border, screenHeight)) #Right
        #I had to search this up beause I couldn't figure it out

        pygame.draw.rect(screen, inner_color, (border, border,
                                               canvasWidth, canvasHeight))
        
        pygame.display.flip()

    pygame.quit()






if __name__ == "__main__":
    main()
