class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        dic2 = {}
        
        for char in s:
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1
                
        for char in t:
            if char not in dic2:
                dic2[char] = 1
            else:
                dic2[char] += 1
                
                
        return dic == dic2
            
            