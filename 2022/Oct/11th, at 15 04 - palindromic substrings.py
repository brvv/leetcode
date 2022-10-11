class Solution:
    def is_palindrome(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
    def get_palindromes_from_index(self, start_index, s):
        left = start_index
        right = start_index
        count = 0
        
        while s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
            
            if (left < 0) or (right >= len(s)):
                break
        
        left = start_index - 1
        right = start_index
                
        while left >= 0 and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
            
            if (left < 0) or (right >= len(s)):
                break
        
        return count
    
    def countSubstrings(self, s: str) -> int:
        count = 0
        
        start = 0
        for i in range(len(s)):
            count += self.get_palindromes_from_index(i, s)
        return count