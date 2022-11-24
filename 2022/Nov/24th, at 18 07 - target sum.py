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
        
        def targetSumTable(nums, target):
            # row = current_sum
            # col = current_index
            offset = 1000
            table = [[0 for i in range(2000+1)] for j in range(len(nums))]
            
            table[0][nums[0] + offset] += 1
            table[0][-nums[0] + offset] += 1
            
            for row_i in range(0, len(table)-1):
                row = table[row_i]
                for col_i, count in enumerate(row):
                    if count != 0:
                        next_val = nums[row_i+1]
                        
                        table[row_i+1][col_i + next_val] += count
                        table[row_i+1][col_i - next_val] += count
            
            return table[-1][target+offset]
            
        return targetSumTable(nums, target)