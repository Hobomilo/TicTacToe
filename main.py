import os
import pygame
from background import Background
from TicTacToe import TicTacToe



screen_width, screen_height = 820, 613
running = True

def main():
    global running
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('TicTacToe')

    background = Background()
    tic_tac_toe = TicTacToe()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
                x, y = event.pos
                row = y // (screen_height // 3)
                col = x // (screen_width // 3)
                tic_tac_toe.handle_click(row, col)

        # Draw background
        background.draw(screen)

        # Draw Tic Tac Toe board
        tic_tac_toe.draw(screen)

        # Update display
        pygame.display.flip()

if __name__ == "__main__":
    main()
