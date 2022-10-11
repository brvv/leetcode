class Solution:
    def get_largest_palindrome(self, s, start_index):
        left = start_index
        right = start_index
        count1 = -1
        pali1 = ""
        
        
        
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                pali1 = s[left:right + 1]
                count1 += 2
                left -= 1
                right +=1
                
            else:
                break
                
        
                
        left = start_index
        right = start_index+1
        count2 = 0
        pali2 = ""
        
        
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                count2 += 2
                pali2 = s[left:right + 1]
                left -= 1
                right +=1
                
            else:
                break
        
        if count1 > count2:
            return pali1
        else:
            return pali2
    
    def longestPalindrome(self, s: str) -> str:
        max_pali = ""
        
        for i in range(len(s)):
            pali =self.get_largest_palindrome(s, i)
            if len(pali) >= len(max_pali):
                max_pali = pali
        return max_pali