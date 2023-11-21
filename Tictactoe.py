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
    x = col * cell_width
    y = row * cell_height
    pygame.draw.line(screen, (255, 255, 255), (x, y), (x + cell_width, y + cell_height), 5)
    pygame.draw.line(screen, (255, 255, 255), (x, y + cell_height), (x + cell_width, y), 5)

def draw_o(screen, row, col, cell_width, cell_height):
    x = col * cell_width + cell_width // 2
    y = row * cell_height + cell_height // 2
    radius = min(cell_width, cell_height) // 2 - 5
    pygame.draw.circle(screen, (255, 255, 255), (x, y), radius, 5)
