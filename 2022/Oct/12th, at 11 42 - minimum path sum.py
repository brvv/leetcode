class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        newGrid = [[1000 for item in row] for row in grid]
        newGrid[0][0] = grid[0][0]
        
        for row_i, row in enumerate(grid):
            for col_i, item in enumerate(row):
                if row_i == 0 and col_i == 0:
                    continue
                
                left = newGrid[row_i][col_i - 1] if col_i - 1 >= 0 else 1000
                top = newGrid[row_i - 1][col_i] if row_i - 1 >= 0 else 1000
                
                newGrid[row_i][col_i] = grid[row_i][col_i] + min(left, top)
        
        return newGrid[-1][-1]