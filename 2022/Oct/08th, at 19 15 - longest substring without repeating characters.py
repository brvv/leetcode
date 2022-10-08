class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        longest = 0
        ptr1 = 0
        ptr2 = 0
        
        while (ptr2 < len(s)):

            char = s[ptr2]
            
            while char in substring:
                other = s[ptr1]
                substring.remove(other)
                ptr1 += 1
            
            substring.add(char)
            longest = max(len(substring), longest)
            ptr2 += 1
        return longest