class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        
        def dfs(subset, i):
            if (i >= len(nums)):
                subsets.append(subset)
                return
            
            dfs(subset + [nums[i]], i+1)
            dfs(subset, i + 1)
            
        dfs([], 0)
        return subsets