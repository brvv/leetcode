class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}
        def lcsRec(index1, index2):
            if index1 < 0 or index2 < 0:
                return 0
            
            
            char1 = text1[index1]
            char2 = text2[index2]
            
            res = []
            
            subproblem = tuple([index1, index2])
            
            if subproblem in dp:
                return dp[subproblem]
            
            if char1 == char2:
                res.append(1 + lcsRec(index1 - 1, index2 - 1))
            else:
                res.append(lcsRec(index1 - 1, index2))
                res.append(lcsRec(index1, index2 - 1))
            
            dp[subproblem] = max(res)
            return dp[subproblem]
            
        return lcsRec(len(text1)-1, len(text2)-1)