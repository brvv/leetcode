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
        
        def lcsTable(str1, str2):
            table = [[0 for c2 in str2] for c1 in str1]
            
            
            for row_i in range(len(table)):
                row = table[row_i]
                for col_i in range(len(row)):
                    left = table[row_i][col_i - 1] if col_i > 0 else 0
                    top = table[row_i-1][col_i] if row_i > 0 else 0
                    left_top = table[row_i-1][col_i-1] if col_i > 0 and row_i > 0 else 0

                    c1 = str1[row_i]
                    c2 = str2[col_i]
                    
                    if c1 == c2:
                        table[row_i][col_i] = left_top + 1
                    else:
                        table[row_i][col_i] = max(left, top)
            return table[-1][-1]
        
        def lcsRecPrint(index1, index2):
            if index1 < 0 or index2 < 0:
                return ""
            
            
            char1 = text1[index1]
            char2 = text2[index2]
            
            res = []
            
            subproblem = tuple([index1, index2])
            
            if subproblem in dp:
                return dp[subproblem]
            
            if char1 == char2:
                res.append(char1 + lcsRecPrint(index1 - 1, index2 - 1))
            else:
                res.append(lcsRecPrint(index1 - 1, index2))
                res.append(lcsRecPrint(index1, index2 - 1))
            
            longest_str = ""
            
            for s in res:
                if len(s) > len(longest_str):
                    longest_str = s
            dp[subproblem] = longest_str
            return dp[subproblem]
        
        lcs = lcsRecPrint(len(text1)-1, len(text2)-1)
        lcs = lcs[::-1]
        
        return len(lcs)