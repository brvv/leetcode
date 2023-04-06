class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        visited = [[False for item in row] for row in grid]

        def dfs(row_i, col_i):
            if row_i >= len(grid) or row_i < 0:
                return False
            elif col_i >= len(grid[row_i]) or col_i < 0:
                return False
            
            if visited[row_i][col_i]:
                return True

            cell = grid[row_i][col_i]
            visited[row_i][col_i] = True

            if cell == 1:
                return True
            
            #cell is part of island

            left = dfs(row_i, col_i - 1)
            right = dfs(row_i, col_i + 1)
            top = dfs(row_i - 1, col_i)
            bot = dfs(row_i + 1, col_i)
            return left and right and top and bot

        islands = 0

        for row_i in range(len(grid)):
            for col_i in range(len(grid[row_i])):
                if grid[row_i][col_i] == 0 and not visited[row_i][col_i]:
                    if dfs(row_i, col_i):
                        islands += 1

        return islands
