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

class TicTacToe:
    def __init__(self):
        self.board = [['', '', ''],
                      ['', '', ''],
                      ['', '', '']]
        self.current_player = 'X'

    def switch_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def handle_click(self, row, col):
        if self.board[row][col] == '':
            self.board[row][col] = self.current_player
            self.switch_player()

    def draw(self, screen):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == 'X':
                    draw_x(screen, row, col)
                elif self.board[row][col] == 'O':
                    draw_o(screen, row, col)

def draw_x(screen, row, col):
    # Implement your code to draw X at the specified row and col
    pass

def draw_o(screen, row, col):
    # Implement your code to draw O at the specified row and col
    pass

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
