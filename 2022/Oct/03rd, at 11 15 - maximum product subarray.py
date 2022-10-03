class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_array = [1 for num in nums]
        max_array_abs = [1 for num in nums]
        max_array_abs_right = [1 for num in nums]
        
        max_array[0] = nums[0]
        max_array_abs[0] = nums[0]
        max_array_abs_right[-1] = nums[-1]
        
        for i in range(1, len(nums)):
            num = nums[i]
            
            max_array[i] = max(num, num * max_array[i-1])
            
            if (abs(num) > abs(num * max_array_abs[i-1])):
                max_array_abs[i] = num
            else:
                max_array_abs[i] = num * max_array_abs[i-1]
                
        for i in range(len(nums) - 2, -1, -1):
            num = nums[i]
            if (abs(num) > abs(num * max_array_abs_right[i+1])):
                max_array_abs_right[i] = num
            else:
                max_array_abs_right[i] = num * max_array_abs_right[i+1]
            
        print(max_array, max_array_abs, max_array_abs_right)    
        
        return max(max_array + max_array_abs + max_array_abs_right)