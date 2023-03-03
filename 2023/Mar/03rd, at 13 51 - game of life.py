class Solution:
    def getNeighbours(self, board, target):
        row_start = max(0, target[0] - 1)
        col_start = max(0, target[1] - 1)
        row_end = min(len(board) - 1, target[0] + 1)
        col_end = min(len(board[0]) - 1, target[1] + 1)

        count = 0

        for row_i in range(row_start, row_end + 1):
            for col_i in range(col_start, col_end + 1):
                cell = board[row_i][col_i]

                if cell == 1 and [row_i, col_i] != target:
                    count += 1
        return count


    def gameOfLife(self, board: List[List[int]]) -> None:


        next_board = [[0 for item in row] for row in board]
        
        for row_i in range(len(board)):
            for col_i in range(len(board[row_i])):
                neighbours = self.getNeighbours(board, [row_i, col_i])

                if neighbours < 2:
                    next_board[row_i][col_i] = 0
                elif 2 == neighbours:
                    next_board[row_i][col_i] = board[row_i][col_i]
                elif neighbours > 3:
                    next_board[row_i][col_i] = 0 
                elif neighbours == 3:
                    next_board[row_i][col_i] = 1
                else:
                    print('should not happen????')
        
        for row_i in range(len(board)):
            for col_i in range(len(board[row_i])):
                board[row_i][col_i] = next_board[row_i][col_i] 
        return board

