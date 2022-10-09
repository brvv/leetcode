class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            middle = (start + end) // 2
            
            s_val = nums[start]
            e_val = nums[end]
            mid_val = nums[middle]
            
            if end - start <= 1:
                if s_val > e_val:
                    return e_val
                else:
                    return s_val
                
            
            if mid_val < s_val:
                end = middle
            elif mid_val > e_val:
                start = middle
            else:
                return s_val
        return s_val