class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        def countPatternSubseq(str1, pattern):
            ch1 = pattern[0]
            ch2 = pattern[1]
            
            #make sure not the same index in case pattern consists of two same letters
            ch1_indexes = []
            ch2_indexes = []
            
            res = 0
            
            for i, letter in enumerate(str1):
                if letter == ch1:
                    ch1_indexes.append(i)
                
                if letter == ch2:
                    ch2_indexes.append(i)
                    
            bigger = [0 for _ in str1]
            ch2_indexes_ptr = len(ch2_indexes) - 1
            
            
            for i in range(len(bigger) -2 , -1 ,-1):
                bigger[i] += bigger[i + 1]
                if ch2_indexes_ptr >= 0 and ch2_indexes[ch2_indexes_ptr] > i:
                    bigger[i] += 1
                    ch2_indexes_ptr -= 1
                     
                
            for ch1_i in ch1_indexes:
                res += bigger[ch1_i]
            return res
                    
            
        text1 = [pattern[0]] + list(text)
        text2 = list(text) + [pattern[1]]
        
        res1 = countPatternSubseq(text1, pattern)
        res2 = countPatternSubseq(text2, pattern)
        
        return max(res1, res2)
        