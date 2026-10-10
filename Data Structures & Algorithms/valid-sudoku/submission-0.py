class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_box(row, col):
            seen = set()
            for r in range(row, row + 3):
                for c in range(col, col + 3):
                    if board[r][c] in seen:
                        return False
                    if board[r][c] != ".":
                        seen.add(board[r][c])
            return True
        
        def check_row(row):
            seen = set()
            for c in range(len(board[row])):
                if board[row][c] in seen:
                        return False
                if board[row][c] != ".":
                    seen.add(board[row][c])
            return True

        def check_col(col):
            seen = set()
            for r in range(len(board[col])):
                if board[r][col] in seen:
                        return False
                if board[r][col] != ".":
                    seen.add(board[r][col])
            return True
        
        for i in range(9):
            if check_col(i) == False or check_row(i) == False:
                return False
        corner = [(0, 0), (3,3), (6, 6), (3, 0), (6, 0), (0, 3), (0, 6), (6, 0), (6, 3)]

        for i, j in corner:
            if check_box(i, j) == False:
                return False
        return True

        
        