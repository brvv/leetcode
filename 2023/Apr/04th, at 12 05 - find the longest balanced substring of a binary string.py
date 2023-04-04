class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        
        ones = 0
        zeros = 0
            
        max_l = 0
        
        for curr in s:
            if curr == '1':
                ones += 1
                max_l = max(max_l, min(ones, zeros))
            if curr == '0':
                if ones > 0:
                    ones = 0
                    zeros = 0
                zeros += 1
        return max_l * 2