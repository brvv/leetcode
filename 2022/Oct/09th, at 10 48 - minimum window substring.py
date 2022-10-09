class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic1 = {}
        dic2 = {}
        match_chars = 0
                
        
        for char in t:
            dic1[char] = 1 + dic1.get(char, 0)
            
        for key in dic1:
            match_chars += 1
            
        
        ptr1 = 0
        ptr2 = 0
        dic2_matches = 0
        min_len = 10**6
        min_word = ""
        
        while ptr2 < len(s):
            
            
            char = s[ptr2]
            dic2[char] = 1 + dic2.get(char, 0)
            
            if char in dic1 and dic2[char] == dic1[char]:
                dic2_matches += 1
        
            #remove characters from the left 
            while match_chars == dic2_matches:
                first_char = s[ptr1]
                
                if (ptr2 - ptr1 + 1) < min_len:
                    min_len = ptr2 - ptr1 + 1
                    min_word = s[ptr1 : ptr2 + 1]
                
                
                dic2[first_char] -= 1
                if first_char in dic1 and dic2[first_char] < dic1[first_char]:
                    dic2_matches -= 1
                ptr1 += 1
            ptr2 += 1
            
                    
        
        return min_word