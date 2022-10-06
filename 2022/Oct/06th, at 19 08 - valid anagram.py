class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        count2 = {}
        
        for letter in s:
            count[letter] = 1 + count.get(letter, 0)
            
        for letter in t:
            count2[letter] = 1 + count2.get(letter, 0)
            
        return count == count2