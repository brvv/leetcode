class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first = max(nums[0]-1, nums[1]-1)
        second = min(nums[0]-1, nums[1]-1)

        for i in range(2, len(nums)):
            num = nums[i] - 1

            if num >= first:
                second = first
                first = num
            elif num >= second:
                second = num
        
        return first * second