class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (len(s)<=1):
            return len(s)
        
        current_substring = set({})
        current_length = 1
        max_length = 0
         
        
        left_pointer = 0
        right_pointer = 1
        
        current_substring.add(s[left_pointer])
        
        while (right_pointer < len(s)):
            left_char = s[left_pointer]
            right_char = s[right_pointer]
            
            if right_char in current_substring:
                while(right_char) in current_substring:
                    left_char = s[left_pointer]
                    current_substring.remove(left_char)
                    left_pointer += 1
                    current_length -= 1
            
            current_substring.add(right_char)
            current_length += 1
                
            max_length = max(max_length, current_length)
            right_pointer += 1
        
        return max_length