class Solution:
    
    def findAdjacentPlots(self, grid: list[list[str]], visited_matrix : list[list[bool]], pos: tuple[int, int]) -> list[tuple[int, int]]:
        gridHeight = len(grid)
        gridWidth = len(grid[0])
        
        res = []
        
        #top
        if pos[0] > 0 and not visited_matrix[pos[0]-1][pos[1]] and grid[pos[0]-1][pos[1]] == "1":
            res.append((pos[0]-1, pos[1]))
            visited_matrix[pos[0]-1][pos[1]] = True
        #bot
        if pos[0] < (gridHeight-1) and not visited_matrix[pos[0]+1][pos[1]] and grid[pos[0]+1][pos[1]] == "1":
            res.append((pos[0]+1, pos[1]))
            visited_matrix[pos[0]+1][pos[1]] = True
        #left
        if pos[1] > 0 and not visited_matrix[pos[0]][pos[1]-1] and grid[pos[0]][pos[1]-1] == "1":
            res.append((pos[0], pos[1]-1))
            visited_matrix[pos[0]][pos[1]-1] = True
        #right
        if pos[1] < (gridWidth-1) and not visited_matrix[pos[0]][pos[1]+1] and grid[pos[0]][pos[1]+1] == "1":
            res.append((pos[0], pos[1]+1))
            visited_matrix[pos[0]][pos[1]+1] = True
        return res
    
                        
                        
    def markAdjacentLandPlots(self, grid: list[list[str]], visited_matrix : list[list[bool]], pos: tuple[int, int]):
        gridHeight = len(grid)
        gridWidth = len(grid[0])
        
        
        stack = []
        stack.append((pos[0], pos[1]))
        
        while stack:
            coordinates = stack.pop()
            neighbours = self.findAdjacentPlots(grid, visited_matrix, coordinates)
            if neighbours:
                stack.extend(neighbours)
            
                        
    
    def numIslands(self, grid: list[list[str]]) -> int:
        visited_matrix = [[False for item in row] for row in grid]
        islands_count = 0
        
        for row_num in range(len(grid)):
            for col_num in range(len(grid[0])):
                item = grid[row_num][col_num]
                if not visited_matrix[row_num][col_num]:
                    visited_matrix[row_num][col_num] = True
                    
                    if item == "1":
                        islands_count += 1
                        self.markAdjacentLandPlots(grid, visited_matrix, (row_num, col_num))
        return islands_count            

