class Solution:
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1
        while left <= right:
            left_c = s[left]
            right_c = s[right]
            if left_c != right_c:
                return False
            left += 1
            right -= 1
        return True
    
    def longestPalindromeSubseq(self, s: str) -> int:
        cache = {}
        max_seq = {}
        max_seq[0] = []
        
        
        #recursive dynamic programming solution
        def dfs(text1, text2, index1=0, index2=0, seq=[]):
            if index1 >= len(text1) or index2>=len(text2):
                if len(seq) > len(max_seq[0]) and self.isPalindrome(seq):
                    max_seq[0] = seq
                return 0
            
            if tuple([index1, index2]) in cache:
                return cache[tuple([index1, index2])]
            
            letter1 = text1[index1]
            letter2 = text2[index2]
            
            if letter1 == letter2:
                val = 1 + dfs(text1, text2, index1 + 1, index2 + 1, seq + [letter1])
            else:
                val = max(dfs(text1, text2, index1 + 1, index2, seq), dfs(text1, text2, index1, index2 + 1, seq))
            cache[tuple([index1, index2])] = val
            return cache[tuple([index1, index2])]
        
        #longest palindromic subsequence is the longest common subsequence between a string and its reverse
        res = dfs(s, s[::-1])

        return res