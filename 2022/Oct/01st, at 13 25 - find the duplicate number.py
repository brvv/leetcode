class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tort = nums[0]
        hare = nums[0]
        
        intersection = None
        cycle_start = None
        
        while True:
            tort = nums[tort]
            hare = nums[hare]
            hare = nums[hare]
            
            if tort == hare:
                intersection = hare
                break
                
        second_tort = nums[0]
        
        while tort != second_tort:
            tort = nums[tort]
            second_tort = nums[second_tort]
            
        cycle_start = second_tort
        
        return cycle_start