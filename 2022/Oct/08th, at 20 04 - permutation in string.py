class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic1 = {}
        dic2 = {}
        
        for char in "abcdefghijklmnopqrstuvwxyz":
            dic1[char] = 0
            dic2[char] = 0
        
        characters = [0 for char in range(26)]
        for char in s1:
            dic1[char] = 1 +  dic1.get(char, 0)
            
        s2_slice = s2[0 : len(s1)]
        for char in s2_slice:
            dic2[char] = 1 + dic2.get(char, 0)
            

        for i in range(1, len(s2) - len(s1) + 1):
            if dic1 == dic2:
                return True
            
            removed_char = s2[i-1]
            added_char = s2[i + len(s1)-1]
            
            dic2[removed_char] = dic2.get(removed_char, 1) - 1
            dic2[added_char] = 1 + dic2.get(added_char, 0)

        if dic1 == dic2:
            return True

        return False
            