class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #recursive with cache
        
        cache = {}
        
        def uniquePathsRec(m, n):
            if m == 0 and n == 0:
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
    
        return uniquePathsRec(m-1, n-1)