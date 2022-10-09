class Solution:
    def findPivot(self, nums):
        start = 0
        end = len(nums) - 1
        
        while start < end:
            middle = (start + end) // 2
            start_val = nums[start]
            end_val = nums[end]
            mid_val = nums[middle]
            
            
            if end - start <= 1:
                if start_val < end_val:
                    return start
                else:
                    return end
            
            if mid_val < start_val:
                end = middle
                
            elif mid_val > end_val:
                start = middle
            else:
                return start
        return start
                
    def getTrueValueInRotated(self, nums, index, pivot):
        return nums[(pivot + index)%len(nums)]
    
    
    def search(self, nums: List[int], target: int) -> int:
        pivot_index = self.findPivot(nums)
        
        start = 0
        end = len(nums) - 1
        
        print(pivot_index)
        
        while start <= end:
            middle = (start + end) // 2
            start_val = self.getTrueValueInRotated(nums, start, pivot_index)
            end_val = self.getTrueValueInRotated(nums, end, pivot_index)
            mid_val = self.getTrueValueInRotated(nums, middle, pivot_index)
            
            if target < mid_val:
                end = middle - 1
            elif target > mid_val:
                start = middle + 1
            else:
                return (pivot_index + middle) % len(nums)
        return -1
                