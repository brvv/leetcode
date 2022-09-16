class Solution:
    def countBits(self, n: int) -> List[int]:
        # [0,1, | 1,2, | 1,2,2,3, | 1 2 2 3 2 3 3 4 ]
        # [1 1  | 2 2  | 3 3 3 3  | 4 4 4 4 4 4 4 4 ]
        # [0 1  | 2 3  | 4 5 6 7  | 8 9 10 11]
        # 1000 1001 1010 1011 1100 1101 1110 1111
        # 
        # 
        res = [0 for _ in range(n+1)]
        
        if n == 0:
            return [0]
        
        res[0] = 0
        res[1] = 1
    
        if n == 1:
            return res
        
        
        currentMod = 2
        
        for i in range(2, len(res)):
            if (i == currentMod * 2):
                currentMod *= 2
            
            res[i] = 1 + res[i % currentMod]
        
        return res
            