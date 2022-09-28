class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()
        def dfs(row, col, i):
            if (i >= len(word)):
                return True
            elif (row < 0 or row >= ROWS) or (col < 0 or col >= COLS) or (word[i] != board[row][col]) or ((row,col) in path):
                return False

            path.add((row,col))
            next_letter = dfs(row - 1, col, i + 1) or dfs(row + 1, col, i + 1) or dfs(row, col - 1, i + 1) or dfs(row, col + 1, i + 1)
            path.remove((row,col))
            return next_letter
        
        for row_i, row in enumerate(board):
            for col_i, item in enumerate(row):
                
                if (dfs(row_i, col_i, 0)):
                    return True
        return False
 