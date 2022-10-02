#numbers 1 .. n inclusive

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        
        def dfs(comb, n, k):
            if k == 0:
                combinations.append(comb)
                return
            
            prevValue = None
            
            if (comb == []):
                prevValue = 0
            else:
                prevValue = comb[-1]
                
            for i in range(prevValue + 1, n + 1):
                dfs(comb + [i], n, k-1)
                
        dfs([], n, k)
        return combinations
                