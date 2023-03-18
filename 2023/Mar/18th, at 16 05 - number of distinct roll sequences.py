class Solution:
    def distinctSequences(self, n: int) -> int:
        cache = {}
        mod = (10**9 + 7)
         
        def dfs(last=0, lastlast=0, index=0):
            if index >= n:
                return 1
        
            subproblem = tuple([last, lastlast, index])
            if subproblem in cache:
                return cache[subproblem]
            
            res = 0

            for i in range(1, 7):
                if last == 0 or math.gcd(i, last) == 1:
                    if last != i and lastlast != i:
                        res += dfs(i, last, index + 1) % mod
            cache[subproblem] = res
            return res

        return dfs() % mod