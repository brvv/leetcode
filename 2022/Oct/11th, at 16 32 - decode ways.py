class Solution:
    def canCombine(self, s, index):
        return s[index] != "0" and 10 <= int(s[index] + s[index + 1]) <= 26
    
    def numDecodings(self, s: str) -> int:
        couplings = [None for i in range(len(s) + 1)]
        
        if s[0] == '0':
            return 0
        
        couplings[-1] = 1
        couplings[-2] = 1 if s[-1] != "0" else 0
        
        for i in range(len(s) - 2, -1, -1):
            if s[i] + s[i + 1] == "00":
                return 0
            
            canCombine = self.canCombine(s, i)
            if not canCombine:
                if (s[i] == "0"):
                    couplings[i] = 0
                else:
                    couplings[i] = couplings[i+1]
            else:
                if (s[i+1] == "0"):
                    couplings[i] = couplings[i+2]
                else:
                    couplings[i] = couplings[i+1] + couplings[i + 2]
        return couplings[0]
        