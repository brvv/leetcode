class Solution:
    def helperRob(self, nums: List[int]) -> int:
        tab = [0 for i in nums]
        
        if len(nums) <= 2:
            return max(nums)
        
        tab[-1] = nums[-1]
        tab[-2] = nums[-2]
        tab[-3] = nums[-3] + tab[-1]
        
        for i in range(len(tab)-4, -1, -1):
            tab[i] = max(nums[i] + tab[i + 2], nums[i] + tab[i + 3])
        
        return max(tab)
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        
        left = self.helperRob(nums[:-1:])
        right = self.helperRob(nums[1::])
            
        return max(left, right)
            
        