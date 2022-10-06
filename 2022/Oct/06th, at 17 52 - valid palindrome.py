class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
        word = ''
        alpha_set = set(list(alphabet))

        
        for letter in s:
            if letter.lower() in alpha_set:
                word += letter
                
        ptr1 = 0
        ptr2 = len(word) - 1
        
        while ptr1 < ptr2:         
            print(word[ptr1], word[ptr2])
            if word[ptr1].lower() != word[ptr2].lower():
                return False
            else:
                ptr1 += 1
                ptr2 -=1
                
        return True