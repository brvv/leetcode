class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}
        
        def dfs(text1, text2, index1=0, index2=0):
            if index1 >= len(text1) or index2>=len(text2):
                return 0
            
            if tuple([index1, index2]) in cache:
                return cache[tuple([index1, index2])]
            
            letter1 = text1[index1]
            letter2 = text2[index2]
            
            if letter1 == letter2:
                val = 1 + dfs(text1, text2, index1 + 1, index2 + 1)
            else:
                val = max(dfs(text1, text2, index1 + 1, index2), dfs(text1, text2, index1, index2 + 1))
            cache[tuple([index1, index2])] = val
            return cache[tuple([index1, index2])]
            
        return dfs(text1, text2)