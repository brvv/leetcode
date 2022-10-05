class Solution:
    def canJump(self, nums: List[int]) -> bool:
        canReach = [False for _ in nums]
        lastReachable = len(nums) - 1
        canReach[-1] = True
        
        
        for i in range(len(nums) - 2, -1, -1):
            jumpValue = nums[i]
            
            if i + jumpValue >= lastReachable:
                canReach[i] = True
                lastReachable = i
        return canReach[0]