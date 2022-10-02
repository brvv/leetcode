class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        
        def dfs(nums, current_sum, n, target):
            if n == len(nums):
                if current_sum == target:
                    return 1
                elif current_sum == target:
                    return 1
                else:
                    return 0
            if tuple([current_sum, n]) in cache:
                return cache[tuple([current_sum, n])]
            
            cache[tuple([current_sum, n])] = dfs(nums, current_sum + nums[n], n + 1, target) + dfs(nums, current_sum - nums[n], n + 1, target)
        
            return cache[tuple([current_sum, n])]
        
        return dfs(nums, 0, 0, target)