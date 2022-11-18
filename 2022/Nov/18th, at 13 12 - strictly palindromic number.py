class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def isPalindrome(s):
            start = 0
            end = len(s) - 1
            while start <= end:
                chr1 = s[start]
                chr2 = s[end]
                
                if chr1 != chr2:
                    return False
                
                start += 1
                end -= 1
            return True
        
        def getNumInBase(n, base):
            if n == 0:
                return '0'
            res = ""
            
            while n > 0:
                n, r = divmod(n, base)
                res += str(r)
            return res
        
        for base in range(2, n - 1):
            if not isPalindrome(getNumInBase(n, base)):
                return False
        return True