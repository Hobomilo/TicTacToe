class Trophy:
    def __init__(self, board):
        self.board = board

    def check_win(self):
        # Check rows and columns
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                return self.board[i][0]  # Win in row
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '':
                return self.board[0][i]  # Win in column

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return self.board[0][0]  # Win in diagonal
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return self.board[0][2]  # Win in diagonal

        return None  # No win

    def check_tie(self):
        for row in self.board:
            for cell in row:
                if cell == '':
                    return False  # Game is not a tie

        return True  # Game is a tie
