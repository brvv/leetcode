class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        ptr2 = len(nums)-1
        ptr1 = 0
        
        while ptr1 <= ptr2:
            val1 = nums[ptr1]
            val2 = nums[ptr2]
            
            if val1 == val:
                nums[ptr1], nums[ptr2] =  nums[ptr2], nums[ptr1] 
                ptr2 -= 1
            else:
                ptr1 += 1
                
        return ptr2 +1
    
