class Solution:
    def findAdjacentPlots(self, grid: list[list[str]], pos: tuple[int, int]) -> list[tuple[int, int]]:
        gridHeight = len(grid)
        gridWidth = len(grid[0])
        
        res = []
        
        #top
        if pos[0] > 0 and grid[pos[0]-1][pos[1]] == 1:
            res.append((pos[0]-1, pos[1]))
            grid[pos[0]-1][pos[1]] = 2
        #bot
        if pos[0] < (gridHeight-1) and grid[pos[0]+1][pos[1]] == 1:
            res.append((pos[0]+1, pos[1]))
            grid[pos[0]+1][pos[1]] = 2
        #left
        if pos[1] > 0 and grid[pos[0]][pos[1]-1] == 1:
            res.append((pos[0], pos[1]-1))
            grid[pos[0]][pos[1]-1] = 2
        #right
        if pos[1] < (gridWidth-1) and grid[pos[0]][pos[1]+1] == 1:
            res.append((pos[0], pos[1]+1))
            grid[pos[0]][ pos[1]+1] = 2
        return res
    
    def performStep(self, grid, rotten_coords, steps):
        adjacent_oranges = []
        
        while rotten_coords:
            coords = rotten_coords.pop()
            adjacent = self.findAdjacentPlots(grid, coords)
            adjacent_oranges.extend(adjacent)
        
        if (adjacent_oranges):
            steps += 1
            
        
        return adjacent_oranges.copy()
        
        
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten_coords = []
        steps = 0
        
        for row_n, row in enumerate(grid):
            for item_n, item in enumerate(row):
                if item == 2:
                    rotten_coords.append((row_n, item_n))
        
        
        while rotten_coords:
            steps += 1
            rotten_coords = self.performStep(grid, rotten_coords, steps)
        
        if steps > 0:
            steps -= 1
            
        for row_n, row in enumerate(grid):
            for item_n, item in enumerate(row):
                if item == 1:
                    return -1
        return steps
        
        