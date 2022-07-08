class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        
        def dfs(depth=0, total=0):
            if total == target:
                res.append(subset.copy())
                return
            
            if depth >= len(candidates) or total > target:
                return
            
            subset.append(candidates[depth])
            dfs(depth, total + candidates[depth])
            
            subset.pop()
            dfs(depth + 1, total)
        
        dfs()
        return res