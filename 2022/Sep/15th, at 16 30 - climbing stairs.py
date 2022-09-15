class Solution:
    def climbStairs(self, n: int) -> int:
        lst = [None for _ in range(n+1)]
        
        lst[-1] = 1
        
        lst[-2] = 1
            
        
        for i in range(n-2, -1, -1):
            lst[i] = lst[i + 1] + lst[i + 2]
        print(lst)
        return lst[0]