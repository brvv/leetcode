class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        visited = [[False for item in row] for row in grid]

        def dfs(row_i, col_i):
            if row_i >= len(grid) or row_i < 0:
                return False, 0
            elif col_i >= len(grid[row_i]) or col_i < 0:
                return False, 0
            
            if visited[row_i][col_i]:
                return True, 0

            cell = grid[row_i][col_i]
            visited[row_i][col_i] = True

            if cell == 0:
                return True, 0
            
            #cell is part of island

            left, left_count = dfs(row_i, col_i - 1)
            right, right_count = dfs(row_i, col_i + 1)
            top, top_count = dfs(row_i - 1, col_i)
            bot, bot_count = dfs(row_i + 1, col_i)
            is_enclave = left and right and top and bot
            cell_count = 1 + left_count + right_count + top_count + bot_count
            return is_enclave, cell_count

        islands = 0

        for row_i in range(len(grid)):
            for col_i in range(len(grid[row_i])):
                if grid[row_i][col_i] == 1 and not visited[row_i][col_i]:
                    is_enclave, count = dfs(row_i, col_i)

                    if is_enclave:
                        islands += count

        return islands