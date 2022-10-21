class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # recursive with memoization:
        cache = {}
        def minPathSumRecursive(row_i=0, col_i=0):
            current_cost = grid[row_i][col_i]
            
            if row_i == len(grid) - 1 and col_i == len(grid[0]) - 1:
                return current_cost
            
            if (tuple([row_i, col_i]) in cache):
                return cache[tuple([row_i, col_i])]

            bottom = 10000000
            right = 10000000

            if row_i + 1 < len(grid):
                bottom = current_cost + minPathSumRecursive(row_i + 1, col_i)

            if col_i + 1 < len(grid[0]):
                right = current_cost + minPathSumRecursive(row_i, col_i + 1)

            cache[tuple([row_i, col_i])] = min(bottom, right)
            return cache[tuple([row_i, col_i])]
        
        # 2d table dp
        def minPathSum2DTable():
            table = [[0 for item in row] for row in grid]
            
            for row_i, row in enumerate(table):
                for col_i, item in enumerate(row):
                    cost = grid[row_i][col_i]
                    
                    if row_i == 0 and col_i == 0:
                        table[row_i][col_i] = cost
                    else:
                        top = table[row_i-1][col_i] if row_i - 1 >= 0 else 10000000000000
                        left = table[row_i][col_i - 1] if col_i - 1 >= 0 else 10000000000000
                        
                        table[row_i][col_i] = cost + min(top, left)
                        
                        
            return table[-1][-1]
                    
                    
        
        return minPathSum2DTable()