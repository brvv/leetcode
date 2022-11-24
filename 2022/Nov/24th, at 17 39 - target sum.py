class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        
        def targetSumRec(index, current_sum):
            if index == -1:
                if current_sum == 0:
                    return 1
                return 0
            
            subproblem = tuple([index, current_sum])
            
            if subproblem in dp:
                return dp[subproblem]
            
            current_pos = targetSumRec(index - 1, current_sum + nums[index])
            current_neg = targetSumRec(index - 1, current_sum - nums[index])
            
            dp[subproblem] = current_pos + current_neg
            return dp[subproblem]
        return targetSumRec(len(nums)-1, target)