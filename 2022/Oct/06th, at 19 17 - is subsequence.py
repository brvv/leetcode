class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sub_ptr = 0
        word_ptr = 0
        
        while sub_ptr < len(s) and word_ptr < len(t):
            char_sub = s[sub_ptr]
            char_word = t[word_ptr]
            
            if char_sub == char_word:
                sub_ptr += 1
            word_ptr += 1
        return sub_ptr == len(s)