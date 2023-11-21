import pygame
import math
from pygame.math import Vector2
import Background
screen_width, screen_height = 1920, 1080
running = True
#import the shit
def main():
    global running  # Declare running as a global variable
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('TicTacToe')
    #title
    pygame.display.update()
    #clean screen
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

                # Draw background
        Background.load

        # Update display
        pygame.display.flip()
        #infinte running loop



if __name__ == "__main__":
    main() #run Main sequence