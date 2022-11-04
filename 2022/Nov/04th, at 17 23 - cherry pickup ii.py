class Solution:
    
    def getPossibleCoordinates(self, current_i, grid):
        coords = [current_i]
        if current_i - 1 >= 0:
            coords.append(current_i - 1)
        if current_i + 1 < len(grid[0]):
            coords.append(current_i + 1)
        return coords
    
    def getMaxValForCell(self, table, grid, level, cell_r1, cell_r2):
        prev_r1s = self.getPossibleCoordinates(cell_r1, grid) 
        prev_r2s = self.getPossibleCoordinates(cell_r2, grid) 
        
        max_prev_val = -1
        
        for prev_r1 in prev_r1s:
            for prev_r2 in prev_r2s:
                val = table[level - 1][prev_r1][prev_r2]
                if val >= max_prev_val:
                    max_prev_val = val
        return max_prev_val
    
    def get2DMax(self, table, level):
        max_v = -1
        
        for row in table[level]:
            for val in row:
                max_v = max(max_v, val)
        return max_v
        
        
    def cherryPickup(self, grid: List[List[int]]) -> int:
        #table[row][r1][r2]
        table = [[[-1 for _ in row] for _ in row] for row in grid]
        
        table[0][0][len(grid[0])-1] = grid[0][0] + grid[0][-1]
        
        for row_i in range(1, len(grid)):
            for r1_i in range(len(table[row_i])):
                for r2_i in range(len(table[row_i][r1_i])):
                    max_prev_val = self.getMaxValForCell(table, grid, row_i, r1_i, r2_i)
                    
                    if max_prev_val == -1:
                        continue
                    
                    curr_r1 = grid[row_i][r1_i]
                    curr_r2 = grid[row_i][r2_i]
                    
                    new_cell_val = max_prev_val + curr_r1 + curr_r2 if r1_i != r2_i else max_prev_val + curr_r1
                    
                    table[row_i][r1_i][r2_i] = new_cell_val
        print(table)
        return self.get2DMax(table, len(table) - 1)