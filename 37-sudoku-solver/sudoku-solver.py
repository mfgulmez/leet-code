class Solution(object):
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    boxes[(i//3)*3 + j//3].add(board[i][j])

        def backtrack():
            min_candidates = 10
            target = None

            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        box = (i//3)*3 + j//3
                        candidates = set("123456789") - rows[i] - cols[j] - boxes[box]
                        if len(candidates) < min_candidates:
                            min_candidates = len(candidates)
                            target = (i, j, candidates)
                        if min_candidates == 1:
                            break

            if not target:
                return True  

            i, j, candidates = target
            box = (i//3)*3 + j//3

            for c in candidates:
                board[i][j] = c
                rows[i].add(c)
                cols[j].add(c)
                boxes[box].add(c)

                if backtrack():
                    return True

                board[i][j] = "."
                rows[i].remove(c)
                cols[j].remove(c)
                boxes[box].remove(c)

            return False

        backtrack()
