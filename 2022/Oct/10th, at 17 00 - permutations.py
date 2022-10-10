class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(perm, available):
            if len(available) == 0:
                res.append(perm.copy())
                return
            
            for item in available:
                dfs(perm + [item], available - {item})
                
        dfs([], set(nums))
        
        return res