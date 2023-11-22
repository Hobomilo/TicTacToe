screen_width, screen_height = 820, 613
screen = screen_width, screen_height
import pygame
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
        cell_width = screen_width // 3
        cell_height = screen_height // 3

        for row in range(3):
            for col in range(3):
                if self.board[row][col] == 'X':
                    draw_x(screen, row, col, cell_width, cell_height)
                elif self.board[row][col] == 'O':
                    draw_o(screen, row, col, cell_width, cell_height)

def draw_x(screen, row, col, cell_width, cell_height):
    x = col * cell_width + cell_width // 2
    y = row * cell_height + cell_height // 2
    line_length = int(min(cell_width, cell_height) * 0.6)  # Downsize by 40%

    if col == 0:  # Adjust for the left column
        x += int(cell_width * 0.4)  # Increase the adjustment more to the right
    elif col == 2:  # Adjust for the right column
        x -= int(cell_width * 0.2)  # Adjusted less to make it more to the left

    x_start = x - line_length // 2
    y_start = y - line_length // 2
    pygame.draw.line(screen, (0, 0, 0), (x_start, y_start), (x_start + line_length, y_start + line_length), 3)
    pygame.draw.line(screen, (0, 0, 0), (x_start, y_start + line_length), (x_start + line_length, y_start), 3)

def draw_o(screen, row, col, cell_width, cell_height):
    x = col * cell_width + cell_width // 2
    y = row * cell_height + cell_height // 2
    radius = int(min(cell_width, cell_height) // 2 * 0.6)  # Downsize by 40%

    if col == 0:  # Adjust for the left column
        x += int(cell_width * 0.4)  # Increase the adjustment more to the right
    elif col == 2:  # Adjust for the right column
        x -= int(cell_width * 0.2)  # Adjusted less to make it more to the left

    pygame.draw.circle(screen, (0, 0, 0), (x, y), radius, 3)
