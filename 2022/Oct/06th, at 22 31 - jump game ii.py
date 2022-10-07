class Solution:
    def jump(self, nums: List[int]) -> int:
        jump_vals = [None for i in nums]
        jump_vals[-1] = 0
        
        for i in range(len(nums)-2, -1, -1):
            max_jump_distance = min(len(jump_vals), i + nums[i]+1)
            
            if nums[i] == 0:
                jump_vals[i] = 2000
                continue
            
            jump_vals[i] = 1 + min(jump_vals[i+1:max_jump_distance])
        return jump_vals[0]
            
            
            
        