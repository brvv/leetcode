class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # recursive solution
        # with memoization
        cache = {}
        def uniquePathsRec(row_i, col_i):
            if obstacleGrid[row_i][col_i] == 1:
                return 0
            
            if row_i == 0 and col_i == 0:
                return 1
            
            if tuple([row_i, col_i]) in cache:
                return cache[tuple([row_i, col_i])] 
            
            left = 0
            top = 0
            if row_i - 1 >= 0:
                top = uniquePathsRec(row_i - 1, col_i)
            
            if col_i - 1 >= 0:
                left = uniquePathsRec(row_i, col_i-1)
            cache[tuple([row_i, col_i])] = top + left
            return cache[tuple([row_i, col_i])]
        
        # O(n * m)Table dynamic programming solution
        
        def uniquePathsDynamic():
            table = [[0 for item in row] for row in obstacleGrid]
                    
            for row_i, row in enumerate(table):
                for col_i, item in enumerate(row):
                    if obstacleGrid[row_i][col_i] == 1:
                        table[row_i][col_i] = 0
                    elif row_i == 0 and col_i == 0:
                        table[row_i][col_i] = 1
                    else:
                        left = 0
                        top = 0
                        
                        if row_i - 1 >= 0:
                            top = table[row_i-1][col_i]
                        
                        if col_i - 1 >= 0:
                            left = table[row_i][col_i-1]
                        table[row_i][col_i] = left + top
                        
                    # Table dynamic programming solution
        
        # O( m * 2) row dynamic programming
        
        def uniquePathsDynamic1Row():
            row = [0 for item in obstacleGrid[0]]
                    
            for row_i, obstacle_row in enumerate(obstacleGrid):
                new_row = [0 for item in obstacleGrid[0]]
                
                for col_i, item in enumerate(obstacle_row):
                    if obstacleGrid[row_i][col_i] == 1:
                        new_row[col_i] = 0
                    elif row_i == 0 and col_i == 0:
                        new_row[col_i] = 1
                    else:
                        left = 0
                        top = 0
                        
                        if row_i - 1 >= 0:
                            top = row[col_i]
                        
                        if col_i - 1 >= 0:
                            left = new_row[col_i-1]
                        new_row[col_i] = left + top
                row = new_row
            
            
            return row[-1]
    
        return uniquePathsDynamic1Row()