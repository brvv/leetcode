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
            
        #2d table
        def minimumTotalTable():
            table = [[elem for elem in row] for row in triangle]
            for row_i, row in enumerate(table):
                for col_i, cost in enumerate(row):
                    if row_i == 0 and col_i == 0:
                        table[row_i][col_i] = cost
                        continue
                            
                    left_parent = table[row_i - 1][col_i - 1] if col_i - 1 >= 0 else 100000000000000000000
                    right_parent = table[row_i - 1][col_i] if col_i < len(table[row_i-1]) else 1000000000000000000000
                    
                    table[row_i][col_i] = cost + min(left_parent, right_parent)
            return min(table[-1])
        
        return minimumTotalTable()