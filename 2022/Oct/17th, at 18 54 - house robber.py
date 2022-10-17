class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def dfs(index, nums):
            if index >= len(nums):
                return 0
            
            include = None
            #include the element
            if index in cache:
                return cache[index]

            include = nums[index] + dfs(index + 2, nums)
            #don't include the element
            no_include = dfs(index + 1, nums)
            cache[index] = max(include, no_include)
            
            return cache[index]
        return dfs(0, nums)