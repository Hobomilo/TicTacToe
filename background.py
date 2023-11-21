import os
import pygame

class Background:
    def __init__(self):
        # Get the path of the current script
        script_path = os.path.dirname(os.path.abspath(__file__))

        # Load background image
        image_path = os.path.join(script_path, 'ackground.png')
        self.sprite = pygame.image.load(image_path)
        self.position = 0

    def draw(self, surface):
        surface.blit(self.sprite, (self.position, 0))
