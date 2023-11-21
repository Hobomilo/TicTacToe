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
