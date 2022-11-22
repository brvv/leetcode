class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        vertical_skyline = [max(row) for row in grid]
        horizontal_skyline = [max([grid[row_i][col_i] for row_i in range(len(grid))]) for col_i in range(len(grid[0]))]
        
        res = 0
        
        for row_i in range(len(grid)):
            for col_i in range(len(grid[row_i])):
                max_increase = 0
                curr_val = grid[row_i][col_i]
                skyline = min(vertical_skyline[row_i], horizontal_skyline[col_i])
                
                if curr_val <= skyline:
                    max_increase = skyline - curr_val
                
                
                res += max_increase
        return res