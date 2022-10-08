class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic = {}
        
        characters = [0 for char in range(26)]
        for char in s1:
            characters[ord(char) - ord('a')] += 1
        dic[tuple(characters)] = True
            
        for i in range(0, len(s2) - len(s1) + 1):
            s2_slice = s2[i : i + len(s1)]
            
            new_characters = [0 for char in range(26)]
            for char in s2_slice:
                new_characters[ord(char) - ord('a')] += 1
            
            if tuple(new_characters) in dic:
                return True

        return False
            