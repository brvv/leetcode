class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #recursive with cache
        
        cache = {}
        
        def uniquePathsRec(m, n):
            if m == 1 and n == 1:
                return 1
            
            if tuple([m,n]) in cache:
                return cache[tuple([m,n])]
            
            top, left = 0, 0
            if m-1 >= 0:
                top =  uniquePathsRec(m - 1, n) 
            
            if n-1 >= 0:
                left = uniquePathsRec(m, n -1)
            
            cache[tuple([m,n])] = top + left
            return cache[tuple([m,n])]
        
        # dp with whole table
        
        def uniquePaths2DTable(m,n):
            table = [[1 for i in range(n)] for ii in range(m)]
            
            for row_i in range(1, len(table)):
                for col_i in range(1, len(table[row_i])):
                    table[row_i][col_i] = table[row_i-1][col_i] + table[row_i][col_i-1]
            return table[-1][-1]
            
    
        return uniquePaths2DTable(m, n)