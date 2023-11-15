import pygame
import math
from pygame.math import Vector2
from background import Background
screen_width, screen_height = 1920, 1080
running = True
#import the shit
def main():
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
        #infinte running loop



if __name__ == "__main__":
    main() #run Main sequence