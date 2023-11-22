import os
import pygame
from background import Background
from Tictactoe import TicTacToe
from trophy import Trophy

screen_width, screen_height = 820, 613
running = True

def display_result(screen, result):
    font = pygame.font.Font(None, 74)  # Use the default system font
    text = font.render(result, True, (0, 0, 0))  # Render text in black
    screen.blit(text, (screen_width // 4, screen_height // 2))
    
def main():
    global running
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('TicTacToe')

    background = Background()
    tic_tac_toe = TicTacToe()
    trophy = Trophy(tic_tac_toe.board)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                row = y // (screen_height // 3)
                col = x // (screen_width // 3)
                tic_tac_toe.handle_click(row, col)

        background.draw(screen)
        tic_tac_toe.draw(screen)

        result = trophy.check_win()
        if result is None:
            if trophy.check_tie():
                display_result(screen, "Tie!")
                pygame.display.flip()
                pygame.time.wait(2000)
                running = False
        else:
            display_result(screen, f"{result} wins!")
            pygame.display.flip()
            pygame.time.wait(2000)
            running = False

        pygame.display.flip()

if __name__ == "__main__":
    main()
