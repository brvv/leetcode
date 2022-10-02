class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(perm, choice):
            if len(choice) == 0:
                res.append(perm.copy())
                return
            
            for item in choice:
                dfs(perm + [item], choice - {item})
                
        dfs([], set(nums))
        
        return res