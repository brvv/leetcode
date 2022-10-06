class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        
        left = 0
        right = len(nums) - 1
        
        
        
        while True:
            middle = (left + right) // 2
            
            isLeftSorted = nums[middle] >= nums[left]
            isRightSorted = nums[middle] <= nums[right]
            
            if isLeftSorted and isRightSorted:
                return nums[left]
            
            if isLeftSorted:
                left = middle + 1
                continue
                
            else:
                right = middle
                continue
        