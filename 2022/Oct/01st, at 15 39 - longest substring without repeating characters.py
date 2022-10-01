class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (len(s) == 0):
            return 0
        
        if (len(s) == 1):
            return 1
        
        
        char_set = set()
        ptr1 = 0

        max_size = 1
        
        for ptr2 in range(len(s)):
            char2 = s[ptr2]
            
            
            while (char2 in char_set):
                char1 = s[ptr1]
                char_set.remove(char1)
                ptr1 += 1
                
            char_set.add(char2)
            max_size = max(max_size, len(char_set))
                
        return max_size
    