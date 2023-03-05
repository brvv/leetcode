class Solution:
    def coloredCells(self, n: int) -> int:
        if (n == 1):
            return 1
        res = [0 for i in range(n + 1)]
        res[0] = 0
        res[1] = 1
        res[2] = 5

        for i in range(3, n + 1):
            res[i] = res[i - 1] + 4 * (i - 1)
        
        return res[n]
        
