class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        #recursion with memoization
        cache = {}
        def minimumTotalRec(row_i=0, col_i=0):
            current_cost = triangle[row_i][col_i]
            if row_i == len(triangle) - 1:
                return triangle[row_i][col_i]
            
            if tuple([row_i, col_i]) in cache:
                return cache[tuple([row_i, col_i])]
            
            left = current_cost + minimumTotalRec(row_i + 1, col_i)
            right = current_cost + minimumTotalRec(row_i + 1, col_i + 1)
            
            
            cache[tuple([row_i, col_i])] = min(left, right)
            
            return cache[tuple([row_i, col_i])]
        
        return minimumTotalRec()