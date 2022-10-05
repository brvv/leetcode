class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        newGrid = [[1 for item in range(n)] for _ in range(m)]
        
        for row_i in range(1, len(newGrid)):
            row = newGrid[row_i]
            for col_i in range(1, len(row)):
                newGrid[row_i][col_i] = newGrid[row_i - 1][col_i] + newGrid[row_i][col_i - 1]
        return newGrid[-1][-1]