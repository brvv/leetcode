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
    
        return uniquePathsRec(len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1)