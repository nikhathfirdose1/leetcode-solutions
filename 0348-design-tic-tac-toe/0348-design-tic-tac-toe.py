class TicTacToe:

    def __init__(self, n: int):

        self.n = n
        self.rows = [0] * self.n
        self.cols = [0] * self.n
        self.diag = 0
        self.anti = 0
        

    def move(self, row: int, col: int, player: int) -> int:

        add = 1 if player == 1 else - 1


        self.rows[row] += add
        self.cols[col] += add

        if row == col:
            self.diag += add
        if row + col == self.n - 1:
            self.anti += add


        if abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or abs(self.diag) == self.n or abs(self.anti) == self.n:
            return player

        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)