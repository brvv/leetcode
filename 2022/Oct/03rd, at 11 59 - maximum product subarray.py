class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # O(1) space solution
        global_max = max(nums)
        curr_max = 1
        curr_min = 1
        
        for i in range(len(nums)):
            num = nums[i]
            
            if num == 0:
                curr_max = 1
                curr_min = 1
                
            local_val = num * curr_max
            
            curr_max = max(local_val, curr_min * num, num)
            curr_min = min(local_val, curr_min * num, num)
                
                
            global_max = max(global_max, curr_max, curr_min)
            
        return global_max