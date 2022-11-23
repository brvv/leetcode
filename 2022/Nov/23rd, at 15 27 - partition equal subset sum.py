class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        
        if sum(nums) % 2 != 0:
            return False
        
        dp = {}
        
        def canPartRec(index, psum, target):
            if index < 0:
                if psum == target:
                    return True
                return False
            
            if psum > target:
                return False
            
            cell = tuple([index, psum])
            if cell in dp:
                return dp[cell]
            
            include = canPartRec(index - 1, psum + nums[index], target)
            
            if include:
                return include
            
            skip = canPartRec(index - 1, psum, target)
            
            dp[cell] = include or skip
            
            return dp[cell]
        
        return canPartRec(len(nums)-1, 0, sum(nums)//2)