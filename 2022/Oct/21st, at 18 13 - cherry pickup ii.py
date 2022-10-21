class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        coordinates = []
        cache = {}
        
        def cherryPickupRec(row_i=0, r1_col=0, r2_col=len(grid[0])-1):
            if (row_i >= len(grid)):
                return 0
            
            if tuple([row_i, r1_col, r2_col]) in cache:
                return cache[tuple([row_i, r1_col, r2_col])]
            
            curr_picked = grid[row_i][r1_col] + grid[row_i][r2_col] if r1_col != r2_col else grid[row_i][r1_col]
            
            r1_next_cols = []
            r2_next_cols = []
            for i in range(-1, 2, 1):
                if 0 <= r1_col + i < len(grid[0]):
                    r1_next_cols.append(r1_col + i)
                if 0 <= r2_col + i < len(grid[0]):
                    r2_next_cols.append(r2_col + i)
            
            
            max_picked = []
            for r1_next_col in r1_next_cols:
                for r2_next_col in r2_next_cols:
                    max_picked.append(curr_picked + cherryPickupRec(row_i + 1, r1_next_col, r2_next_col))
            cache[tuple([row_i, r1_col, r2_col])] = max(max_picked)
            return cache[tuple([row_i, r1_col, r2_col])]
                    
        return cherryPickupRec()