class Solution(object):
    def returnSolutions(self, row, cols, positive_diagonal, negative_diagonal, board, solutions):
        n = len(cols)

        if row == n:
            copyBoard = list(board)
            solutions.append(copyBoard)
            return 
        
        for col in range(n):
            if cols[col] or positive_diagonal[row + col] or negative_diagonal[row - col + n - 1]:
                continue

            board[row] = board[row][:col] + "Q" + board[row][col + 1:]
            cols[col] = 1
            positive_diagonal[row + col] = 1
            negative_diagonal[row - col + n - 1] = 1

            self.returnSolutions(row + 1, cols, positive_diagonal, negative_diagonal, board, solutions)

            board[row] = board[row][:col] + "." + board[row][col + 1:]
            cols[col] = 0
            positive_diagonal[row + col] = 0
            negative_diagonal[row - col + n - 1] = 0

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        cols = [0 for i in range(n)]
        positive_diagonal, negative_diagonal = [0 for i in range(2 * n - 1)], [0 for i in range(2 * n - 1)]
        board = ["." * n for _ in range(n)]
        solutions = []
        
        self.returnSolutions(0, cols, positive_diagonal, negative_diagonal, board, solutions)
        return solutions