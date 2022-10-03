class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}
        
        def dfs(s, wordDict, trueStartIndex=0):
            if (trueStartIndex in cache):
                return False
            
            if len(s) == 0 or s in wordDict:
                return True
            
            startIndex = 0
            endIndex = 1
            
            for i in range(1, len(s)):
                endIndex = i
                word = s[startIndex:endIndex]
                if word =="":
                    
                    return False
                
                if word in wordDict:
                    res = dfs(s[endIndex:], wordDict, trueStartIndex + endIndex)
                    if res:
                        return True
                    else:
                        continue
            cache[trueStartIndex] = False
            return False
        return dfs(s, wordDict)