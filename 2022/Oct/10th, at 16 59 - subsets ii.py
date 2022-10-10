class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        vals = sorted(nums)
        used_values = set({})
        res = []
        
        def dfs(nums, subset=[], level=0):
            if level >= len(nums):
                res.append(subset)
                return
                
            current_num = nums[level]
            
            dfs(nums, subset + [current_num], level + 1)
            
            while level + 1 < len(nums) and nums[level] == nums[level + 1]:
                level += 1
            dfs(nums, subset, level + 1)
        dfs(vals)
        return res