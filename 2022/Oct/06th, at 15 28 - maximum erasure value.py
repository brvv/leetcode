class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        max_score = 0
        current_score = 0
        
        elements = {} # val to index
        
        if len(nums) == 1:
            return nums[0]
        
        
        ptr1 = 0
        ptr2 = 0

        max_score = nums[0]
        
        while ptr2 < len(nums):
            val = nums[ptr2]
            
            if nums[ptr2] not in elements:
                elements[val] = ptr2
                current_score += val
                max_score = max(max_score, current_score)
                ptr2 += 1
            else:
                
                while nums[ptr2] in elements:
                    
                    del_val = nums[ptr1]
                    current_score -= del_val
                    del elements[del_val]
                    ptr1 += 1
        return max_score
        