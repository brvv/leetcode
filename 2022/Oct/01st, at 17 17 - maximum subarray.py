class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = [None for i in nums]
        sums[0] = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            sums[i] = max(sums[i-1] + nums[i], nums[i])
        return max(sums)