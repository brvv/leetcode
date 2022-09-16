class Solution:
    def helperRob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        left_profit = [0 for _ in nums]
        
        left_profit[0] = nums[0]
        left_profit[1] = nums[1]
        
        if len(nums) >= 3:
            left_profit[2] = max(nums[2] + nums[0], nums[1])
        
        for i in range(3, len(nums)):
            left_profit[i] = max(nums[i] + left_profit[i-3], nums[i] + left_profit[i-2], left_profit[i-1])
        print(left_profit)
            
        return max(left_profit)
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        
        left = self.helperRob(nums[:-1:])
        right = self.helperRob(nums[1::])
            
        return max(left, right)
            
        