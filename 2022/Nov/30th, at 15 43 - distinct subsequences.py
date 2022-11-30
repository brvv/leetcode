class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}
        
        def numDistinctRec(index, index_t, str1, trg):
            if index_t < 0:
                return 1
            
            if index < 0:
                return 0
            
            subproblem = tuple([index, index_t])

            if subproblem in dp:
                return dp[subproblem]
            
            ch1 = str1[index]
            ch2 = trg[index_t]
            
            take = 0
            
            if ch1 == ch2:
                take = numDistinctRec(index - 1, index_t - 1, str1, trg)
            
            skip = numDistinctRec(index - 1, index_t, str1, trg)
            
            dp[subproblem] = take + skip
            return dp[subproblem]
        return numDistinctRec(len(s) - 1, len(t) - 1, s, t)