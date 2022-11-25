class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        def findIndexes(str1, lcs):
            ptr_s = 0
            ptr_lcs = 0
            ans = []
            
            while ptr_lcs < len(lcs):
                char = str1[ptr_s]
                char_lcs = lcs[ptr_lcs]
                
                if char == char_lcs:
                    ans.append(ptr_s)
                    ptr_lcs += 1
                ptr_s += 1
            return ans
        
        text1 = str1
        text2 = str2
        
        dp = {}
        
        def lcsRec(index1, index2):
            if index1 < 0 or index2 < 0:
                return ""
            
            
            char1 = text1[index1]
            char2 = text2[index2]
            
            res = []
            
            subproblem = tuple([index1, index2])
            
            if subproblem in dp:
                return dp[subproblem]
            
            if char1 == char2:
                res.append(char1 + lcsRec(index1 - 1, index2 - 1))
            else:
                res.append(lcsRec(index1 - 1, index2))
                res.append(lcsRec(index1, index2 - 1))
            
            longest_str = ""
            
            for s in res:
                if len(s) > len(longest_str):
                    longest_str = s
            dp[subproblem] = longest_str
            return dp[subproblem]
        
        lcs = lcsRec(len(text1)-1, len(text2)-1)
        lcs = lcs[::-1]
        
        lcs_indexes1 = findIndexes(str1, lcs)
        lcs_indexes2 = findIndexes(str2, lcs)
        
        print(lcs, lcs_indexes1, lcs_indexes2)
        
        ans = ""
        
        ans += str1[0:lcs_indexes1[0]]
        ans += str2[0:lcs_indexes2[0]]
        
        ans += lcs[0]
        
        for i in range(1, len(lcs)):
            
            if lcs_indexes1[i] - lcs_indexes1[i-1] > 1:
                ans += str1[lcs_indexes1[i-1]+1:lcs_indexes1[i]]
        
            if lcs_indexes2[i] - lcs_indexes2[i-1] > 1:
                ans += str2[lcs_indexes2[i-1]+1:lcs_indexes2[i]]
            
            ans += lcs[i]
            
            
        if (lcs_indexes1[-1] + 1 < len(str1)):
            ans += str1[lcs_indexes1[-1]+1:]
        
            
        if (lcs_indexes2[-1] + 1 < len(str2)):
            ans += str2[lcs_indexes2[-1]+1:]
        
        return ans
                
                
        